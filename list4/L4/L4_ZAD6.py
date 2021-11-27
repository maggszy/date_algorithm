class UnorderedList(object):
  """
  Tutaj skopiuj swoją implementację klasy UnorderedList,
  wykonaną jako rezultat Zadania 5.
  """

class StackUsingUL(object):
  def __init__(self):
    self.items = UnorderedList()

  def is_empty(self):
    """
    Metoda sprawdzajacą, czy stos jest pusty.
    Nie pobiera argumentów.
    Zwraca True lub False.
    """
  
  def push(self, item):
    """
    Metoda umieszcza nowy element na stosie.
    Pobiera element, który ma zostać umieszczony.
    Niczego nie zwraca.
    """
    
  def pop(self):
    """
    Metoda ściąga element ze stosu.
    Nie przyjmuje żadnych argumentów.
    Zwraca ściągnięty element.
    Jeśli stos jest pusty, rzuca wyjątkiem IndexError.
    """

  def peek(self):
    """
    Metoda podaje wartość elementu na wierzchu stosu
    nie ściągajac go.
    Nie pobiera argumentów.
    Zwraca wierzchni element stosu.
    Jeśli stos jest pusty, rzuca wyjątkiem IndexError.
    """

  def size(self):
    """
    Metoda zwraca liczę elementów na stosie.
    Nie pobiera argumentów.
    Zwraca liczbę elementów na stosie.
    """
    