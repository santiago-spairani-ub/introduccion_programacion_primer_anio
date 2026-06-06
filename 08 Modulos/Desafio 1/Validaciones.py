def elementoRepetido(lista: list[int], nuevo_num: int):
    return nuevo_num in lista;


def limpiarElementosRepetidos(lista: list[int]):
    return list(set(lista));