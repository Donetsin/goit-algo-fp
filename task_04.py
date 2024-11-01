"""
Коментарі до коду
Клас Node:
Створює вузол бінарного дерева з лівим та правим дочірніми вузлами, 
значенням, кольором та унікальним ідентифікатором.

Функція add_edges:
Рекурсивно додає вузли та ребра до графу, обчислюючи координати для кожного вузла.
Використовує унікальні ідентифікатори вузлів для додавання їх до графу 
та встановлення ребер між ними.

Функція draw_tree:
Створює орієнтований граф та викликає функцію add_edges для додавання вузлів та ребер.
Створює список кольорів та міток для вузлів.
Використовує matplotlib для візуалізації графу з вказаними параметрами.

Створення та відображення дерева:
Створює бінарне дерево з коренем та дочірніми вузлами.
Викликає функцію draw_tree для візуалізації дерева.

Цей код дозволяє створювати та візуалізувати бінарне дерево 
з унікальними ідентифікаторами вузлів, кольорами та значеннями.
"""

import uuid
import networkx as nx
import matplotlib.pyplot as plt

# Клас Node представляє вузол бінарного дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Лівий дочірній вузол
        self.right = None  # Правий дочірній вузол
        self.val = key  # Значення вузла
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла

# Функція для додавання вузлів та ребер до графу
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Додаємо вузол до графу
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            # Додаємо ребро між поточним вузлом та його лівим дочірнім вузлом
            graph.add_edge(node.id, node.left.id)
            # Обчислюємо координати для лівого дочірнього вузла
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            # Рекурсивно додаємо лівий дочірній вузол
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            # Додаємо ребро між поточним вузлом та його правим дочірнім вузлом
            graph.add_edge(node.id, node.right.id)
            # Обчислюємо координати для правого дочірнього вузла
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            # Рекурсивно додаємо правий дочірній вузол
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для візуалізації дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()  # Створюємо орієнтований граф
    pos = {tree_root.id: (0, 0)}  # Початкова позиція кореня дерева
    tree = add_edges(tree, tree_root, pos)  # Додаємо вузли та ребра до графу

    # Створюємо список кольорів для вузлів
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    # Створюємо мітки для вузлів
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    # Створюємо фігуру для відображення графу
    plt.figure(figsize=(8, 5)) 
    # Візуалізуємо граф
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)