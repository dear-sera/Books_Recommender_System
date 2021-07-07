
"""

"""

#모듈 불러오기

import pandas as pd
from konlpy.tag import Okt
import re

#데이터 불러오기

df = pd.read_csv('crawling_data/raw_data_merged.csv')
print(df.head())
"""
print(df.iloc[1, 1])  #한개의 리뷰만 가져오기
print('='*70)  #비교를 위해 줄 나누기
sentence = re.sub('[^가-힣]', '', df.iloc[1, 1])  #한글만 가져오기, 내용에서 가-힣 내용이 아니면 ''빈 문자로 변경
print(sentence)


exit()
"""

okt = Okt()

#불용어가 든 파일을 가져오기
stopwords = pd.read_csv('datasets/stopwords.csv', index_col=0)
movie_stopwords = ['도서', '작가', '독자', '저자']  #불용어에 추가해 줄 단어를 리스트로 만들기
stopwords_list = list(stopwords.stopword) + movie_stopwords  #기존 불용어단어들을 리스트로 받아준다 .stopword는 컬럼이름

#csv전체 데이터의 문장을 for문으로 전처리하기

count = 0  #진행사항을 위한 변수
cleaned_summarys = []  #전처리 한 뒤 문장을 넣을 빈 리스트

for sentence in df.summary:
    count += 1
    if count % 10 == 0:  #진행사항을 보기 위해 10개의 문장마다 점찍기
        print('.', end='')
    if count % 100 == 0:  #문장 100개 당 줄바꿈해주니까 점이 10개찍히면 줄바꿈 해주는 것
        print('')
    sentence = re.sub('[^가-힣 | ' ']', '', sentence)  #sentence에서 한글과 공백을 제외하고는 ''이렇게 만들어준다
    token = okt.pos(sentence, stem=True)  #튜플리스트 반환. 단어랑 품사랑 짝지어주는, stem=단어의 원형 반환
    # 토큰을 데이터프레임으로 만들어준다, 첫번째는 단어, 두번째는 명사인지 조사인지 등에 대한 클래스
    df_token = pd.DataFrame(token, columns=['word', 'class'])
    # 데이터프레임안에서 조건식으로 인덱싱 가능하다(클래스가 명사, 동사, 형용사인 것만 뽑는 것)
    df_cleaned_token = df_token[(df_token['class'] == 'Noun') | (df_token['class'] == 'Verb') | (df_token['class'] == 'Adjective')]
    words = []
    for word in df_cleaned_token['word']:  #단어를 기준으로 for문을 돌리기
        if len(word) > 1:   #한 단어는 제외한다
            if word not in stopwords_list:  #불용어 리스트에 없는 단어는 빈리스트에 추가하기
                words.append(word)
    # for문까지 끝낸 단어들을 다시 하나의 문장으로 합쳐주기
    cleaned_summary = ' '.join(words)
    cleaned_summarys.append(cleaned_summary)

#컬럼 만들어서 전처리 문장 넣기
df['summary'] = cleaned_summarys
print(df.head())

print(df.info())

#새 데이터프레임 만들어 저장하기
df = df[['category', 'title', 'author', 'summary', 'url']]
print(df.info())
df.to_csv('./crawling_data/cleaned_data.csv')