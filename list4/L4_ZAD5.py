class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def __str__(self):
        current = self.head
        li = []
        while current != None:
            li.append(current.get_data())
            current = current.get_next()
        s = ("elements in the list are [" + ', '.join(['{}'] * len(li)) + "]")
        return s.format(*li)

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        if self.is_empty():
            print("List already empty")
            return
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
                if current == None:
                    print("Item not found")
                    return

        if previous == None:  # jeśli usuwamy pierwszy element
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        """
        Metoda dodająca element na koniec listy.
        Przyjmuje jako argument obiekt, który ma zostać dodany.
        Niczego nie zwraca.
        """
        current = self.head
        previous = None
        temp = Node(item)

        if not self.is_empty():

            while current != None:
                previous = current
                current = current.get_next()

            previous.set_next(temp)

        else:
            self.add(item)

    def index(self, item):
        """
        Metoda podaje miejsce na liście,
        na którym znajduje się określony element -
        element pod self.head ma indeks 0.
        Przyjmuje jako argument element,
        którego pozycja ma zostać określona.
        Zwraca pozycję elementu na liście lub None w przypadku,
        gdy wskazanego elementu na liście nie ma.
        """
        index = 0
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
                return index
            else:
                current = current.get_next()
                index += 1

    def insert(self, pos, item):
        """
        Metoda umieszcza na wskazanej pozycji zadany element.
        Przyjmuje jako argumenty pozycję,
        na której ma umiescić element oraz ten element.
        Niczego nie zwraca.
        Rzuca wyjątkiem IndexError w przypadku,
        gdy nie jest możliwe umieszczenie elementu
        na zadanej pozycji (np. na 5. miejsce w 3-elementowej liście).
        """
        current = self.head
        previous = None
        temp = Node(item)
        index = 0

        if pos > self.size() or pos < -self.size() - 1:
            raise IndexError("Wrong position!")

        else:
            if pos < 0:
                pos += self.size() + 1

            if pos == 0:
                self.add(item)

            else:
                while current != None and index < pos:
                    previous = current
                    current = current.get_next()
                    index += 1

                previous.set_next(temp)
                temp.set_next(current)

    def pop(self, pos=-1):
        """
        Metoda usuwa z listy element na zadaniej pozycji.
        Przyjmuje jako opcjonalny argument pozycję,
        z której ma zostać usunięty element.
        Jeśli pozycja nie zostanie podana,
        metoda usuwa (odłącza) ostatni element z listy.
        Zwraca wartość usuniętego elementu.
        Rzuca wyjątkiem IndexError w przypadku,
        gdy usunięcie elementu z danej pozycji jest niemożliwe.
        """
        current = self.head
        previous = None
        index = 0

        if self.is_empty():
            raise IndexError("Data structure already empty!")
        elif pos >= self.size() or pos < -self.size():
            raise IndexError("Wrong position!")

        else:
            if pos < 0:
                pos += self.size()

            if self.size() == 1:
                self.head = None
                return current.get_data()
            else:
                while current != None and index < pos:
                    previous = current
                    current = current.get_next()
                    index += 1

                if previous == None:  # jeśli usuwamy pierwszy element
                    self.head = current.get_next()
                    return current.get_data()
                else:
                    previous.set_next(current.get_next())
                    return current.get_data()

    def peek(self):
        """
        Metoda podaje wartość elementu na końcu listy
        nie ściągajac go.
        Nie pobiera argumentów.
        Jeśli lsta jest pusta, rzuca wyjątkiem IndexError.
        """
        current = self.head
        previous = None

        if not self.is_empty():

            while current != None:
                previous = current
                current = current.get_next()

            return previous.get_data()

        else:
            raise IndexError("Data structure is empty!")
