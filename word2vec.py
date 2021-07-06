import pandas as pd
from gensim.models import Word2Vec

df_book = pd.read_csv("./crawling_data/cleaned_data.csv", index_col=0)
print(df_book.info())

df_book.dropna(axis=0, inplace=True)
print(df_book.info())

cleaned_token_summary = list(df_book["cleaned_summary"])
print(len(cleaned_token_summary))
cleaned_tokens = []
count = 0
for summary in cleaned_token_summary:
    token = summary.split(" ")
    cleaned_tokens.append(token)
# print(len(cleaned_tokens))
# print(cleaned_token_summary[0])
# print(cleaned_tokens[0])
embedding_model = Word2Vec(
    cleaned_tokens,
    vector_size=100,
    window=4,
    min_count=20,
    workers=12,
    epochs=100,
    sg=1,
)
# vector_size: 차원 수
# windows: 앞 뒤로 고려하는 단어의 수
# workers: 사용 cpu 수
# min_count: 단어의 최소 등장 횟수

embedding_model.save("./models/word2VecModel_book.model")
# print(embedding_model.wv.vocab.keys())
# print(len(embedding_model.wv.vocab.keys())) # 단어 사전에 몇개가있는지
