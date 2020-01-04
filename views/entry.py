# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from storage import BLOG_ENTRIES

def entry_page(key):
    if request.method=='GET':
        for article in BLOG_ENTRIES:
            if article['key']==key:
                return render_template('entry.html', article=article)
        return 'Такой статьи не существует'
    else:
        for i in range(len(BLOG_ENTRIES)):
            if BLOG_ENTRIES[i]['key']==key:
                BLOG_ENTRIES[i]['comments'].append({'name':request.form.get('name'),
                                                    'text':request.form.get('text')})
                break
        return redirect(url_for('entry_page', key=key))