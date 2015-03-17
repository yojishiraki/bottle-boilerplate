# -*- coding: utf-8 -*-
 
import sys
sys.path.append('libs')

from bottle import route, static_file, default_app
from app.controllers import *

@route('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./assets/release/')
 
from bottle import run

if __name__ == '__main__':
    run(host='0.0.0.0', port=4000, debug=True, reloader=True)
else:
    # uWSGI
    application = default_app()
