import pandas as pd

df = pd.read_csv('./users.csv')
users_list = [i for i in df['username']]

print(str(df[(df.username == users_list[0])].id.values[0]))

