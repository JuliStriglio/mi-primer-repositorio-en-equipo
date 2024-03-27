from typing import List, Union

def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:

    enteros = []
    strings = []

    for item in lista:
        if isinstance(item,(int,float)):
            enteros.append(item)
        else:
            strings.append(item)

    return strings + enteros


assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]


#########################################################################################

def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    enteros = [item for item in lista if isinstance(item, (int,float))]
    strings = [item for item in lista if not isinstance(item, (int, float))]

    return strings + enteros


assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]

#########################################################################################

