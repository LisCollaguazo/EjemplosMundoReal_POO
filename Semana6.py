# Clase base: Animal
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def sonido(self):
        print("El animal hace un sonido")

# Clase derivada: Perro
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.__raza = raza  # Atributo privado

    def get_raza(self):
        return self.__raza

    def sonido(self):  # Método sobrescrito
        print("El perro ladra")

# Clase derivada: Gato
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.__color = color  # Atributo privado

    def get_color(self):
        return self.__color

    def sonido(self):  # Método sobrescrito
        print("El gato maulla")

# Ejemplo de polimorfismo
def hacer_sonido(animal: Animal):
    animal.sonido()

# Creación de objetos
perro = Perro("Fido", 3, "Golden Retriever")
gato = Gato("Whiskers", 2, "Negro")

# Uso de la función polimórfica
hacer_sonido(perro)  # Output: El perro ladra
hacer_sonido(gato)  # Output: El gato maulla

# Acceso a atributos privados a través de métodos getter
print(perro.get_nombre())  # Output: Fido
print(gato.get_edad())  # Output: 2
