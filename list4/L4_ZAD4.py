import re

class Stackk():
    """
    Last in, first out
    (początek stostu od lewej)
    """

    def __init__(self):
        self.list_of_items = []
        
    def enqueue(self, item):
        self.list_of_items.append(item)
    
    def peek(self):
        return self.list_of_items[len(self.list_of_items - 1)]
        
    def dequeue(self):
        return self.list_of_items.pop()
    
    def is_empty(self):
        return self.list_of_items==[]
        
    def size(self):
        return len(self.list_of_items) 

def checking_HTML_correctness(filename):
    """
    Funkcja ma za zadanie sprawdzać poprawność składni dokumentu HTML.
    Jako argument przyjmuje nazwę pliku, który ma sprawdzić.
    Zwraca True jeśli dokument jest poprawny składniowo i False jeśli nie jest.
    """
    file_obj = open(filename, 'r')
    text = file_obj.read()
    #idk jak zrobić jeśli mają atrybuty jakieś
    ignore=['<area>','<base>','<br>','<col>','<command>','<embed>','<hr>','<img>','<input>','<keygen>','<link>','<meta>','<param>','<source>','<track>','<wbr>']
    stack=Stackk()
    pattern = re.compile('<.*?>')
    pattern_cl=  re.compile('</.*?>')
    tag_list = re.findall(pattern, text)
    print(tag_list)

    balanced = True
    index = 0
    #while index < len(tag_list):
     #   s

a=print(checking_HTML_correctness('L4_ZAD4_sampleHTML_3.txt'))

def clean(list):
    comment=re.compile('<!--.*?-->')
    cm= re.findall(comment, list)
    print(cm)

b=clean(a)

