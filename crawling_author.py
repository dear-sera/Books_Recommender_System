from multiprocessing import Pool

import numpy as np
import pandas as pd
from selenium import webdriver
import book_constant

# from selenium.common.exceptions import NoSuchElementException


def crawler(cid, page_start, page_end):
    chromedriver = "./datasets/chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    # options.add_argument("--headless")
    options.add_argument("disable_gpu")
    options.add_argument("lang=ko_KR")

    driver = webdriver.Chrome(chromedriver, options=options)
    driver.implicitly_wait(10)
    titles = []
    authors = []
    saved_page = 1
    df_total = pd.DataFrame()
    for page in range(page_start, page_end + 1):
        url = f"https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=25&ViewType=Detail&PublishMonth=0&SortOrder=2&page={page}&Stockstatus=1&PublishDay=84&CID={cid}&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=&SearchOption="
        driver.get(url)
        titles_page = driver.find_elements_by_xpath(
            f'//div[@class="ss_book_box"]//*[@class="ss_book_list"]//li/a[@class="bo3"]/b'
        )
        titles_page = [title.text for title in titles_page]
        authors_page = driver.find_elements_by_xpath(
            f'//div[@class="ss_book_box"]//*[@class="ss_book_list"]//li[a[@class="bo3"]]/following-sibling::li[1]'
        )
        authors_page = [" ".join(author.text.split("|")[:-2]).strip() for author in authors_page]
        titles += titles_page
        authors += authors_page
        if (page % 50 == 0 and page != 0) or page == page_end:
            data = [(title, author) for title, author in zip(titles, authors)]
            df = pd.DataFrame(data, columns=["title", "author"])
            df["category"] = book_constant.cid_to_cat[cid]
            df_total = pd.concat([df_total, df], ignore_index=True)
            # df.to_csv(f"./crawling_data/{cid}_{saved_page}-{page}.csv", index=False)
            titles = []
            authors = []
            saved_page = page + 1

    # df_total.to_csv(f"./crawling_data/{cid}_{page_start}-{page_end}.csv", index=False)
    driver.close()
    print(len(df_total))
    return df_total


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
    df.to_csv(f"./crawling_data/author_{page_total}.csv", index=False)
