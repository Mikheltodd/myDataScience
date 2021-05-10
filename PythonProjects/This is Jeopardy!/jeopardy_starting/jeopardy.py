import pandas as pd
pd.set_option('display.max_colwidth', -1)
data = pd.read_csv('jeopardy.csv')
print(data)