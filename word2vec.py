"""
전처리(불용어처리)가 된 데이터의 책 소개를 Word2Vec으로 자연어 처리 후 embedding_model 만들어주기
"""

#모듈 불러오기
import pandas as pd
from gensim.models import Word2Vec

summary_word = pd.read_csv('crawling_data/cleaned_data.csv').fillna("")
# print(review_word.info())
cleaned_token_summary = list(summary_word['summary'])  #책 소개를 기준으로 리스트에 넣어준다
print(len(cleaned_token_summary))
# print(cleaned_token_summary)
# exit()

cleaned_tokens = [] #빈 리스트 생성

for sentence in cleaned_token_summary:
    token = sentence.split(' ')  #리스트의 담긴 문장들을 빈칸을 기준으로 띄어주기
    cleaned_tokens.append(token)  #띄어진 문장의 단어를 빈리스트에 담아서 2차원 리스트로 생성

# print(len(cleaned_tokens))
print(cleaned_token_summary[0])
print(cleaned_tokens[0])
#exit()

#워드투벡터라이징 모델 설정
#vector_size: 차원 수, windows: 앞 뒤로 고려하는 단어의 수, workers: 사용 cpu 수, min_count: 단어의 최소 등장 횟수 sg=어떤 알고리즘을 사용하느지
embedding_model = Word2Vec(cleaned_tokens, vector_size=100, window=4, min_count=20, workers=4, epochs=100, sg=1)  #2차원 리스트의 단어로
embedding_model.save('./models/word2vecModel_summary.model')  #모델 저장
print(embedding_model.wv.vocab.keys())  #단어 확인해보기
print(len(embedding_model.wv.index_to_key()))