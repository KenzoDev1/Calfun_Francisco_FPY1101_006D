import csv

productos_disponibles=[]


def agregar_producto(coleccion, codigos): #1
    nombre_producto = input("Ingrese un producto --> ")
    cantidad_producto = int(input("Ingrese cantidad del producto --> "))
    precio_producto = int(input("Ingrese precio del producto --> $"))
    if 111001 in codigos[0]:
        nuevo_codigo = codigos[-1]
        nuevo_codigo = nuevo_codigo + 1
        codigos.append(nuevo_codigo)
        coleccion.append([nuevo_codigo,nombre_producto,cantidad_producto,precio_producto])
    else:
        codigos.append(111001)
        coleccion.append([111001,nombre_producto,cantidad_producto,precio_producto])
def eliminar_producto(coleccion, codigos):
        opcion_eliminar = int(input("Ingrese el codigo del producto que desea eliminar: -> "))
        rango=len(codigos)
        for i in range (rango):
            if opcion_eliminar in codigos[i]:
                coleccion.remove[i]
                codigos.remove[i]
        else:
            print("Usted ingreso un Codigo NO VALIDO.")
def guardar_archivo(coleccion):
    with open('archivo.csv','w',encoding='utf-8',newline='') as archivo_csv:
        #Declarar escritura de archivo_csv en escritor_csv
        escritor_csv = csv.writer(archivo_csv)
        #Escribir encabezado de archivo_csv
        escritor_csv.writerow(['CODIGO','NOMBRE','CANTIDAD','PRECIO'])
        #Escribir filas en archivo_csv
        escritor_csv.writerows(coleccion)
            
    