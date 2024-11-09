# Diccionario
inventario = {}

# Menú
while True:
    print("\n---MENU---------------")
    print("\t1. VER STOCK")
    print("\t2. AGREGAR")
    print("\t3. QUITAR")
    print("\t4. SALIR")
    print("----------------------")
    
    opcion = int(input("\nSELECCIONE UNA OPCION (1-4): "))

# Ver Stock
    if opcion == 1:
        if not inventario:
            print("\n----------------------")
            print("El INVENTARIO está VACÍO.")
            print("----------------------")
        else:
            print("\n---STOCK ACTUAL---")
            for producto, cantidad in inventario.items():
                print(f"\nEl producto {producto} tiene {cantidad} unidades en Stock.")

# Agregar producto
    elif opcion == 2:
        producto = str(input("Indique el producto: ")).lower()
        cantidad = int(input(f"Indique la cantidad de {producto} a agregar: "))
        if producto in inventario:
            inventario[producto] += cantidad
        else:
            inventario[producto] = cantidad
            print("\n----------")
            print(f"El producto {producto} tiene {cantidad} unidades en Stock.")
            print("----------")

# Quitar producto
    elif opcion == 3:
        producto = str(input("Indique el producto: ")).lower()
        cantidad = int(input(f"Indique la cantidad de {producto} a agregar: "))

        if producto in inventario:
            inventario[producto] -= cantidad
        else:
            inventario[producto] = cantidad
            print("\n----------")
            print(f"\nEl prodcuto {producto} tiene {cantidad} unidades en Stock.")
            print("----------")

# Salir
    elif opcion == 4:
        print("Saliendo...")
        break

# Opción no válida
    else:
        print("\n----------")
        print("Opción NO válida.\nSelecciona un número del 1 al 4.")
        print("----------")

