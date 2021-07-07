from bs4 import BeautifulSoup
import re
import time
import requests



def bestseller():
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


    return  book_titles, book_authors, book_urls


# print("2번째 작가:", bestseller()[1][1])
#
BS = bestseller()
bs_titles = [BS[0][i] for i in range(10)]
print(bs_titles[0])
