from ProjectPlot import *
from ProjectCsv import *
from ProjectParser import *
from ProjectStorage import *
from pr import *
import click

@click.group()
def cli():
    pass

@cli.command()
def inform():
    try:
        d = DataStorage()
        d.inform()
        click.echo("Сейчас в базе имеются данные с {0} по {1}".format(conv(d.fromdate),conv(d.todate)))
    except Exception as ex:
        click.echo(ex)

@cli.command()
@click.option('--pages',default=10,help='Количество страниц, которое надо отпарсить')
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
@click.option('--fromdate',default="0",help='С какой даты парсить статьи. Формат ввода YYYY-MM-DD')
@click.option('--todate',default="0",help='По какую дату парсить статьи. Формат ввода YYYY-MM-DD')
def parsstor(fromdate, todate):
    try:
        form(fromdate)
        form(todate)
        pars = Parser()
        pars.parserandstorage(fromdate, todate)
        click.echo('В базу добавлены данные по тегам' + " c " + conv(fromdate) + " по " + conv(todate))
    except ValueError:
        click.echo('Введите даты в правильном формате YYYY-MM-DD')
    except Exception as ex:
        click.echo(ex)


@cli.command()
@click.option('--fromdate',default="0",help='С какой даты учитывать данные для гистограммы. Формат ввода YYYY-MM-DD')
@click.option('--todate',default="0",help='По какую дату учитывать данные для гистограммы. Формат ввода YYYY-MM-DD')
@click.argument('count')
def plot(count,fromdate,todate):
    try:
        form(fromdate)
        form(todate)
        d = DataStorage()
        if fromdate != "0" and todate != "0":
            data = d.datalimit(fromdate, todate)
        else:
            data=d.get_data()
        plot = Plot(data, int(count))
        plot.histogram()
        plot.limit_count()
        if fromdate != "0" and todate != "0":
            p = plot.barchart(" c " + conv(fromdate) + " по " + conv(todate))
        else:
            p = plot.barchart()
        click.echo(p)
    except ValueError:
        click.echo('Введите даты в правильном формате YYYY-MM-DD')
    except Exception as ex:
        click.echo(ex)



@cli.command()
@click.option('--fromdate',default="0",help='С какой даты учитывать данные для загрузки в csv файл. Формат ввода YYYY-MM-DD')
@click.option('--todate',default="0",help='По какую дату учитывать данные для загрузки в csv файл. Формат ввода YYYY-MM-DD')
@click.option('--group', is_flag=False,help='Группировать ли данные. Формат ввода True/False')
def csv(group,fromdate,todate):
    try:
        form(fromdate)
        form(todate)
        d = DataStorage()
        data = d.get_data()
        if fromdate != "0" and todate != "0":
            data = d.datalimit(fromdate, todate)
        csv = CSV(data)
        if group:
            data = csv.group_by_month(data)
        else:
            p = Plot(data, 1)
            dict = p.histogram()
            data = csv.histogr(dict)
        if fromdate != "0" and todate != "0":
            csv.write(data,
                      "DATA" + "c" + str(fromdate) + "по" + str(todate) + "group" + str(group) + ".csv")
        else:
            csv.write(data, "DATA" + "group" + str(group) + ".csv")
        click.echo("csv файл создан")
    except ValueError:
        click.echo('Введите даты в правильном формате YYYY-MM-DD')
    except Exception as ex:
        click.echo(ex)



if __name__ == '__main__':
    cli()
