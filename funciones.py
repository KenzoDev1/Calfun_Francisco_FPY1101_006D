from Menu_de_opciones import codigos
import csv
def agregar_producto(coleccion):
    global codigos #Poner el codigo 111001, el primer archivo del codigo al incio
    nombre_producto = input("Ingrese un producto --> ")
    cantidad_producto = int(input("Ingrese cantidad del producto --> "))
    precio_producto = int(input("Ingrese precio del producto --> $"))
    if 111001 in codigos:
        nuevo_codigo = codigos[-1]
        nuevo_codigo = nuevo_codigo + 1
        codigos.append(nuevo_codigo)
    else:
        codigos.append(111001)
    datos = []
    datos.append([codigo,nombre_producto,cantidad_producto,precio_producto])
    coleccion.append(datos)
    with open('productos.csv','w',encoding='utf-8') as archivo_csv:
        #Declarar escritura de archivo_csv en escritor_csv
        escritor_csv = csv.writer(archivo_csv)
        #Escribir encabezado de archivo_csv
        escritor_csv.writerow('CODIGO','NOMBRE','CANTIDAD','PRECIO')
        #Escribir filas en archivo_csv
        escritor_csv(datos)
