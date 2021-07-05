import pandas as pd
from konlpy.tag import Okt
import re
from multiprocessing import Pool
from tqdm import tqdm


tqdm.pandas()

okt = Okt()
df = pd.read_csv('./crawling_data/raw_data_merged.csv')
print(df.head(20))
print(df.info())
stopwords = pd.read_csv('./datasets/stopwords.csv', index_col=0)
#print(stopwords)

# 또 다른 불용어 추가
book_stopwords = ['도서','작품','작가','저자',]
stopwords_list = list(stopwords.stopword) + book_stopwords

cleaned_sentences = []
for sentence in tqdm(df.summary):
    sentence = re.sub('[^가-힣 ]', '', sentence)
    token = okt.pos(sentence, stem=True)
    df_token = pd.DataFrame(token, columns=['word', 'class'])
    df_cleaned_token = df_token[
        (df_token['class'] == 'Noun') | (df_token['class'] == 'Verb') | (df_token['class'] == 'Adjective')]
    words = [word for word in df_cleaned_token['word'] if word not in stopwords_list and len(word) > 1]
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)

df['cleaned_sentences'] = cleaned_sentences
print(df.head())

print(df.info())

df = df[['title', 'cleaned_sentences', 'category', 'author']]
print(df.info())
df.to_csv('./data/cleaned_book_data.csv')