import datetime


def form(date):
    try:
        l = date.split("-")
        year=int(l[0])
        month=int(l[1])
        day=int(l[2])
        datetime.date(year,month,day)
    except:
        raise ValueError
