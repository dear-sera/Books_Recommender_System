from bs4 import BeautifulSoup
import re
import requests


class Best:
    def __init__(self):
        base_url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&BestType="
        self.url = {
            "Daily": f"{base_url}DailyBest",
            "Weekly": f"{base_url}Bestseller",
            "New Release": f"{base_url}TodayHot",
        }

        self.book_titles = []
        self.book_authors = []
        self.book_urls = []
        self.book_imgs = []
        self.flags = []

    def crawling(self, flag):
        for n in range(1):
            req = requests.get(self.url.get(flag))
            html = req.text
            soup = BeautifulSoup(html, "html.parser")
            titles = soup.select("a.bo3 > b")
            authors = soup.select("a.bo3")
            urls = soup.select("a.bo3")
            imgs = soup.select("img.i_cover")

            for i in titles:
                title = i.text
                self.book_titles.append(title)
                self.flags.append(flag)
            for i in authors:
                author = i.parent.find_next_sibling().select_one("a:nth-of-type(1)").get_text()
                # author = author.text
                self.book_authors.append(author)
            for i in urls:
                url = i.get("href")
                self.book_urls.append(url)
            for i in imgs:
                img = i.get("src")
                img = img.replace("cover150", "cover500")
                self.book_imgs.append(img)

    def get_values(self):
        return self.book_titles, self.book_authors, self.book_urls, self.book_imgs, self.flags
