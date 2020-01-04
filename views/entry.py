# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from storage import get_comments,add_comment

def entry_page(key):
    a = get_comments()
    if request.method=='GET':
        for article in a:
            if article['key']==key:
                return render_template('entry.html', article=article)
        return 'Такой статьи не существует'
    else:
        for i in range(len(a)):
            if a[i]['key']==key:
                add_comment(key, request.form.get('name'), request.form.get('text'))
                break
        return redirect(url_for('entry_page', key=key))