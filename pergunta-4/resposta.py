def completa_intervalo(arr):
    if not arr:
        return arr

    max_numero = max(arr)
    intervalo_completo = set(range(max_numero + 1))

    numeros_faltando = list(intervalo_completo - set(arr))

    return arr + numeros_faltando

arr = [9, 2, 3, 1, 4]
resultado = completa_intervalo(arr)
print(resultado)
