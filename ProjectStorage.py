import sqlite3
from Day import *

class DataStorage:

    def get_connection(self):
        conn = sqlite3.connect('mydata.db')
        cursor = conn.cursor()
        return conn, cursor

    def createbase(self,datatobase):
        conn, cursor = self.get_connection()
        cursor.execute("""CREATE TABLE IF NOT EXISTS tags (tag text, date text,time text)""");
        data = list(map(tuple, datatobase))
        cursor.executemany("INSERT INTO tags (tag, date,time) values (?, ?, ?)", data)
        conn.commit()

    def get_data(self):
        _, cursor = self.get_connection()
        result = []
        for row in cursor.execute("SELECT * FROM tags"):
            result.append(list(row))
        return result

    def add_data(self,data):
        conn, cursor = self.get_connection()
        cursor.executemany("INSERT INTO tags (tag, date, time) values (?, ?, ?)", data)
        conn.commit()

    def inform(self):
        _, cursor = self.get_connection()
        cursor.execute("SELECT max(date) FROM tags ")
        self.todate=cursor.fetchall()[0][0]
        cursor.execute("SELECT min(date) FROM tags ")
        self.fromdate=cursor.fetchall()[0][0]


    def datalimit(self,fromdate,todate):
        _, cursor = self.get_connection()
        result = []
        for row in cursor.execute("SELECT * FROM tags WHERE date BETWEEN ? AND ?",(fromdate,todate)):
            result.append(list(row))
        return result
