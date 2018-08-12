#!/urs/bin/env python2.7
# -*- coding: utf-8 -*-

from flask import Flask
from flask_spyne import Spyne
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable

app = Flask(__name__)
spyne = Spyne(app)

# Todos los Servicios
class SomeSoapService(spyne.Service):
    __service_url_path__ = '/soap/service'
    __in_protocol__ = Soap11(validator = 'lxml')
    __out_protocol__ = Soap11()

    @spyne.srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def echo(str, cnt):
        for i in range(cnt):
            yield str

    @spyne.srpc(Integer, Integer, _returns=Integer)
    def suma(a, b):
        return a+b

    @spyne.srpc(Integer, Integer, _returns=Integer)
    def resta(a, b):
        return a-b

    @spyne.srpc(Integer, Integer, _returns=Integer)
    def mltiplicacion(a, b):
        return a*b

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 1337)
