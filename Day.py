from datetime import datetime, timedelta

month=["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"]
month1=["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]

def repl(a):
    b=a
    if "Jan" in b:
        return b.replace("Jan","января")
    if "Feb" in b:
        return b.replace("Feb","февраля")
    if "Mar" in b:
        return b.replace("Mar","марта")
    if "Apr" in b:
        return b.replace("Apr","апреля")
    if "May" in b:
        return b.replace("May","мая")
    if "Jun" in b:
        return b.replace("Jun","июня")
    if "Jul" in b:
        return b.replace("Jul","июля")
    if "Aug" in b:
        return b.replace("Aug","августа")
    if "Sep" in b:
        return b.replace("Sep","сентября")
    if "Oct" in b:
        return b.replace("Oct","октября")
    if "Nov" in b:
        return b.replace("Nov","ноября")
    if "Dec" in b:
        return b.replace("Dec","декабря")


def day(p):
    if 'сегодня' in p:
        pp=p.replace('сегодня',datetime.today().strftime("%d %b %Y"))
        if pp[0]=='0':
            pp=pp[1:]
        return repl(pp)
    elif 'вчера' in p:
        pp=p.replace('вчера',(datetime.now() - timedelta(days=1)).strftime("%d %b %Y"))
        if pp[0]=='0':
            pp=pp[1:]
        return repl(pp)
    else:
        return p

def m_number(b):
    if "января"==b:
        return '01'
    if "февраля"==b:
        return '02'
    if "марта"==b:
        return '03'
    if "мая"==b:
        return '04'
    if "апреля"==b:
        return '05'
    if "июня"==b:
        return '06'
    if "июля"==b:
        return '07'
    if "августа"==b:
        return '08'
    if "сентября"==b:
        return '09'
    if "октября"==b:
        return '10'
    if "ноября"==b:
        return '11'
    if "декабря"==b:
        return '12'

def count(data,tag,month):
    c=0
    for i in data:
        if i[0]==tag and i[1][5:7]==month:
            c+=1
    return c

def conv(d):
    return str(int(d[-2:]))+" "+month[int(d[5:7])-1]+" "+d[:4]+" года"