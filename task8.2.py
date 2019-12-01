import sqlite3
#декоратор
def commit_after_execute(param):
    def inner_decorator_sleep(func):
        def wrapper(*args,**kwargs):
            func(*args,**kwargs)
            param.commit()
        return wrapper
    return inner_decorator_sleep

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE people (user_id integer, user_name text)""")
cursor.execute("""INSERT INTO people VALUES(1, "Tina")""")

@commit_after_execute(conn)
def func(a):
    cursor.execute("""INSERT INTO people (user_id, user_name) VALUES(?, ?)""", a)

b = (2, "Alice")
func(b)
cursor.execute("""SELECT * FROM people""")
print(cursor.fetchall())