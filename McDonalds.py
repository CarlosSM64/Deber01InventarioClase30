inventario = []

def menu_principal():
    while True:
        print("Menú Principal")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender Producto")
        print("4. Actualizar inventario")
        print("5. Salir")
        
        opcion = input("Seleccione un opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            vender_producto()
        elif opcion == "4":
            actualizar_inventario()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo, por favor")

def agregar_producto():
    
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    producto = {"nombre": nombre, "precio": precio, "stock": cantidad}

    inventario.append(producto)
    
    print(f"Producto {nombre} agregado al inventario")
    print(inventario)

def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío")
    else:
        print("Presentando Inventario")
        
        for producto in inventario:
            print(f"Nombre:{producto['nombre']}, Precio: {producto['precio']:.2f}, Stock: {producto['stock']}")
          
def vender_producto():
    nombre = input("Ingrese el nombre dentro del producto donde desea vender: ")
    
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            cantidad = int(input(f"¿Cuántas unidades de {nombre} desea vender"))
            if cantidad <= producto["stock"]:
                producto["stock"] -= cantidad
                total = cantidad * producto["precio"]
                print(f"Venda realizada. Total: ${total:.2f}")
                
                if producto["stock"] == 0:
                    print(f"El producto {nombre} se ha agotado")
                return
            else:
                print("No hay suficiente Stock en inventario")
                
    print("No se encontro producto")
    
def actualizar_inventario():    
    nombre = input("Ingrese el nombre del producto que quiere actualizar: ")
    
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nuevo_precio = input("Ingrese nuevo precio: ")
            nuevo_stock = input("Ingrese nuevo stock: ")
            
            if nuevo_nombre:
                producto["nombre"] = nuevo_nombre
            if nuevo_precio:
                producto["precio"] = float(nuevo_precio)
            if nuevo_stock:
                producto["stock"] = int(nuevo_stock)
                
            print(f"Producto {nombre} actualizado exitosamente.")
            return

        
    
menu_principal()