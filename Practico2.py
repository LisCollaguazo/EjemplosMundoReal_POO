import threading

def funcion_uno():
    """Función que se ejecutará en un hilo separado."""
    for i in range(10):
        print("Hilo 1: Iteración", i)

def funcion_dos():
    """Función que se ejecutará en un hilo separado."""
    for i in range(10):
        print("Hilo 2: Iteración", i)

# Crear dos hilos
hilo_1 = threading.Thread(target=funcion_uno)
hilo_2 = threading.Thread(target=funcion_dos)

# Iniciar la ejecución de los hilos
hilo_1.start()
hilo_2.start()

# Esperar a que los hilos terminen
hilo_1.join()
hilo_2.join()

print("Todos los hilos han terminado.")