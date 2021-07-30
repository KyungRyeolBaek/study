from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<item>') # => 127.0.0.1:5000 + / => 127.0.0.1:5000/
def index(item):
    apple = 'apple'
    return render_template('index.html', apple = apple, item = item)

@app.route('/main/')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)