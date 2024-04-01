from typing import Union

def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    resultado= None
    if multiplicar:
        resultado = a*b
    elif b == 0:
        resultado = "Operación no válida"
    else :
        resultado = a/b

    return resultado

    

assert operacion_basica(1, 1, True) == 1
assert operacion_basica(1, 1, False) == 1
assert operacion_basica(25, 5, True) == 125
assert operacion_basica(25, 5, False) == 5
assert operacion_basica(0, 5, True) == 0
assert operacion_basica(0, 5, False) == 0
assert operacion_basica(1, 0, True) == 0
assert operacion_basica(1, 0, False) == "Operación no válida"

##################################################################################

def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:

    if multiplicar:
        return a*b
    elif b == 0:
        return 'Operación no válida'
    else:
        return a/b

assert operacion_basica(1, 1, True) == 1
assert operacion_basica(1, 1, False) == 1
assert operacion_basica(25, 5, True) == 125
assert operacion_basica(25, 5, False) == 5
assert operacion_basica(0, 5, True) == 0
assert operacion_basica(0, 5, False) == 0
assert operacion_basica(1, 0, True) == 0
assert operacion_basica(1, 0, False) == "Operación no válida"