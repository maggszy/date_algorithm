class Stack():
    """
    Klasa implementująca stos używając pythonowych list.
    """

    def __init__(self):
        self.list_of_items = []

    def push(self, item):
        """
        Metoda służąca do dodawania obiektu do stosu.
        Pobiera jako argument obiekt który ma być dodany.
        Niczego nie zwraca.
        """
        self.list_of_items.append(item)

    def peek(self):
        """
        Metoda służąca do podawania jaki obiekt znajduje się na szczycie stosu.
        Nie pobiera argumentów.
        Zwraca obiekt znajdujący się na szczycie stosu, ale go stamtąd nie ściąga.
        """
        return self.list_of_items[len(self.list_of_items) - 1]

    def pop(self):
        """
        Metoda służąca do ściągania obiektów ze stosu.
        Nie pobiera argumentów.
        Zwraca ściągnięty obiekt.
        """
        return self.list_of_items.pop()

    def is_empty(self):
        """
        Metoda służąca do sprawdzania, czy stos jest pusty.
        Nie pobiera argumentów.
        Zwraca True jeśli stos jest pusty lub False gdy nie jest.
        """
        return self.list_of_items == []

    def size(self):
        """
        Metoda służąca do określania wielkości stosu.
        Nie pobiera argumentów.
        Zwraca liczbę obiektów w stosie.
        """
        return len(self.list_of_items)

    def __str__(self):
        """
        Medota odpowiadająca za nieformalną reprezentacje kolejki.
        Nie pobiera argumentów.
        """
        return str(self.list_of_items)


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key