import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmwrite, mmread
import pickle
from gensim.models import Word2Vec

# 데이터 불러오기
df_book = pd.read_csv("./crawling_data/cleaned_data.csv")

Tfidf_matrix = mmread("./models/tfidf_book_summary.mtx").tocsr()
with open("./models/tfidf.pickle", "rb") as f:
    Tfidf = pickle.load(f)

# 추천 함수 생성
def getRecommendation(cosine_sim):
    simScore = list(
        enumerate(cosine_sim[-1])
    )  # book_idx와 전체 martix의 cosine 유사도에 해당하는 값과 index list로 반환
    simScore = sorted(simScore, key=lambda x: x[1], reverse=True)  # 유사도의 내림차순으로 정렬
    simScore = simScore[1:11]  # 가장 유사한 상위 10개 책
    bookidx = [i[0] for i in simScore]  # 10개 책의 index
    recBookList = df_book.iloc[bookidx]
    return recBookList


# 입력한 책과 비슷한 책 찾기
book_idx = df_book[df_book["title"] == "북유럽 생활소품"].index[0]

# print(df_book.iloc[book_idx, 0])


# cosine_sim = linear_kernel(Tfidf_matrix[book_idx],
#                            Tfidf_matrix)
# # shape: (1, len(Tfidf_matrix))
# # 유사한 책 10개를 추천
# recommendation = getRecommendation(cosine_sim)
# print(recommendation)


embedding_model = Word2Vec.load("./models/word2VecModel_book.model")
key_word = "생활소품"
summary = [key_word] * 10
if key_word in embedding_model.wv.key_to_index:
    sim_word = embedding_model.wv.most_similar(key_word, topn=10)
    labels = []
    for label, _ in sim_word:
        labels.append(label)
    print(labels)
    # 가장 유사한 단어를 많이 저장
    for i, word in enumerate(labels):
        summary += [word] * (9 - i)

# 유사한 단어를 조합한 문장
summary = " ".join(summary)
print(summary)

summary_vec = Tfidf.transform([summary])
cosine_sim = linear_kernel(summary_vec, Tfidf_matrix)
recommendation = getRecommendation(cosine_sim)
print(recommendation.loc[:, ["category", "title", "author"]])
