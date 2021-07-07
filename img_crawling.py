from multiprocessing import Pool

import numpy as np
import pandas as pd
import book_constant
from bs4 import BeautifulSoup
import urllib.request
import requests
# from selenium.common.exceptions import NoSuchElementException


def crawler(cid, page_start, page_end):
    base_url = 'https://www.aladin.co.kr/home/welcome.aspx'

    book_titles = []
    book_authors = []
    book_urls = []
    df_total = pd.DataFrame()
    print('debug1')
    for page in range(page_start, page_end + 1):
        print('page : ', page)
        url = f"https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=25&ViewType=Detail&PublishMonth=0&SortOrder=2&page={page}&Stockstatus=1&PublishDay=84&CID={cid}&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=&SearchOption="
        try:
            req = requests.get(url)
        except:
            print('error :' ,url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('a.bo3 > b')
        authors = soup.select('a.bo3')
        urls = soup.select('img.i_cover')
        #print(urls)
        print('titles len ', len(titles))
        for i in titles:
            title = i.text
            book_titles.append(title)
        print('book_titles len :', len(book_titles))
        for i in authors:
            author = i.parent.find_next_sibling().select_one('a:nth-child(1)').get_text()
            # author = author.text
            book_authors.append(author)
        for i in urls:
            urls = i.get('src')
            urls = urls.replace('/cover150/', '/cover500/')
            book_urls.append(urls)
        #return book_titles, book_authors, book_urls
        saved_page = 1
        print('len : ', len(df_total))

    data = [(title, author, url) for title, author, url in zip(book_titles, book_authors, book_urls)]
    df = pd.DataFrame(data, columns=["title", "author", "url"])
    df_total = pd.concat([df_total, df], ignore_index=True)

    df_total.to_csv(f"./crawling_data/img_{cid}_{page_start}-{page_end}.csv", index=False)
    return






if __name__ == "__main__":
    processes = 8
    page_total = 400
    page_step = np.linspace(1, page_total + 1, processes + 1, dtype=int)
    print(page_step)

    inputs = []
    for cid in book_constant.cid_to_cat.keys():
        inputs += [[cid, page_step[i], page_step[i + 1] - 1] for i in range(processes)]
    print(inputs)

    pool = Pool(processes=processes)
    results = pool.starmap(crawler, inputs)
    print(len(results))
    exit()
    pool.close()
    pool.join()
    df = pd.concat(results, ignore_index=True)