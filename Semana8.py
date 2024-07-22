import os
import subprocess


# Función para mostrar el código de un script
def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


# Función para ejecutar un script
def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


# Función para mostrar el menú principal
def mostrar_menu(opciones, unidades):
    print("\n** Menú Principal **")
    print("____________________")
    for key, value in opciones.items():
        print(f"{key} - {value}")
    for key, value in unidades.items():
        print(f"{key} - {value}")
    print("0 - Salir")
    eleccion = input("Elige un script para ver su código o '0' para salir: ")
    if eleccion == '0':
        print("Saliendo del programa.")
        return
    elif eleccion in opciones:
        ruta_script = os.path.join(ruta_base, opciones[eleccion])
        mostrar_codigo(ruta_script)
    elif eleccion in unidades:
        mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion]))
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")


# Función para mostrar el submenú
def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
    print("\n** Submenú **")
    print("____________")
    for i, carpeta in enumerate(sub_carpetas, start=1):
        print(f"{i} - {carpeta}")
    print("0 - Regresar al menú principal")
    eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
    if eleccion_carpeta == '0':
        return
    else:
        try:
            eleccion_carpeta = int(eleccion_carpeta) - 1
            if 0 <= eleccion_carpeta < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
        except ValueError:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Función para mostrar los scripts
def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]
    print("\n** Scripts **")
    print("__________")
    for i, script in enumerate(scripts, start=1):
        print(f"{i} - {script}")
    print("0 - Regresar al submenú anterior")
    print("9 - Regresar al menú principal")
    eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
    if eleccion_script == '0':
        return
    elif eleccion_script == '9':

