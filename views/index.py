# -*- coding: utf-8 -*-
from flask import render_template
from storage import get_comments

def index_page():
    return render_template('index.html', articles=get_comments())
