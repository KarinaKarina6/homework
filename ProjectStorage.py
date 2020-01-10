import sqlite3
from Day import *

class DataStorage:

    def get_connection(self):
        conn = sqlite3.connect('mydata.db')
        cursor = conn.cursor()
        return conn, cursor

    def createbase(self,datatobase):
        conn, cursor = self.get_connection()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tags (tag text, day text, month text, year text)""");
        data = list(map(tuple, datatobase))
        cursor.executemany("INSERT INTO tags (tag, day, month, year) values (?, ?, ?, ?)", data)
        conn.commit()

    def get_data(self):
        _, cursor = self.get_connection()
        result = []
        for row in cursor.execute("SELECT * FROM tags"):
            result.append(list(row))
        return result

    def add_data(self,data):
        conn, cursor = self.get_connection()
        cursor.executemany("INSERT INTO tags (tag, day, month, year) values (?, ?, ?, ?)", data)
        conn.commit()

    def inf(self,data):
        l1 = set()
        for i in data:
            l1.add(int(i[3]))
        self.minyear = str(sorted(l1)[0])
        self.maxyear = str(sorted(l1)[-1])

        l21 = set()
        for i in data:
            if str(self.minyear) in i:
                l21.add(i[2])
        self.minyearminmonth = str(sorted(l21)[0])

        l22 = set()
        for i in data:
            if str(self.maxyear) in i:
                l22.add(i[2])
        self.maxyearmaxmonth = str(sorted(l22)[-1])

        l31 = set()
        for i in data:
            if str(self.minyear) in i:
                if self.minyearminmonth in i:
                    l31.add(int(i[1]))
        self.minyearminmonthminday = str(sorted(l31)[0])

        l32 = set()
        for i in data:
            if str(self.maxyear) in i:
                if self.maxyearmaxmonth in i:
                    l32.add(int(i[1]))
        self.maxyearmaxmonthmaxday = str(sorted(l32)[-1])


    def datalimit(self,data,fromday,frommonth,fromyear,today,tomonth,toyear):
        list = []
        for i in data:
            if int(fromyear) <= int(i[3]) <= int(toyear) and month_number(frommonth) <= month_number(i[2]) <= month_number(
                    tomonth) and int(fromday) <= int(i[1]) <= int(today):
                list.append(i)
        return list

    def stoppars(self,r,articledate):
        list = []
        for row in r:
            list.append(row[1:])

        unique = []
        for i in list:
            if i not in unique:
                unique.append(i)
        return articledate in unique


