# -*- coding: utf-8 -*-
from flask import render_template
from storage import BLOG_ENTRIES

def index_page():
    return render_template('index.html', articles=BLOG_ENTRIES)
