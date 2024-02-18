#asegura que el número esté entre el rango y sea entero
def num_entero(a):
    try:
        numero=int(a)
        assert numero<=10 and numero>0
        return numero
    except:
        print('el dato ingresado no se encuentra en el rango')
        a=input('por favor, introduzca otra vez el tado: ')
        return num_entero(a)
#asegura que la tabla que quiera ver exista, de lo contrario muestra un mensaje de error
def exi_tabla(b):
    try:
        ruta=f'tabla-{b}.txt'
        with open(ruta, mode='r') as data:
            lectura=data.read()
        return lectura
    except:
        print('ERROR: Esta tabla no ha sido creada aún')
        b=input('Por favor, introduzca el número otra vez: ')
        b=num_entero(b)
        return exi_tabla(b)
#asegura que la tabla exista y devuelve una lista con los elementos
def exi_tabla_list(c):
    try:
        ruta=f'tabla-{c}.txt'
        with open(ruta, mode='r') as data:
            lista_tabla=data.readlines()
        return lista_tabla
    except:
        print('ERROR: Esta tabla no ha sido creada aún')
        c=input('Por favor, introduzca el número otra vez: ')
        c=num_entero(c)
        return exi_tabla_list(c)
#1.- solicitar número y crear tabla y presenta en pantalla  
numero=input('introduce un número del 1 al 10: ')
numero=num_entero(numero)
lista_multiplos=[]
for i in range(1,11):
    multiplo=f'{i}x{numero}={i*numero}\n'
    lista_multiplos.append(multiplo)

ruta_tabla=f'tabla-{numero}.txt'
with open(ruta_tabla, mode='w') as file:
    file.writelines(lista_multiplos)

#2.- Leer una tabla especifica ya creada:
numero_lec_tabla=input('introduce el número de tabla que quisiera observar (del 1 al 10): ')
numero_lec_tabla=num_entero(numero_lec_tabla)
print(exi_tabla(numero_lec_tabla))

#3.- debe leer una fila m especifica de una tabla ya creada
n=input('intruduzca la tabla que desea ver (1 a 10): ')
n=num_entero(n)
lista_tab=exi_tabla_list(n)
m=input(f'introduzca la fila de la tabla-{n} que desea ver (1 a 10): ')
m=num_entero(m)
fila=lista_tab[m-1]
print(fila)
    
    