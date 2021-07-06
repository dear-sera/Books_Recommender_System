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
        #author = author.text
        book_authors.append(author)
    for i in urls:
        urls = i.get('href')
        book_urls.append(urls)



for i in range(len(book_titles)) :
    print('책 제목:' , book_titles[i])
    print('지은이:' , book_authors[i])
    print('url :', book_urls[i])
    print('-----------------------------------')

print(len(book_titles), len(book_authors), len(book_urls))



