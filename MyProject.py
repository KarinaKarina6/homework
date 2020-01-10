from ProjectPlot import *
from ProjectCsv import *
from ProjectParser import *
from ProjectStorage import *
import click

@click.group()
def cli():
    pass

@cli.command()
def inform():
    try:
        d = DataStorage()
        data = d.get_data()
        d.inf(data)
        click.echo("Сейчас в базе имеются данные с {0} {1} {2} по {3} {4} {5}".format(d.minyearminmonthminday,
                                                                                      d.minyearminmonth,
                                                                                      d.minyear,
                                                                                      d.maxyearmaxmonthmaxday,
                                                                                      d.maxyearmaxmonth, d.maxyear))
    except Exception as ex:
        click.echo(ex)

@cli.command()
@click.option('--pages',default=10)
def createbd(pages):
    try:
        pars = Parser(pages)
        pars.parser()
        data = pars.l
        s = DataStorage()
        s.createbase(data)
        click.echo("База тегов успешно создана по %s последним страницам" % pages)
    except Exception as ex:
        click.echo(ex)



@cli.command()
def getdata():
    try:
        d = DataStorage()
        data = d.get_data()
        click.echo(data)
    except Exception as ex:
        click.echo(ex)


@cli.command()
@click.option('--fromday',default=0)
@click.option('--frommonth',default="0")
@click.option('--fromyear',default=0)
@click.option('--today',default=0)
@click.option('--tomonth',default="0")
@click.option('--toyear',default=0)
def parsstor(fromday,frommonth,fromyear,today,tomonth,toyear):
    try:
        if fromday != 0 and frommonth != "0" and fromyear != 0 and today != 0 and tomonth != "0" and toyear != 0:
            pars = Parser()
            pars.parserandstorage(fromday, frommonth, fromyear, today, tomonth, toyear)
            click.echo('В базу добавлены данные по тегам' + " c " + str(fromday) + " " + str(frommonth) + " " + str(
                fromyear) + " года" + " по " + str(today) + " " + str(tomonth) + " " + str(toyear) + " года")
        else:
            click.echo('Укажите границы')
    except Exception as ex:
        click.echo(ex)

@cli.command()
@click.option('--fromday',default=0)
@click.option('--frommonth',default="0")
@click.option('--fromyear',default=0)
@click.option('--today',default=0)
@click.option('--tomonth',default="0")
@click.option('--toyear',default=0)
@click.argument('count')
def plot(count,fromday,frommonth,fromyear,today,tomonth,toyear):
    try:
        d = DataStorage()
        data = d.get_data()
        if fromday != 0 and frommonth != "0" and fromyear != 0 and today != 0 and tomonth != "0" and toyear != 0:
            data = d.datalimit(data, fromday, frommonth, fromyear, today, tomonth, toyear)
        plot = Plot(data, int(count))
        plot.histogram()
        plot.limit_count()
        if fromday != 0 and frommonth != "0" and fromyear != 0 and today != 0 and tomonth != "0" and toyear != 0:
            p = plot.barchart(
                " c " + str(fromday) + " " + str(frommonth) + " " + str(fromyear) + " года" + " по " + str(
                    today) + " " + str(tomonth) + " " + str(toyear) + " года")
        else:
            p = plot.barchart()
        click.echo(p)
    except Exception as ex:
        click.echo(ex)



@cli.command()
@click.option('--fromday',default=0)
@click.option('--frommonth',default="0")
@click.option('--fromyear',default=0)
@click.option('--today',default=0)
@click.option('--tomonth',default="0")
@click.option('--toyear',default=0)
@click.option('--group', is_flag=False)
def csv(fromday,group,frommonth,fromyear,today,tomonth,toyear):
    try:
        d = DataStorage()
        data = d.get_data()
        if fromday != 0 and frommonth != "0" and fromyear != 0 and today != 0 and tomonth != "0" and toyear != 0:
            data = d.datalimit(data, fromday, frommonth, fromyear, today, tomonth, toyear)
        csv = CSV(data)
        if group:
            data = csv.group_by_month(data)
        else:
            p = Plot(data, 1)
            dict = p.histogram()
            data = csv.histogr(dict)
        if fromday != 0 and frommonth != "0" and fromyear != 0 and today != 0 and tomonth != "0" and toyear != 0:
            csv.write(data,
                      "DATA" + "c" + str(fromday) + str(frommonth) + str(fromyear) + "года" + "по" + str(today) + str(
                          tomonth) + str(toyear) + "года" + "group" + str(group) + ".csv")
        else:
            csv.write(data, "DATA" + "group" + str(group) + ".csv")
        click.echo("csv файл создан")
    except Exception as ex:
        click.echo(ex)



if __name__ == '__main__':
    cli()

