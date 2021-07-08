import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmwrite, mmread
import pickle
from gensim.models import Word2Vec
from konlpy.tag import Okt
import re
from tqdm import tqdm


tqdm.pandas()

okt = Okt()

df_summary_one_sentence = pd.read_csv(
    './data/cleaned_book_data.csv'
)


Tfidf_metrix = mmread('./models/tfidf_book_summary.mtx').tocsr()
with open('./models/tfidf.pickle', 'rb') as f:
    Tfidf = pickle.load(f)


def getRecommendation(cosine_sim):
    simScore = list(enumerate(cosine_sim[-1]))
    simScore = sorted(simScore, key=lambda x:x[1], reverse=True) #유사도가 가장 높은 것으로 정렬
    simScore = simScore[1:11] #자기 자신 빼고 유사도가 가장 높은 10개 추출
    movieidx = [i[0] for i in simScore]
    recMovieList = df_summary_one_sentence.iloc[movieidx] #가장 유사한 책 10개 받기
    return recMovieList


# #1) 입력한 책과 비슷한 내용의 책 추천받기
# book_idx =df_summary_one_sentence[
#     df_summary_one_sentence[
#         'title']=='황성주 박사의 생식과 건강'].index[0]
#
#
#
# #book_idx = 127
# #print(df_review_one_sentence.iloc[book_idx,1]) # 127번 책의 제목 찾기
# cosine_sim = linear_kernel(Tfidf_metrix[book_idx],
#                            Tfidf_metrix)     #코사인 유사도
# #print(list(enumerate(cosine_sim)))
# #print(list(enumerate(cosine_sim[-1])))
# recommendation = getRecommendation(cosine_sim)
# print(recommendation.iloc[:,1]) #책 제목만




#2) 키워드를 입력하고 추천받기
embedding_model = Word2Vec.load("./models/word2VecModel.model")
key_word = '완전범죄 스릴러 뷰티교실'
key_word = re.sub('[^가-힣 ]', '', key_word)
token = okt.pos(key_word, stem=True)
df_token = pd.DataFrame(token, columns=['word', 'class'])
df_cleaned_token = df_token[
    (df_token['class'] == 'Noun') | (df_token['class'] == 'Verb') | (df_token['class'] == 'Adjective')]
words = [word for word in df_cleaned_token['word'] if  len(word) > 1]
cleaned_sentence = ' '.join(words)

sentence = [cleaned_sentence] * 10
if key_word in embedding_model.wv.index_to_key:
    sim_word = embedding_model.wv.most_similar(key_word, topn=10)
    labels = []
    for label, _ in sim_word:
        labels.append(label)
    print(labels)
    for i, word in enumerate(labels):
        sentence += [word] * (9 - i)

sentence = ' '.join(sentence)
print(sentence)

#파이썬이라는 키워드를 입력했을때 추천되는 책 10개
sentence_vec = Tfidf.transform([sentence])
cosine_sim = linear_kernel(sentence_vec,
                           Tfidf_metrix)
recommendation = getRecommendation(cosine_sim)
print(recommendation.loc[:,['title','author']])