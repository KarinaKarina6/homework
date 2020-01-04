# -*- coding: utf-8 -*-

import datetime
import sqlite3

conn = sqlite3.connect("mydata.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS articles (key text, title text, text text, created_at text)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS comments (key text,name text, text text)""")



cursor.execute("""INSERT INTO articles (key,title,text,created_at) values ('some_id','It is first entry','The term normalisation comes from the database world. It refers to transforming the schema of a 
        database to remove redundant information. Also, redundant information means the same data that is stored in more 
        than one place.','23:15:35 - Dec 24 2019')""")

cursor.execute("""INSERT INTO articles (key,title,text,created_at) values ('1','It is second entry','Recommender systems are software tools and techniques providing suggestions for
items to be of use to a user. The suggestions provided by a recommender system are
aimed at supporting their users in various decision-making processes, such as what
items to buy, what music to listen, or what news to read.','23:15:35 - Dec 24 2019')""")

cursor.execute("""INSERT INTO comments (key,name,text) values ('some_id','Julius Koronci','Nice article')""")
cursor.execute("""INSERT INTO comments (key,name,text) values ('some_id','Alexander Shirokov','Thanks for good article')""")
cursor.execute("""INSERT INTO comments (key,name,text) values ('1','Francesco Ricci','This is my article!')""")
conn.commit()
l=[]

def get_connection():
    conn=sqlite3.connect('mydata.db')
    cursor=conn.cursor()
    return conn,cursor

def get_articles():
    _, cursor = get_connection()
    result=[]
    for row in cursor.execute("SELECT * FROM articles"):
        result.append({"key": row[0],"title": row[1],"text": row[2],"created_at":row[3],"comments":l})
    return result

def get_comments():
    _, cursor = get_connection()
    result=get_articles()
    for i in result:
        di=[]
        for row in cursor.execute("SELECT * FROM comments WHERE key=?",(i['key'],)):
            di.append({'name': row[1],'text': row[2]})
        i["comments"]=di
    return result

def add_article(key, title, text, created_at):
    conn, cursor = get_connection()
    cursor.execute("""INSERT INTO articles (key,title,text,created_at) values (?,?,?,?)""",(key,title,text,created_at))
    conn.commit()

def add_comment(key, name, text):
    conn, cursor = get_connection()
    cursor.execute("""INSERT INTO comments (key,name,text) values (?,?,?)""",(key,name,text))
    conn.commit()

def article_key():
    _, cursor = get_connection()
    cursor.execute("SELECT * FROM articles")
    return (cursor.fetchall())[-1][0]

