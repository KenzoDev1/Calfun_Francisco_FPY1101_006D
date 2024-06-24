
productos=[]



def ver_todos_productos(productos):
    print(productos)

while True:
    print("<--Menu de Opciones--->")
    print("1.-Agregar un producto.")
    print("2- Ver todos los productos.")
    print("3- Modificar un producto.")
    print("4- Eliminar un producto.")
    print("5- Guardar colección en un archivo.")
    print("6- Salir del Programa.")
    
    try :
        opcion=int(input("Ingrese una opcion: -> "));
    except ValueError:
        print("Ingrese una opcion valida del 1 al 5 ");
    
    if opcion == 1 :
        print("●Has elegido agregar un producto: ") 
    elif opcion == 2: 
        print("●Has elegido ver todos los productos");
        ver_todos_productos
    elif opcion == 3:
        print("●Has elegido modificar un producto")
    elif opcion== 4:
        print("●Has elegido eliminar un producto.")
    elif opcion == 5 :
        print("● Haz elegid guardar colección en un archivo")
    elif opcion==6:
        print("●Has elegido salir del Programa");
        break
        def resgistros():
    nombre=input("ingrese el su producto: -> ").title()
    time.sleep(0.3)
    cantidad=input("Ingrese la cantidad del producto: -> ").title()
    time.sleep(0.3)
    time.sleep(0.3)
    try:  
     precio=int(input("Ingrese ingrese el precion del producto: -> "));
     time.sleep(0.3)
    except ValueError:
     print("Ingrese caracteres validos.");
    productos={'Nombre':nombre,
                'Apellido':cantidad,
                'Sueldo':precio};
    lista_registros.append(productos);
    print(":Producto registrado exitosamente:");
    time.sleep(0.3)
def monstrar_produdtos():
   if len(lista_registros) == 0:
      print("No hay productos en el sistema")
   else:
      print("Lista de trabajadores registrados")
      for i, trabajador in enumerate(lista_registros,start=1):
         nombre = trabajador['Nombre']
         cantidad = trabajador['Apellido']
         precio= trabajador['Sueldo']
         print(f"{i}-. {nombre} {cantidad}- precio {precio}")
         time.sleep(0.3)
