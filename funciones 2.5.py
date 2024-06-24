import csv

productos_disponibles=[]



def ver_todos_productos(productos):
    for i, productos in enumerate(productos_disponibles,start=1):
        codigo = productos['Codigo']
        nombre = productos['Nombre']
        cantidad= productos['Catidad']
        precio= productos ['Precio'];
        print(f"{i} -Codigo:{codigo} - Producto {nombre} - Cantidad {cantidad} - Precio {precio}. ")
        
def agregar_producto(productos):
    global codigo #Poner el codigo 111001, el primer archivo del codigo al incio
    nombre_producto = input("Ingrese un producto --> ")
    cantidad_producto = int(input("Ingrese cantidad del producto --> "))
    precio_producto = int(input("Ingrese precio del producto --> "))
    datos = []
    codigos = []
    productos={'Codigo':codigos,
                'Nombre':nombre_producto,
               'Cantidad':cantidad_producto,
               'Precio':precio_producto}
    datos.append([codigo,nombre_producto,cantidad_producto,precio_producto])
    datos.append(productos)
    
    with open('productos.csv','w',encoding='utf-8') as archivo_csv:
        #Declarar escritura de archivo_csv en escritor_csv
        escritor_csv = csv.writer(archivo_csv)
        #Escribir encabezado de archivo_csv
        escritor_csv.writerow('CODIGO','NOMBRE','CANTIDAD','PRECIO')
        #Escribir filas en archivo_csv
        escritor_csv(datos)


    
    
def eliminar_producto(productos):
        opcion_eliminar=input("Ingrese el codigo del producto que desea eliminar: -> ")
        if opcion_eliminar==productos:
            productos.remove(opcion_eliminar)
        else:
            print("Usted ingreso un Codigo NO VALIDO.")


def guardar_archivo(coleccion,nombre_archivo):
#PERMISOS DE LA ESCRITURA
    archivo = open('productos.txt', 'r’)
    contenido = archivo.read()
    print(contenido)
    archivo.close()
    with open('datos.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
            
    