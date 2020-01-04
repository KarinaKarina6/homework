import click
import requests

@click.group()
def cli():
    pass

address = "https://cloud-api.yandex.net:443"
headers={'Authorization': "OAuth " + 'Токен'}

#1 задание
@cli.command()
def inf():
    try:
        r = requests.get(address + '/v1/disk', headers=headers)
        if r.status_code == 200:
            res = r.json()
            click.echo('Общий объем диска: '+str(res['total_space']))
            click.echo('Используемый объем диска: '+str(res['used_space']))
        else:
            click.echo('Ошибка: '+str(r.status_code))
    except Exception as ex:
        click.echo(ex)


#2 задание
@cli.command()
@click.argument('path')
def inf_resources(path):
    try:
        r = requests.get(address + '/v1/disk/resources/', headers=headers,params={'path':path})
        if r.status_code == 200:
            res = r.json()
            if res['type'] == 'file':
                click.echo("Имя файла:"+str(['name']))
                click.echo("Размер в битах:"+str(['size']))
                click.echo("mime_type:"+str(['mime_type']))
                click.echo("Был загружен:"+str(["created"]))
            else:
                dirs = []
                files = []
                for i in res['_embedded']['items']:
                    if i['type'] == 'file':
                        files.append(i['name'])
                    else:
                        dirs.append(i['name'])
        else:
            click.echo('Ошибка: ' + str(r.status_code))
    except Exception as ex:
        click.echo(ex)

#3 задание
@cli.command()
@click.argument('path')
def download(path):
    try:
        r = requests.get(address + '/v1/disk/resources/', headers=headers,params={'path':path})
        if r.status_code == 200:
            res = r.json()
            f = open('C:/Users/lenovo/Desktop/' + res['file']['name'], "wb")
            f.write(requests.get(res['file']).content)
            f.close()
        else:
            click.echo('Ошибка: ' + str(r.status_code))
    except Exception as ex:
        click.echo(ex)

#4 задание
@cli.command()
@click.argument('path')
def create_folder(path):
    try:
        r = requests.put(address + '/v1/disk/resources', headers=headers, params={"path": path})
        if r.status_code == 201:
            click.echo('Папка создана')
        else:
            click.echo('Ошибка ' + str(r.status_code))
    except Exception as ex:
        click.echo(ex)

#5.1 задание

@cli.command()
@click.argument('path')
@click.argument('url')
def create_file1(path,url):
    params = {"url": url, "path": path + '/' + url.split('/')[-1]}
    try:
        r = requests.post(address+'/v1/disk/resources/upload',
                         headers=headers,params=params)
        if r.status_code == 202:
            click.echo('Файл загружен')
        else:
            click.echo('Ошибка ' + str(r.status_code))
    except Exception as ex:
        click.echo(ex)

#5.2 задание
def create_file2(path,url):
    try:
        file = open(url, 'rb')
        params = {"path": path + '/' + url.split('\\')[-1]}
        r = requests.get(address + '/v1/disk/resources/upload', headers=headers, params=params)
        if r.status_code == 202:
            requests.put(r.json()['href'], headers=headers, data=file)
        else:
            print('Ошибка ' + str(r.status_code))
    except Exception as ex:
        print(ex)



if __name__ == '__main__':
    cli()


