from typing import Iterable

def suma_cubo_pares_for(numeros: Iterable[int]) -> int:

    cubos=[]
    suma = 0
    for n in numeros:
        cubo = n**3
        cubos.append(cubo)

    for m in cubos:
        if m % 2 == 0:
            suma = suma + m

    return suma

assert suma_cubo_pares_for([1, 2, 3, 4, 5, 6]) == 288


###############################################################################

def suma_cubo_pares_sum_list(numeros: Iterable[int]) -> int:
     return sum(s ** 3 for s in numeros if s % 2 == 0)

assert suma_cubo_pares_for([1, 2, 3, 4, 5, 6]) == 288


###############################################################################

    #Re-Escribir utilizando expresiones generadoras (debe resolverse en 1 línea)
   # y la función sum.




###############################################################################

numeros = [1, 2, 3, 4, 5, 6]

numeros_al_cubo = list(map(lambda l: l ** 3, numeros))
numeros_al_cubo_pares = list(map(lambda n: n**3, filter(lambda l: l % 2 ==0, numeros)))
suma_numeros_al_cubo_pares = sum(map(lambda n: n**3, filter(lambda l: l % 2 ==0, numeros)))
numeros_ordenada = sorted(numeros, key=lambda l: l % 2 ==0)

assert numeros_al_cubo == [1, 8, 27, 64, 125, 216]
assert numeros_al_cubo_pares == [8, 64, 216]
assert suma_numeros_al_cubo_pares == 288
assert numeros_ordenada == [1, 3, 5, 2, 4, 6]