def area(a, h):
    """
    Вычисляет площадь треугольника.

    Параметры:
    a (int или float): Основание треугольника.
    h (int или float): Высота треугольника.

    Возвращаемое значение:
    float: Площадь треугольника.

    Исключения:
    TypeError: Если a или h не являются числами.
    ValueError: Если a <= 0 или h <= 0.
    """
    if isinstance(a, bool) or isinstance(h, bool):
        raise TypeError("Основание и высота треугольника не могут быть булевыми значениями.")
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Основание и высота треугольника должны быть числами.")
    if a <= 0 or h <= 0:
        raise ValueError("Основание и высота треугольника должны быть больше нуля.")
    return a * h / 2


def perimeter(a, b, c):
    """
    Вычисляет периметр треугольника.

    Параметры:
    a (int или float): Первая сторона треугольника.
    b (int или float): Вторая сторона треугольника.
    c (int или float): Третья сторона треугольника.

    Возвращаемое значение:
    float: Периметр треугольника.

    Исключения:
    TypeError: Если a, b или c не являются числами.
    ValueError: Если a, b или c <= 0 или не выполняется неравенство треугольника.
    """
    if any(isinstance(x, bool) for x in (a, b, c)):
        raise TypeError("Стороны треугольника не могут быть булевыми значениями.")
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError("Стороны треугольника должны быть числами.")
    if any(x <= 0 for x in (a, b, c)):
        raise ValueError("Стороны треугольника должны быть больше нуля.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Стороны треугольника должны удовлетворять неравенству треугольника.")
    return a + b + c
