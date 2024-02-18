import requests
#esta funcion permite obtener solo los precios de compra y venta
def saca_dato(list):
    lista_sunat=[]
    numero=len(list)
    for i in range(numero):
        dicc_sunat=list[i]
        dolar_compra = dicc_sunat['compra']
        dolar_venta = dicc_sunat['venta']
        list_comp_vent=[dolar_compra,dolar_venta]
        lista_sunat.append(list_comp_vent)
    return lista_sunat

# Función para insertar los datos en la base de datos SQLite
def insertar_datos(precios):
    with sqlite3.connect('base.db') as conexion:
        cursor = conexion.cursor()
        cursor.executemany("INSERT INTO usuariov4(compra, venta) VALUES (?, ?)", precios)
        conexion.commit()

import sqlite3
api_sunat = ''' 
    CREATE TABLE IF NOT EXISTS usuariov4(
        person_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        compra int,
        venta int
        );
        '''
with sqlite3.connect('base.db') as conexion:
        #creamos el cursos
        cursor = conexion.cursor()
        #creamos la tabla
        cursor.execute(api_sunat)
        #Guardar los cambios
        conexion.commit()

#iteramos meses:
for i in range(12):

    url1=f'https://api.apis.net.pe/v1/tipo-cambio-sunat?month={i+1}&year=2023'
    response1=requests.get(url1)

    # 2. Recupero la informacion como json
    if response1.status_code == 200:
        data1 = response1.json()
        precios=saca_dato(data1)
        insertar_datos(precios)


    #lectura de datos
with sqlite3.connect('base.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuariov4")
        precio = cursor.fetchall()
print(precio)
