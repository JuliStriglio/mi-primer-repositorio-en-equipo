from typing import Iterable

def suma_cubo_pares_for(numeros: Iterable[int]) -> int:

    suma = 0
    for n in numeros:
        cubo = n**3
    for n in numeros:
        if n % 2 == 0:
              suma +=n

    return suma

assert suma_cubo_pares_for([1, 2, 3, 4, 5, 6]) == 288
