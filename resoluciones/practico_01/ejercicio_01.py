def maximo_basico(a: float, b: float) -> float:
    if a > b:
        return a
    else:
        return b

assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18


def maximo_libreria(a: float, b: float) -> float:
  return max(a, b)

assert maximo_libreria(10, 5) == 10
assert maximo_libreria(9, 18) == 18

def maximo_ternario(a: float, b: float) -> float:
    return a if a >= b else b

assert maximo_ternario(10, 5) == 10
assert maximo_ternario(9, 18) == 18
