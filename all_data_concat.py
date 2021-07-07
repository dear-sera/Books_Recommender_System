import pandas as pd

df_author = pd.read_csv("./crawling_data/img_data.csv")
print(df_author.info())
df_book = pd.read_csv("./crawling_data/all_raw_data.csv")
print(df_book.info())

df_author.drop_duplicates("title", inplace=True)
df_book.drop_duplicates("title", inplace=True)

df_author.dropna(inplace=True)
print(df_author.info())
df_book.dropna(inplace=True)
print(df_book.info())

df = pd.merge(df_book, df_author, on=["title"], how="inner")

df.to_csv("./crawling_data/raw_data_merged.csv", index=False)

print(df.info())