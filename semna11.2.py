import os
import pickle

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_inventario()

    def agregar_producto(self, producto):
        if producto.id not in self.productos:
            self.productos[producto.id] = producto
            self.guardar_inventario()
            print("Producto agregado con éxito.")
        else:
            print("El ID del producto ya existe.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_inventario()
            print("Producto eliminado con éxito.")
        else:
            print("No se encontró el producto con el ID especificado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            self.guardar_inventario()
            print("Producto actualizado con éxito.")
        else:
            print("No se encontró el producto con el ID especificado.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con el nombre especificado.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("No hay productos en el inventario.")

    def guardar_inventario(self):
        try:
            with open("inventario.dat", "wb") as archivo:
                pickle.dump(self.productos, archivo)
        except PermissionError:
            print("No se tiene permiso para escribir en el archivo.")

    def cargar_inventario(self):
        if not os.path.exists("inventario.dat"):
            self.productos = {}
        else:
            try:
                with open("inventario.dat", "rb") as archivo:
                    self.productos = pickle.load(archivo)
            except Exception as e:
                print(f"Error al cargar inventario: {e}")

def main():
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
        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad del producto (dejar vacío para no cambiar): ")
            precio = input("Ingrese el nuevo precio del producto (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()