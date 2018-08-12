# Universidad Distrital Francisco José de Caldas
## Programa enfocado en la construccion de un SOA construido en SOAP
### Gabriel Vargas Monroy

----

#### Gestion Tecnologica

#### SOAP - Calculadora - FLASK

Una calculadora construida con todos los conceptos de SOAP, basica

#### Como lo uso?

Debemos tener instalados `pip2.7` para que corra las instalaciones necesarias recuerde que **PYTHON2.7** es la aplicacion de uso debemos tenerla instalada.

Cuando tengamos instalado `pip2.7` podemos proceder a instalar todo lo necesario, archivo que está en los requerimientos, corremos el comando

```bash
pip2.7 intall -r requirements
```
EL cual es un archivo que anda en la carpeta con todos las librerias usadas, **Es posible que toque ejecutar alguno de ellos con super usuario**.

El siguiente paso para ejecutar es correr el servidor, en uno de los modulos
```bash
cd servidor
python calculadora.py
```
Este no debe haber generado error, para ver el WSDL que este dá esta bajo el link

[WDLS que se menciona, generado por el programa](http://127.0.0.1:1337/soap/service?wsdl "WSDL")

Donde podemos verificar el WSDL.

Tambien podemos ver la ejecucion del servidor.

Ahora en la carpeta anterior `cd ..`
```bash
cd cliente
python calculadora.py
```
Este ya genera la interfaz del cliente desde el cual podemos interactuar de formas mas correcta, con ello podemos ver desde el link siguiente
[PAGINA PRINCIPAL](http://127.0.0.1:5000 "Pagina Principal")
Este maneja todo lo que tiene el SOAP
