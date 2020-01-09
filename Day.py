from datetime import datetime, date, timedelta

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


def month_number(b):
    if "января"==b:
        return 1
    if "февраля"==b:
        return 2
    if "марта"==b:
        return 3
    if "мая"==b:
        return 4
    if "апреля"==b:
        return 5
    if "июня"==b:
        return 6
    if "июля"==b:
        return 7
    if "августа"==b:
        return 8
    if "сентября"==b:
        return 9
    if "октября"==b:
        return 10
    if "ноября"==b:
        return 11
    if "декабря"==b:
        return 12


def count(data,tag,month):
    c=0
    for i in data:
        if i[0]==tag and i[2]==month:
            c+=1
    return c


def controlpars(articledate,fromday,frommonth,fromyear,today,tomonth,toyear):
    if str(date(int(toyear),month_number(tomonth),int(today))-date(int(articledate[2]),month_number(articledate[1]),int(articledate[0])))[0] == '-':
        return "break"
    elif str(date(int(toyear),month_number(tomonth),int(today))-date(int(articledate[2]),month_number(articledate[1]),int(articledate[0])))[0] != '-' and str(date(int(articledate[2]),month_number(articledate[1]),int(articledate[0]))-date(int(fromyear),month_number(frommonth),int(fromday)))[0]!= '-':
        return "pass"
    else:
        return "StopIteration"
