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
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


def bracket_check(sym_list): #musi być lista stringów
    stack = Stack()           
    balanced = True       
    i = 0
    while i < len(sym_list) and balanced: 
        symbol = sym_list[i]             
        if symbol == "(":                         
            stack.push(symbol)
        else:
            if stack.is_empty():                      
                balanced = False
            else:
                stack.pop()                           

        i = i + 1

    if balanced and stack.is_empty():
        return True
    else:
        return False


