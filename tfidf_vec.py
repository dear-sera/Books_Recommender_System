import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle

df_summary_one_sentence = pd.read_csv(
    './data/cleaned_book_data.csv', index_col=0)

print(df_summary_one_sentence.info())

Tfidf = TfidfVectorizer()
Tfidf_matrix = Tfidf.fit_transform(df_summary_one_sentence['cleaned_sentences']) #모든문장의 tfidf점수를 받아서 매트릭스를 만들어줌


with open('./models/tfidf.pickle', 'wb') as f:
    pickle.dump(Tfidf, f) #tfidf 저장

mmwrite('./models/tfidf_book_summary.mtx', Tfidf_matrix) #tfidf metrix 저장