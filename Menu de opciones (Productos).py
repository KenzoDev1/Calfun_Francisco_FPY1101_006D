from funciones import agregar_producto, guardar_archivo, eliminar_producto

coleccion=[]
codigos=[]

while True:
    print("<--Menu de Opciones--->")
    print("1.-Agregar un producto.")
    print("2- Ver todos los productos.")
    print("3- Modificar un producto.")
    print("4- Eliminar un producto.")
    print("5- Guardar coleccion en un archivo.")
    print("6- Salir del Programa.")
    
    try :
        opcion=int(input("Ingrese una opcion: -> "));
    except ValueError:
        print("Ingrese una opcion valida del 1 al 5 ");
    if opcion == 1 :
        print("●Has elegido agregar un producto: ") 
        agregar_producto(coleccion, codigos)
        print(codigos, coleccion)
    elif opcion == 2: 
        print("●Has elegido ver todos los productos");
    elif opcion == 3:
        print("●Has elegido modificar un producto")
    elif opcion== 4:
        print("●Has elegido eliminar un producto.")
        eliminar_producto(coleccion, codigos)
    elif opcion == 5 :
        print("● Haz elegido guardar colección en un archivo")
        guardar_archivo(coleccion)
    elif opcion==6:
        print("●Has elegido salir del Programa");
        exit()
        
        
