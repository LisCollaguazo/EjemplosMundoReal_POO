def calculate_area(base: int, height: float) -> float:
    """
    Calcula el área de un triángulo.

    Args:
        base (int): La base del triángulo.
        height (float): La altura del triángulo.

    Returns:
        float: El área del triángulo.
    """
    return 0.5 * base * height

def calculate_circle_area(radius: float) -> float:
    """
    Calcula el área de un círculo.

    Args:
        radius (float): El radio del círculo.

    Returns:
        float: El área del círculo.
    """
    return 3.14159 * radius ** 2

def calculate_rectangle_area(length: int, width: int) -> int:
    """
    Calcula el área de un rectángulo.

    Args:
        length (int): La longitud del rectángulo.
        width (int): El ancho del rectángulo.

    Returns:
        int: El área del rectángulo.
    """
    return length * width

# Ejemplos de uso
base = 5  # int
height = 6.0  # float
area_triangle = calculate_area(base, height)
print(f"El área del triángulo es: {area_triangle:.2f}")

radius = 4.0  # float
area_circle = calculate_circle_area(radius)
print(f"El área del círculo es: {area_circle:.2f}")

length = 3  # int
width = 4  # int
area_rectangle = calculate_rectangle_area(length, width)
print(f"El área del rectángulo es: {area_rectangle}")

# Ejemplo de uso con string
figure_type = "triángulo"  # string
if figure_type == "triángulo":
    base = 5  # int
    height = 6.0  # float
    area = calculate_area(base, height)
    print(f"El área del {figure_type} es: {area:.2f}")
else:
    print("No se puede calcular el área de esa figura.")

# Ejemplo de uso con boolean
is_square = True  # boolean
if is_square:
    side = 5  # int
    area = side ** 2
    print(f"El área del cuadrado es: {area}")
else:
    print("No se puede calcular el área de esa figura.")