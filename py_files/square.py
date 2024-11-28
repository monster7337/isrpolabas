def area(a):
    """
    Вычисляет площадь квадрата.

    Параметры:
    a (int или float): Длина стороны квадрата.

    Возвращаемое значение:
    float: Площадь квадрата.

    Исключения:
    TypeError: Если a не является числом.
    ValueError: Если a <= 0.
    """
    if isinstance(a, bool):
        raise TypeError("Сторона квадрата не может быть булевым значением.")
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона квадрата должна быть числом.")
    if a <= 0:
        raise ValueError("Сторона квадрата должна быть больше нуля.")
    return a * a


def perimeter(a):
    """
    Вычисляет периметр квадрата.

    Параметры:
    a (int или float): Длина стороны квадрата.

    Возвращаемое значение:
    float: Периметр квадрата.

    Исключения:
    TypeError: Если a не является числом.
    ValueError: Если a <= 0.
    """
    if isinstance(a, bool):
        raise TypeError("Сторона квадрата не может быть булевым значением.")
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона квадрата должна быть числом.")
    if a <= 0:
        raise ValueError("Сторона квадрата должна быть больше нуля.")
    return 4 * a
