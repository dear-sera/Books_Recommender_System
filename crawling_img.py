from multiprocessing import Pool

import numpy as np
import pandas as pd
from selenium import webdriver
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

    for page in range(page_start, page_end + 1):
        url = f"https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=25&ViewType=Detail&PublishMonth=0&SortOrder=2&page={page}&Stockstatus=1&PublishDay=84&CID={cid}&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=&SearchOption="
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('a.bo3 > b')
        authors = soup.select('a.bo3')
        urls = soup.select('img.i_cover')
        #print(urls)
        for i in titles:
            title = i.text
            book_titles.append(title)
        for i in authors:
            author = i.parent.find_next_sibling().select_one('a:nth-child(1)').get_text()
            # author = author.text
            book_authors.append(author)
        for i in urls:
            urls = i.get('src')
            urls = urls.replace('/cover150/', '/cover500/')
            book_urls.append(urls)
        #return book_titles, book_authors, book_urls

        # if (page % 50 == 0 and page != 0) or page == page_end:
        #     data = [(title, author) for title, author in zip(titles, authors)]
        #     df = pd.DataFrame(data, columns=["title", "author"])
        #     df["category"] = book_constant.cid_to_cat[cid]
        #     df_total = pd.concat([df_total, df], ignore_index=True)
        #     # df.to_csv(f"./crawling_data/{cid}_{saved_page}-{page}.csv", index=False)
        #     saved_page = page + 1
        data = [(title, author, url) for title, author, url in zip(book_titles, book_authors, book_urls)]
        df = pd.DataFrame(data, columns=["title", "author", "url"])
        df_total = pd.concat([df_total, df], ignore_index=True)
        df.to_csv(f"./crawling_data/book_img.csv", index=False)

    df_total.to_csv(f"./crawling_data/{cid}_{page_start}-{page_end}.csv", index=False)

    print(len(df_total))
    return df_total


# if __name__ == "__main__":
#     cid = 1
#     dictionary = crawler(cid, 1, 2)

if __name__ == "__main__":
    processes = 8
    page_total = 400
    page_step = np.linspace(1, page_total + 1, processes + 1, dtype=int)
    inputs = []
    for cid in book_constant.cid_to_cat.keys():
        inputs += [[cid, page_step[i], page_step[i + 1] - 1] for i in range(processes)]
    print(inputs)
    pool = Pool(processes=processes)
    results = pool.starmap(crawler, inputs)
    pool.close()
    pool.join()
    df = pd.concat(results, ignore_index=True)
    df.to_csv(f"./crawling_data/book_img_total.csv", index=False)