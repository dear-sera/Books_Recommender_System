# 모듈 불러오기
import pandas as pd
from konlpy.tag import Okt
import re
from tqdm import tqdm

tqdm.pandas()

# 데이터 불러오기

df = pd.read_csv("./crawling_data/raw_data_merged.csv")
okt = Okt()

# Drop NA
df.dropna(axis=0, inplace=True)
df.info()

# Stopwords
stopwords = pd.read_csv("./datasets/stopwords.csv", index_col=0)
book_stopwords = ["도서", "작품", "작가", "저자"]
stopwords_set = set(list(stopwords.stopword) + book_stopwords)


# preprocessing
count = 0
cleaned_sentences = []


okt = Okt()
cleaned_sentences = []
for sentence in tqdm(df.summary):
    sentence = re.sub("[^가-힣 ]", "", sentence)
    token = okt.pos(sentence, stem=True)  # 단어의 원형 반환
    df_token = pd.DataFrame(token, columns=["word", "class"])
    df_cleaned_token = df_token[
        (df_token["class"] == "Noun")
        | (df_token["class"] == "Verb")
        | (df_token["class"] == "Adjective")
    ]
    words = [
        word
        for word in df_cleaned_token["word"]
        if word not in stopwords_set and len(word) > 1
    ]
    cleaned_sentence = " ".join(words)
    cleaned_sentences.append(cleaned_sentence)

df["cleaned_summary"] = cleaned_sentences


# Save
df = df[["category", "title", "author", "cleaned_summary"]]
print(df.info())
df.to_csv("./crawling_data/cleaned_data.csv")

