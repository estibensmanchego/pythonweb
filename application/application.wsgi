# -*- coding: utf-8 *-*

import os, sys

sys.path.append('/ruta/a/application')

def application(environ, start_response):
    output = "<b>Hola Mundo!</b>"
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    return output