import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
from konlpy.tag import Okt
import matplotlib as mpl
from matplotlib import font_manager, rc

# import matplotlib as mpl
# import matplotlib.font_manager as fm
# fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
# font = fm.FontProperties(fname=fontpath, size=9)
# plt.rc('font', family='NanumBarunGothic')
# mpl.font_manager._rebuild()

fontpath = './datasets/malgun.ttf'
font_name = font_manager.FontProperties(fname=fontpath).get_name()
rc('font', family=font_name)
mpl.font_manager._rebuild()
df = pd.read_csv('./crawling_data/raw_data_merged.csv')
df.dropna(inplace=True)
#print(df.info())

print(df.head(20))
print(df.info())

book_index = df[df['title'] == '황성주 박사의 생식과 건강'].index[0]
print(book_index)
print(df.summary[book_index])
words = df.summary[book_index].split(' ')
print(words)

worddict = collections.Counter(words)
worddict = dict(worddict)
print(worddict)
stopwords = ['도서','작품','작가','저자',]
wordcloud_img = WordCloud(
    background_color='white', max_words=2000,
    font_path=fontpath,
    stopwords=stopwords
    ).generate(df.summary[book_index])
# wordcloud_img = WordCloud(
#     background_color='white', max_words=2000,
#     font_path=fontpath
#     ).generate_from_frequencies(worddict)
plt.figure(figsize=(8,8))
plt.imshow(wordcloud_img, interpolation='bilinear')
plt.axis('off')
plt.title(df.title[book_index], size=25)
plt.show()