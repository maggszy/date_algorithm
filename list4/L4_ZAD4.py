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
        return self.list_of_items[len(self.list_of_items)-1]
        
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
        return self.list_of_items==[]
        
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


def checking_HTML_correctness(filename):
    """
    Funkcja ma za zadanie sprawdzać poprawność składni dokumentu HTML.
    Jako argument przyjmuje nazwę pliku, który ma sprawdzić.
    Zwraca True jeśli dokument jest poprawny składniowo i False jeśli nie jest.
    """

    file_obj = open(filename, 'r')
    text = list(file_obj.read())
    ignore=['!DOCTYPE','area','base','br','br','col','command','embed','hr','img','input','keygen','link','meta','param','source','track','wbr','!--']
    stack_tags=Stack()
    stack_brackets=Stack()

    for i in range(len(text)):
        if text[i]=="<":
            stack_brackets.push(text[i])
            i+=1

            tag=''
            while text[i] != '>':
                tag +=text[i]
                i+=1
                
            tag= tag.split(' ')[0]
            if stack_tags.is_empty() and (tag not in ignore):
                stack_tags.push(tag)
            elif tag in ignore:
                pass
            elif  stack_tags.is_empty()==False and (tag not in ignore):
                if tag == '/'+ stack_tags.peek():
                    stack_tags.pop()
                else:
                    stack_tags.push(tag)
        
        elif text[i]==">":
            if stack_brackets.is_empty():
                return False
            elif stack_brackets.peek()=="<":
                stack_brackets.pop()

    if stack_brackets.is_empty() and stack_tags.is_empty():
        return True
    else:
        return False

#a=print(checking_HTML_correctness('L4_ZAD4_sampleHTML_3.txt'))  #False
#a=print(checking_HTML_correctness('L4_ZAD4_sampleHTML_2.txt'))  #False
#a=print(checking_HTML_correctness('L4_ZAD4_sampleHTML_1.txt'))  #True