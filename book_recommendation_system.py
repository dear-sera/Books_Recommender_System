"""
도서 추천 시스템 만들기
"""

import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmwrite, mmread
import pickle
from gensim.models import Word2Vec

#데이터 불러오기
df = pd.read_csv('./crawling_data/cleaned_data.csv')


#저장해놓은 tfidf, tfidf_matrix 불러오기
Tfidf_matrix = mmread('./models/tfidf_book_summary.mtx').tocsr()
with open('./models/tfidf.pickle', 'rb') as f:
    Tfidf = pickle.load(f)

# 추천 함수 생성
def getRcommendation(cosine_sim):
    # movie_idx와 전체 martix의 cosine 유사도에 해당하는 값과 index list로 반환
    #cosine_sime = shape: (1, len(Tfidf_matrix))라서 [[~~~~]] 이런 형식
    simScore = list(enumerate(cosine_sim[-1]))  #코사인 유사도로 나온 도서들을 -1로 정렬시키고 인덱스를 주기, enumerate=인덱스가 붙는다
    simScore = sorted(simScore, key=lambda x:x[-1], reverse=True)  #코사인 유사도 값이 큰 순으로 정렬이 된다
    simScore = simScore[1:11]  #10개만 인덱싱하기, 0은 지정 도서 자체(book_idx)라서 뺀 것
    book_idx = [i[0] for i in simScore]  #10개의 도서 컴럼의 0번째인 인덱스만 가져와 book_idx 저장
    BookList = df.iloc[book_idx]  #도서들의 해당 인덱스를 원문에서 찾아서 반환하기
    return BookList

#도서 제목이 완전한 행복인 것만 찾아서 인덱싱해주기, 한 줄밖에 없지만 리스트로 오기 때문에 index[0] 해야 한다
#book_idx = df[df['title'] == '완전한 행복'].index[0]

#book_idx = 127  #임의의 숫자를 지정해서 도서를 선택해도 된다(도서 제목이 아닌)
#print(df.iloc[book_idx, 0])  #book_idx의 row에서 0번 컬럼이 title 이라서 이렇게 찍으면 도서 이름을 알 수 있다

# #코사인 유사도 확인하기
# cosine_sim = linear_kernel(Tfidf_matrix[book_idx], Tfidf_matrix)  #점수 표에서 지정시킨 도서와 전체 도서를 비교해 유사한 도서를 선택
# recommendation = getRcommendation(cosine_sim)  #유사한 도서 10개를 추천
# print(recommendation)  #추천된 도서 확인

#키워드를 입력했을 때 추천되는 영화 10건을 가져오기
embedding_model = Word2Vec.load('./models/word2vecModel_summary.model')
key_word = '할리우드'
sentence = [key_word] * 10
if key_word in embedding_model.wv.index_to_key:  #모델에 키 단어가 있다면
    sim_word = embedding_model.wv.most_similar(key_word, topn=10)  #유사단어 10개를 가져오기
    labels = []
    for label, _ in sim_word:
        labels.append(label)  #10개 단어의 이름을 가져오기
    print(labels)
    # 가장 유사한 단어를 많이 저장 ex) [겨울 겨울 겨울 가을 가을 여름]
    for i, word in enumerate(labels):
        sentence +=[word] * (9-i)  #리스트에 들어간 순대로 하나씩 단어의 개수가 적어진 상태로 나온다

# 유사한 단어를 조합한 문장
sentence = ' '.join(sentence)  #출력 단어들을 한 줄로 합치기
print(sentence)

sentence_vec = Tfidf.transform([sentence])  #단어를 tfidf에 합슥시키기
cosine_sim = linear_kernel(sentence_vec, Tfidf_matrix)  #점수표에서 해당 단어와 유사한 점수 선택

recommendataion = getRcommendation(cosine_sim)  #단어와 유사한 도서 추천
print(recommendataion[['title', 'author', 'category']].head())  #추천한 도서의 제목만 가져오기
