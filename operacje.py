import math

def pierwiastek(a):
    return math.sqrt(a)

def procent(a, b):
    return (a * b) / 100

def silnia(a):
    if a < 0:
        raise ValueError("Nie można obliczyć silni dla liczby ujemnej.")
    return math.factorial(a)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

def cot(a):
    cos_wartosc = cos(a)
    sin_wartosc = sin(a)
    if sin_wartosc == 0:
        raise ValueError("Cotangens nie jest zdefiniowany dla tego kąta.")
    return cos_wartosc / sin_wartosc
