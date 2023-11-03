def find_fruit(node, target, path=[]):
    if isinstance(node, list):
        for i, item in enumerate(node):
            if find_fruit(item, target, path + [i]):
                return path + [i]
    elif target == node:
        return path + [target]

    return None

def print_path(tree, path):
    current_tree = tree
    result_path = []
    for step in path:
        result_path.append(current_tree[step])
        current_tree = current_tree[step][1] if isinstance(current_tree[step][1], list) else None

    print(" -> ".join(map(str, result_path)))

tree = [
    "Maça",
    [
        "Morango",
        ["Goiaba", "Limão"]
    ],
    [
        "Pera",
        [
            "Abacaxi",
            [
                "Laranja",
                ["Banana", "Cebola"]
            ]
        ]
    ]
]

while True:
    fruit_choice = input("Escolha uma fruta (ou 'sair' para encerrar): ")
    
    if fruit_choice.lower() == 'sair':
        break

    path_to_fruit = find_fruit(tree, fruit_choice)

    if path_to_fruit:
        print("Caminho até", fruit_choice, ":")
        print_path(tree, path_to_fruit)
    else:
        print(f"A fruta {fruit_choice} não foi encontrada na árvore.")
