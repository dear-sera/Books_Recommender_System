import pickle
import os
import pandas as pd
from scipy.io import mmwrite  # matrix 저장
from sklearn.feature_extraction.text import TfidfVectorizer

df_book = pd.read_csv("./crawling_data/cleaned_data.csv", index_col=0)
print(df_book.info())

df_book.dropna(axis=0, inplace=True)
print(df_book.info())

Tfidf = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix = Tfidf.fit_transform(df_book["cleaned_summary"])


# 폴더 생성
path = "./models/"
if not os.path.isdir(path):
    os.mkdir(path)

# 불러온 모델 저장
with open("./models/tfidf.pickle", "wb") as f:
    pickle.dump(Tfidf, f)

# 매트릭스 점수 저장
mmwrite("./models/tfidf_book_review.mtx", Tfidf_matrix)

