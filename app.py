a = 1
while a == 1:
    try:
        x = 0
        while x == 0:
            opcion = int(input("ingrese alguna de las siguientes opciones para seguir\n 1.-Asignar sueldos aleatorios\n 2.-Clasificar suldos\n 3.-Ver estadísticas\n 4.-Reporte de sueldos\n 5.-Salir del programa\n> "))
            if opcion == 1:
                x = 0
            elif opcion == 2:
                X = 0
            elif opcion == 3:
                X= 0
            elif opcion == 4:
                x = 0
            elif opcion == 5:
                print("finalizando programa\nDesarrollado por: Javier Luna\nRUT: 21.873.701-3")
                x = x + 5
                a = 0
            else:
                print("por favor ingrese un numero dentro de la lista.")
    except ValueError:
        print("Por favior ingrese el tipo de dato pedido")