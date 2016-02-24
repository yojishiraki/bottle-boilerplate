# -*- coding:utf-8 -*-

import sys
sys.path.append('libs')

from bottle import route, post, request, template, debug

@route('/')
def index():
    return template('index')