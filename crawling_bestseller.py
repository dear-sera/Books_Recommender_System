from bs4 import BeautifulSoup
import re
import time
import requests
from urllib.request import urlopen




url = 'https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we'
book_titles = []
book_authors = []
book_urls = []


for n in range(1):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('a.bo3 > b')
    authors = soup.select('a.bo3')
    urls = soup.select('a.bo3')
    imgs = soup.select('img.i_cover')

    for i in titles:
        title = i.text
        book_titles.append(title)
    for i in authors:
        author = i.parent.find_next_sibling().select_one('a:nth-child(1)').get_text()
        # author = author.text
        book_authors.append(author)
    for i in urls:
        urls = i.get('href')
        book_urls.append(urls)

    #책 이미지 크롤링
    n = 1
    for i in imgs:
        img = i['src']
        with urlopen(img) as f:
            with open('./images/bestseller' + str(n) + '.jpg', 'wb') as h:  # w - write b - binary
                img = f.read()
                h.write(img)
            n += 1
            if n > 10:
                break



