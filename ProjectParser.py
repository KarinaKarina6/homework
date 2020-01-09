#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from ProjectStorage import *


class Parser:
    def __init__(self,numbpages=10):
        self.l = []
        self.numbpages=numbpages

    def parser(self):
        url = 'https://habr.com/ru/all/page'
        for i in range(1, self.numbpages):
            r = requests.get(url + str(i))
            soup = BeautifulSoup(r.text, 'html.parser')
            price = soup.findAll("article")
            for article in range(len(price)):
                data = ((day(price[article].findAll("span", {"class": "post__time"})[0].text)).split(' '))[:3]
                T = price[article].findAll("a", {"class": "inline-list__item-link hub-link"})
                for tag in range(len(T)):
                    t = T[tag].text
                    self.l.append([t] + data)

    def parserandstorage(self,fromday,frommonth,fromyear,today,tomonth,toyear):
        url = 'https://habr.com/ru/all/page'
        numbpages = 100
        self.l = []
        try:
            for i in range(1, numbpages):
                r = requests.get(url + str(i))
                soup = BeautifulSoup(r.text, 'html.parser')
                price = soup.findAll("article")
                for article in range(len(price)):
                    date = ((day(price[article].findAll("span", {"class": "post__time"})[0].text)).split(' '))[:3]
                    if controlpars(date, fromday, frommonth, fromyear, today, tomonth, toyear) == "break":
                        break
                    elif controlpars(date, fromday, frommonth, fromyear, today, tomonth, toyear) == "StopIteration":
                        raise StopIteration
                    else:
                        T = price[article].findAll("a", {"class": "inline-list__item-link hub-link"})
                        for tag in range(len(T)):
                            t = T[tag].text
                            self.l.append([t] + date)
        except StopIteration:
            pass
        data = list(map(tuple, self.l))
        d = DataStorage()
        d.add_data(data)


def inform():
    d = DataStorage()
    data = d.get_data()
    d.inf(data)
    print("Сейчас в базе имеются данные с {0} {1} {2} по {3} {4} {5}".format(d.minyearminmonthminday,
                                                                                  d.minyearminmonth,
                                                                                  d.minyear, d.maxyearmaxmonthmaxday,
                                                                                  d.maxyearmaxmonth, d.maxyear))
