#!/urs/bin/env python2.7
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask import render_template
from suds.client import Client as SudsClient

# Ruta de WSDL
url = 'http://127.0.0.1:1337/soap/service?wsdl'

# Configuracion del Cliente
client = SudsClient(url=url, cache=None)

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def main(msg=None):
    if request.method == 'POST':
        return cargar_res(request.form)
    else:
        return cargar_page(msg)

def cargar_page(msg=None):
    if not msg:
        msg = ""
    return render_template('hello.html', res=msg)

def cargar_res(msg):
    num1 = int(msg.get('operacion')[:-1].strip())
    ope = msg.get('operacion')[-1]
    num2 = int(msg.get('valor2').strip())
    r = 0
    if ope == "+":
        r = client.service.suma(num1, num2)
    if ope == "-":
        r = client.service.resta(num1, num2)
    if ope == "*":
        r = client.service.multiplicacion(num1, num2)
    return cargar_page(r)

if __name__ == '__main__':
    app.run(host = '127.0.0.1')

