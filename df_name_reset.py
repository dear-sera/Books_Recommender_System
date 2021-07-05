import pandas as pd


df = pd.read_csv('crawling_data/cleaned_data.csv')
print(df.head())
df['summary'] = df['cleaned_summary']

df = df[['category', 'author', 'title', 'summary']]
print(df.info())
df.to_csv('./crawling_data/cleaned_data.csv')

