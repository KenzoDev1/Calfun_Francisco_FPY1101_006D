import csv

productos_disponibles=[]


def agregar_producto(coleccion, codigos): #1
    datos=[]
    nombre_producto = input("Ingrese un producto --> ")
    cantidad_producto = int(input("Ingrese cantidad del producto --> "))
    precio_producto = int(input("Ingrese precio del producto --> $"))
    if 111001 in codigos:
        nuevo_codigo = codigos[-1]
        nuevo_codigo = nuevo_codigo + 1
        codigos.append(nuevo_codigo)
        datos.append([nuevo_codigo,nombre_producto,cantidad_producto,precio_producto])
    else:
        codigos.append(111001)
        datos.append([111001,nombre_producto,cantidad_producto,precio_producto])
    coleccion.append(datos)

def ver_todos_productos(coleccion, ):
    for i, productos in enumerate(productos_disponibles,start=1):
        codigo = productos['Codigo']
        nombre = productos['Nombre']
        cantidad= productos['Catidad']
        precio= productos ['Precio'];
        print(f"{i} -Codigo:{codigo} - Producto {nombre} - Cantidad {cantidad} - Precio {precio}. ")
        
def eliminar_producto(productos, codigos):
        opcion_eliminar=input("Ingrese el codigo del producto que desea eliminar: -> ")
        rango=len(codigos)
        for i in range (rango):
            if opcion_eliminar in codigos[i]:
                productos.pop(i)
        else:
            print("Usted ingreso un Codigo NO VALIDO.")

def guardar_archivo(coleccion,nombre_archivo):
    with open(nombre_archivo,'w',encoding='utf-8') as archivo_csv:
        #Declarar escritura de archivo_csv en escritor_csv
        escritor_csv = csv.writer(archivo_csv)
        #Escribir encabezado de archivo_csv
        escritor_csv.writerow('CODIGO,NOMBRE,CANTIDAD,PRECIO')
        #Escribir filas en archivo_csv
        escritor_csv(coleccion)
            
    