# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
import datetime, random
from storage import add_article,article_key

def create_entry_page():
    if request.method=='GET':
        return render_template('create_entry.html')
    else:
        article={
        'key': str(random.randint(2,100)),
        'title': request.form.get('title'),
        'text': request.form.get('text'),
        'created_at': datetime.datetime.now(),
        'comments': []
        }
        add_article(article['key'], article['title'],article['text'], article['created_at'])
        k=article_key()
    return redirect(url_for('entry_page', key=k))