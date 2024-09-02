class Producto:
    """
    Clase que representa un producto del inventario.
    """
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        """
        Devuelve una representación en cadena del producto.
        """
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    """
    Clase que gestiona el inventario de productos.
    """
    def __init__(self):
        self.productos = {} # Usamos un diccionario para almacenar productos por ID

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        """
        if producto.id not in self.productos:
            self.productos[producto.id] = producto
            print(f"Producto {producto.nombre} añadido al inventario.")
        else:
            print(f"Error: Ya existe un producto con el ID {producto.id}.")

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.
        """
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con ID {id} eliminado.")
        else:
            print(f"Error: No existe un producto con el ID {id}.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto.
        """
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.cantidad = cantidad
                print(f"Cantidad de {producto.nombre} actualizada a {cantidad}.")
            if precio is not None:
                producto.precio = precio
                print(f"Precio de {producto.nombre} actualizado a {precio}.")
        else:
            print(f"Error: No existe un producto con el ID {id}.")

    def buscar_producto(self, nombre):
        """
        Busca un producto por nombre.
        """
        for id, producto in self.productos.items():
            if producto.nombre == nombre:
                print(f"Producto encontrado: {producto}")
                return
        print(f"No se encontró un producto con el nombre '{nombre}'.")

    def mostrar_todos_los_productos(self):
        """
        Muestra todos los productos del inventario.
        """
        if self.productos:
            for id, producto in self.productos.items():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self, archivo):
        """
        Guarda el inventario en un archivo.
        """
        # Serialización del inventario
        with open(archivo, 'w') as f:
            for id, producto in self.productos.items():
                f.write(f"{id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
        print(f"Inventario guardado en {archivo}.")

    def cargar_inventario(self, archivo):
        """
        Carga el inventario desde un archivo.
        """
        self.productos = {} # Reinicia el inventario
        try:
            with open(archivo, 'r') as f:
                for linea in f:
                    id, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(id, nombre, int(cantidad), float(precio))
                    self.productos[id] = producto
            print(f"Inventario cargado desde {archivo}.")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {archivo}.")

# Ejemplo de uso:
def main():
    inventario = Inventario()

    # Ejemplo de creación de productos
    producto1 = Producto('1', 'Laptop', 10, 1000.00)
    producto2 = Producto('2', 'Ratón', 20, 15.00)
    producto3 = Producto('3', 'Monitor', 5, 250.00)

    # Ejemplo de uso de métodos del inventario
    inventario.añadir_producto(producto1)
    inventario.añadir_producto(producto2)
    inventario.añadir_producto(producto3)
    inventario.mostrar_todos_los_productos()

    inventario.eliminar_producto('2')
    inventario.mostrar_todos_los_productos()

    inventario.actualizar_producto('1', cantidad=15)
    inventario.actualizar_producto('3', precio=275.00)
    inventario.mostrar_todos_los_productos()

    inventario.buscar_producto('Laptop')
    inventario.buscar_producto('Teclado')

    inventario.guardar_inventario("inventario.txt") # Guardar en un archivo
    inventario.cargar_inventario("inventario.txt") # Cargar desde un archivo

    # Implementa la interfaz de usuario en la consola
    # ...
if __name__ == "__main__":
    main()