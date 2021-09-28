import pandas as pd

df_author = pd.read_csv("./crawling_data/author_400.csv")
df_book = pd.read_csv("./crawling_data/all_raw_data.csv")

df_author.drop_duplicates("title", inplace=True)
df_book.drop_duplicates("title", inplace=True)

df_author.dropna(inplace=True)
df_book.dropna(inplace=True)

df = pd.merge(df_book, df_author, on=["title", "category"], how="inner")

df.to_csv("./crawling_data/raw_data_merged.csv", index=False)
