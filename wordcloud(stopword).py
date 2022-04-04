import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import collections
from konlpy.tag import Okt
import matplotlib as mpl
from matplotlib import font_manager, rc

# 워드 클라우드 폰트 path
cloudfontpath = "./datasets/Jalnan.ttf"

# plt 한글 출력
font_path = "./datasets/Malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc("font", family=font)

df = pd.read_csv("./crawling_data/cleaned_data.csv", index_col=0)
df.dropna(inplace=True)
print(df.info())
print(df.head(20))

book_index = df[df["title"] == "북유럽 생활소품"].index[0]

# print(book_index)
print(df.cleaned_summary[book_index])
words = df.cleaned_summary[book_index].split(" ")
print(words)

worddict = collections.Counter(words)
worddict = dict(worddict)
print(worddict)

# wordcloud_img = WordCloud(
#     background_color="White", max_words=2000, font_path=cloudfontpath
#     ).generate_from_frequencies(worddict)
wordcloud_img = WordCloud(
    font_path=cloudfontpath,
    background_color="white",
    width=1000,
    height=1000,
    max_words=100,
    max_font_size=300,
).generate_from_frequencies(worddict)
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud_img, interpolation="bilinear")
plt.axis("off")
plt.title(df.title[book_index], size=10)
plt.show()
