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
                d=((day(price[article].findAll("span", {"class": "post__time"})[0].text)).split(' '))
                date = d[:3]+[d[-1]]
                T = price[article].findAll("a", {"class": "inline-list__item-link hub-link"})
                for tag in range(len(T)):
                    t = T[tag].text
                    row = [t] + date
                    self.l.append([row[0], row[3] + '-' + m_number(row[2]) + '-' + row[1], row[4]])


    def parserandstorage(self,fromdate,todate):
        s = DataStorage()
        read = s.get_data()

        unique = []
        for i in read:
            if i[1:] not in unique:
                unique.append(i[1:])

        url = 'https://habr.com/ru/all/page'
        numbpages = 100
        self.l = []
        try:
            for i in range(1, numbpages):
                r = requests.get(url + str(i))
                soup = BeautifulSoup(r.text, 'html.parser')
                price = soup.findAll("article")
                for article in range(len(price)):
                    d = ((day(price[article].findAll("span", {"class": "post__time"})[0].text)).split(' '))
                    date = d[:3] + [d[-1]]
                    article_date = date[2] + '-' + m_number(date[1]) + '-' + date[0]
                    if article_date > todate or [article_date] + [d[-1]] in unique:
                        break
                    elif fromdate > article_date:
                        raise StopIteration
                    else:
                        T = price[article].findAll("a", {"class": "inline-list__item-link hub-link"})
                        for tag in range(len(T)):
                            t = T[tag].text
                            self.l.append([t, article_date, date[-1]])
        except StopIteration:
            pass
        data = list(map(tuple, self.l))
        d = DataStorage()
        d.add_data(data)
