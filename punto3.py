productos = []
opcion = 100
print ("Digitar 1 para recibir nombre de un producto: ")
print ("Digitar 2 para mostrar todos los productos registrados")
print ("Digitar 3 para permitir agregar un nuevo producto a la lista de productos ")
print("Digitar 4 para permitir eliminar el ultimo producto de la lista")
print (" Digitar 0 para SALIR")

productos = []

while opcion !=0:
    opcion = int(input("Digite su opción: "))
    if opcion == 1 or opcion == 3 :
        producto = input ("digite el producto que desea registrar: ")
        productos.append(producto)
    elif opcion == 2:
        print ("pedido: ")
        for producto in productos:
            print (f"producto: {producto}")
    elif opcion == 4 :
        productos.pop()
    elif opcion == 0:
        break
    else:
        print("Estimado usuario, digite una opción valida")


