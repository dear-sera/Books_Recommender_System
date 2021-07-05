from multiprocessing import Pool

import numpy as np
import pandas as pd
from selenium import webdriver


def get_book(cids, list_start, list_end):

    chromedriver = "./datasets/chromedriver.exe"
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")

    driver = webdriver.Chrome(chromedriver, options=options)
    driver.implicitly_wait(10)

    for cid in cids:
        df_total = pd.DataFrame(columns=["title", "author"])
        titles = []
        authors = []
        for page in range(list_start, list_end + 1):
            url = f"https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=25&ViewType=Detail&PublishMonth=0&SortOrder=2&page={page}&Stockstatus=1&PublishDay=84&CID={cid}&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=&SearchOption="
            driver.get(url)
            for i in range(1, 26):
                title = driver.find_elements_by_xpath(
                    f'//*[@id="Myform"]/div[2]/div[{i}]/table/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/div[1]/ul/li[2]/a[1]'
                ).text

                author = driver.find_elements_by_xpath(
                    f'//*[@id="Myform"]/div[2]/div[{i}]/table/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/div[1]/ul/li[3]/a[1]'
                ).text

                titles.append(title)
                authors.append(author)

        df_titles = pd.DataFrame(titles)
        df_authors = pd.DataFrame(authors)
        df_total = pd.concat([df_titles, df_authors], axis=0, ignore_index=True)
        df_total.to_csv(f"./crawling_data/title_author_{cid}.csv", index=False)

    driver.close()


if __name__ == "__main__":
    processes = 8
    page_total = 400
    cids = [1, 170, 987, 1237, 76001, 1230, 55890, 517, 74, 336, 1196, 55889, 656]
    page_step = np.linspace(1, page_total + 1, processes + 1, dtype=int)
    inputs = [[cids, page_step[i], page_step[i + 1] - 1] for i in range(processes)]
    print(inputs)
    pool = Pool(processes=processes)
    results = pool.starmap(get_book, inputs)
    pool.close()
    pool.join()
