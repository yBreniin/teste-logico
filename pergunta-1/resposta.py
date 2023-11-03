arr = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]

arr.sort(key=lambda x: x != 1)

print(arr)
input("Sair do Terminal")