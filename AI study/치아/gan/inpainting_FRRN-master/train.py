import os 
import yaml 
import random
import argparse

import numpy as np

from utils.general import get_config
from utils.masks import get_constant_mask
from utils.progbar import Progbar
from model.net import InpaintingModel
from data.dataset import Dataset
from scripts.metrics import compute_metrics
from utils.model import random_crop


os.system("clear")
def main(config_path, experiment_path):
    # ARGS 
    masks_path = None
    training = True

    # load config
    code_path = '/'
    config, pretty_config = get_config(os.path.join(code_path, config_path))
    config['path']['experiment'] = os.path.join(experiment_path, config['path']['experiment'])

    print('\nModel configurations:'\
          '\n---------------------------------\n'\
          + pretty_config +\
          '\n---------------------------------\n')

    os.environ['CUDA_VISIBLE_DEVICES'] = config['gpu']

    # Import Torch after os env
    import torch
    import torchvision
    from torch import nn
    from torch.utils.tensorboard import SummaryWriter
    from torchvision.utils import save_image

    # init device
    if config['gpu'] and torch.cuda.is_available():
        device = torch.device("cuda")
        torch.backends.cudnn.benchmark = True   # cudnn auto-tuner
    else:
        device = torch.device("cpu")

    # initialize random seed
    torch.manual_seed(config["seed"])
    torch.cuda.manual_seed_all(config["seed"])
    if not training:
        np.random.seed(config["seed"])
        random.seed(config["seed"])

    # parse args
    images_path = config['path']['train']
    checkpoint = config['path']['experiment']
    discriminator = config['training']['discriminator']

    # initialize log writer
    logger = SummaryWriter(log_dir=config['path']['experiment'])

    # build the model and initialize
    inpainting_model = InpaintingModel(config).to(device)
    if checkpoint:
        inpainting_model.load()
    
    pred_directory = os.path.join(checkpoint, 'predictions')
    if not os.path.exists(pred_directory):
        os.makedirs(pred_directory)

    # generator training
    if training:
        print('\nStart training...\n')
        batch_size = config['training']['batch_size']

        # create dataset
        dataset = Dataset(config, training=True)
        train_loader = dataset.create_iterator(batch_size)

        test_dataset = Dataset(config, training=False)

        # Train the generator
        total = len(dataset)
        if total == 0:
            raise Exception("Dataset is empty!")

        # Training loop
        epoch = 0
        for i, items in enumerate(train_loader):
            inpainting_model.train()

            if i % total == 0:
                epoch += 1
                print('Epoch', epoch)
                progbar = Progbar(total, width=20, stateful_metrics=['iter'])
            
            images, masks, constant_mask = items['image'], items['mask'], items['constant_mask']

            del items
            if config['training']['random_crop']:
                images, masks, constant_mask = random_crop(images, masks, constant_mask, 
                                                           config['training']['strip_size'])
            images, masks, constant_mask = images.to(device), masks.to(device), constant_mask.to(device)

            if discriminator:
                # Forward pass
                outputs, residuals, gen_loss, dis_adv_loss, logs = inpainting_model.process(images, masks, constant_mask)    
                del masks, constant_mask, residuals
                loss = gen_loss + dis_adv_loss
                # Backward pass
                inpainting_model.backward(gen_loss, dis_adv_loss)
            else:
                # Forward pass
                outputs, residuals, loss, logs = inpainting_model.process(images, masks, constant_mask)    
                del masks, constant_mask, residuals
                # Backward pass
                inpainting_model.backward(loss)
            
            step = inpainting_model._iteration
            
            # Adding losses to Tensorboard
            for log in logs:
                logger.add_scalar(log[0], log[1], global_step=step)

            if i % config['training']['tf_summary_iters'] == 0:
                grid = torchvision.utils.make_grid(outputs, nrow=4)
                logger.add_image('outputs', grid, step)

                grid = torchvision.utils.make_grid(images, nrow=4)
                logger.add_image('gt', grid, step)
            
            del outputs
            if step % config['training']['save_iters'] == 0:
                inpainting_model.save()
                
                alpha = inpainting_model.alpha
                inpainting_model.alpha = 0.0
                
                inpainting_model.generator.eval()

                print('Predicting...')
                test_loader = test_dataset.create_iterator(batch_size=1)    
                
                eval_directory = os.path.join(checkpoint, f'predictions/pred_{step}') 
                if not os.path.exists(eval_directory):
                    os.makedirs(eval_directory)
                
                # TODO batch size
                for items in test_loader:
                    images = items['image'].to(device)
                    masks = items['mask'].to(device)
                    constant_mask = items['constant_mask'].to(device)
                    outputs, _, _ = inpainting_model.forward(images, masks, constant_mask)

                    # Batch saving
                    filename = items['filename']
                    for f, result in zip(filename, outputs): 
                        result = result[:, :config['dataset']['image_height'], :config['dataset']['image_width']]
                        save_image(result, os.path.join(eval_directory, f))
                    del outputs, result, _

                mean_psnr, mean_l1, metrics = compute_metrics(eval_directory, config['path']['test']['labels'])
                logger.add_scalar('PSNR', mean_psnr, global_step=step)
                logger.add_scalar('L1', mean_l1, global_step=step)

                inpainting_model.alpha = alpha
            
            if step >= config['training']['max_iteration']:
                break

            progbar.add(len(images), values=[('iter', step), 
                                             ('loss', loss.cpu().detach().numpy())] + logs)
            del images

    # generator test
    else:
        print('\nStart testing...\n')
        #generator.test()

    logger.close()
    print('Done')
    

# ARGS
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path')
    parser.add_argument('--experiment_path', default='../experiments')
    args = parser.parse_args()
    main(args.config_path, args.experiment_path)