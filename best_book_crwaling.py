import numpy as np
import pandas as pd
from selenium import webdriver
from multiprocessing import Pool

# df = pd.read_csv('./crawling_data/new_book_data.csv')
# df = df.loc[0:49]
# df.to_csv("./crawling_data/new_book_data.csv", index=False)
# print(df.info())
# print(df.head())
# exit()

def crawler(page_start, page_end):
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
    names = ['DailyBest', 'Bestseller', 'TodayHot']
    for name in names:
        url = f'https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&BestType={name}'
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
        data = [(title, author) for title, author in zip(titles, authors)]
        df = pd.DataFrame(data, columns=["title", "author"])
        # df_total = pd.concat([df_total, df], ignore_index=True)
        names = ['DailyBest', 'Bestseller', 'TodayHot']
        df.to_csv(f"./crawling_data/{name}_book_data.csv", index=False)
        titles = []
        authors = []

    driver.close()


if __name__ == "__main__":
    dictionary = crawler(1, 2)
