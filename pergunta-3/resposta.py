def tem_soma_combinacao(arr, X):
    numeros_vistos = set()

    for num in arr:
        complemento = X - num
        if complemento in numeros_vistos:
            return True
        numeros_vistos.add(num)

    return False

arr = [1, 15, 2, 7, 2, 5, 7, 1, 4]

X = int(input("Digite o valor de X: "))

resultado = tem_soma_combinacao(arr, X)
print(resultado)
