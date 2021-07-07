import pandas as pd
from glob import glob


files = glob("./crawling_data/raw*.csv")
df = pd.DataFrame()
# 중복 및 null 제거 후 concat
print(files)
for file in files:
    df_temp = pd.read_csv(file)
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates(inplace=True)
    print(df_temp.duplicated().sum())
    df = pd.concat([df, df_temp])

print(df.info())

df.to_csv("./crawling_data/img_data.csv", index=False)
