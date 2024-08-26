import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = []
        self.cargar_inventario()

    def agregar_producto(self, producto):
        if not any(p.get_id() == producto.get_id() for p in self.productos):
            self.productos.append(producto)
            self.guardar_inventario()
            print("Producto agregado con éxito.")
        else:
            print("El ID del producto ya existe.")

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                self.guardar_inventario()
                print("Producto eliminado con éxito.")
                return
        print("No se encontró el producto con el ID especificado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_inventario()
                print("Producto actualizado con éxito.")
                return
        print("No se encontró el producto con el ID especificado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
        else:
            print("No se encontraron productos con el nombre especificado.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
        else:
            print("No hay productos en el inventario.")

    def guardar_inventario(self):
        try:
            with open("inventario.txt", "w") as archivo:
                for producto in self.productos:
                    archivo.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
        except PermissionError:
            print("No se tiene permiso para escribir en el archivo.")

    def cargar_inventario(self):
        if not os.path.exists("inventario.txt"):
            open("inventario.txt", "w").close()  # Crear archivo vacío si no existe
        try:
            with open("inventario.txt", "r") as archivo:
                for linea in archivo:
                    id, nombre, cantidad, precio = linea.strip().split(",")
                    producto = Producto(id, nombre, int(cantidad), float(precio))
                    self.productos.append(producto)
        except FileNotFoundError:
            print("No se encontró el archivo de inventario.")
        except Exception as e:
            print(f"Error al cargar inventario: {e}")

# Ejemplo de uso
inventario = Inventario()
while True:
    print("\nMenú de Inventario:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar todos los productos")
    print("6. Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        id = input("Ingrese el ID del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        producto = Producto(id, nombre, cantidad, precio)
        inventario.agregar_producto(producto)
    elif opcion == "2":
        id = input("Ingrese el ID del producto a eliminar: ")
        inventario.eliminar_producto(id)