# 13.4 Escribir un método booleano IDENTICOS() que permita decir si dos árboles binarios son iguales
# Un nodo de un arbol binario contiene datos, y apunta hacia el hijo izquierdo y apunta hacia el hijo derecho
class Node:
    # Metodo constructor para crear un nuevo nodo
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Dados dos arboles, retornar verdadero si los dos son estructuralmente identicos
    def identicalTrees(a, b):
        # 1. Primer ejemplo con ambos vacios
        if a is None and b is None:
            return True

        # 2. Segundo ejemplo ambos con valores definidos -> Se comparan
        if a is not None and b is not None:
            return ((a.data == b.data) and
                    identicalTrees(a.left, b.left) and
                    identicalTrees(a.right, b.right))

        # 3. Tercer ejemplo uno vacio el otro no | Retorna falso
        return False

    # Pruebas
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(4)
    root2.left.left = Node(3)
    root2.left.right = Node(5)

    if identicalTrees(root1, root2):
        print("Ambos árboles son idénticos")
    else:
        print("Los árboles no son idénticos")