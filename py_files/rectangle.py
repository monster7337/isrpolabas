def area(a, b):
    """
    Вычисляет площадь прямоугольника.

    Параметры:
    a (int или float): Длина прямоугольника.
    b (int или float): Ширина прямоугольника.

    Возвращаемое значение:
    float: Площадь прямоугольника.

    Исключения:
    TypeError: Если a или b не числа.
    ValueError: Если a или b <= 0.
    """
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Длина и ширина не могут быть булевыми значениями.")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Длина и ширина должны быть числами.")
    if a <= 0 or b <= 0:
        raise ValueError("Длина и ширина должны быть больше нуля.")
    return a * b


def perimeter(a, b):
    """
    Вычисляет периметр прямоугольника.

    Параметры:
    a (int или float): Длина прямоугольника.
    b (int или float): Ширина прямоугольника.

    Возвращаемое значение:
    float: Периметр прямоугольника.

    Исключения:
    TypeError: Если a или b не числа.
    ValueError: Если a или b <= 0.
    """
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Длина и ширина не могут быть булевыми значениями.")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Длина и ширина должны быть числами.")
    if a <= 0 or b <= 0:
        raise ValueError("Длина и ширина должны быть больше нуля.")
    return 2 * (a + b)
