class UnorderedList(object):
  """
  Tutaj, skopiuj swoją implementację klasy UnorderedList,
  wykonaną jako rezultat Zadania 5.
  """

class DequeueUsingUL(object):

  def __init__(self):
    self.items = UnorderedList()

  def is_empty(self):
    """
    Metoda sprawdzajacą, czy kolejka jest pusta.
    Nie pobiera argumentów.
    Zwraca True lub False.
    """
    
  def add_left(self, item):
    """
    Metoda dodaje element do kolejki z lewej strony.
    Pobiera jako argument element, który ma zostać dodany.
    Niczego nie zwraca.
    """
    
  def add_right(self, item):
    """
    Metoda dodaje element do kolejki z prawej strony.
    Pobiera jako argument element, który ma zostać dodany.
    Niczego nie zwraca.
    """
    
  def remove_left(self):
    """
    Metoda usuwa element z kolejki z lewej strony.
    Nie pobiera argumentów.
    Zwraca usuwany element.
    W przypadku pustej kolejku rzuca wyjątkiem IndexError
    """
    
  def remove_right(self):
    """
    Metoda usuwa element z kolejki z prawej strony.
    Nie pobiera argumentów.
    Zwraca usuwany element.
    W przypadku pustej kolejku rzuca wyjątkiem IndexError
    """
  
  def size(self):
    """
    Metoda zwraca liczę elementów na w kolejce.
    Nie pobiera argumentów.
    Zwraca liczbę elementów na w kolejce.
    """
    