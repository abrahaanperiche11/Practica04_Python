#contar cuantas lineas de código tiene un archivo.py

#asegura que el nombre del archivo termine en .py
def terminacion_py(a):
    try:
        a=str(a)
        nombre=a.lower()
        assert nombre.endswith('.py')
        return a
    except:
        print('el archivo no tiene el formato apropiado')
        a=input('por favor, introduzca otra vez el nombre del archivo: ')
        return terminacion_py(a)
        

ruta_archivo=input('introduce la ruta del archivo: ')
ruta_archivo=terminacion_py(ruta_archivo)
while True:
    try: 
        with open(ruta_archivo, mode='r', encoding='utf_8') as file:
            data=file.readlines()
            break
    except:
        print('Error, la ruta es invalida')
    ruta_archivo=input('introduzca nuevamente la ruta del archivo: ')
    ruta_archivo=terminacion_py(ruta_archivo)
numero_elemento=len(data)
num_lineas=0
for i in range(numero_elemento):
    if data[i]=='\n' or data[i].startswith('#'):
        continue
    else:
        num_lineas +=1

print(f'Archivo: {ruta_archivo}, número de lineas: {num_lineas}')