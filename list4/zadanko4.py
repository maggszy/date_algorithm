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

    def show(self):
        return print(self.list_of_items) 


def checking_HTML_correctness(filename):
    """
    Funkcja ma za zadanie sprawdzać poprawność składni dokumentu HTML.
    Jako argument przyjmuje nazwę pliku, który ma sprawdzić.
    Zwraca True jeśli dokument jest poprawny składniowo i False jeśli nie jest.
    """
    file_obj = open(filename, 'r')
    text = file_obj.read()
    #idk jak zrobić jeśli mają atrybuty jakieś
    ignore=['<!DOCTYPE html>','<area>','<base>','<br />','<br>','<col>','<command>','<embed>','<hr>','<img>','<input>','<keygen>','<link>','<meta>','<param>','<source>','<track>','<wbr>']
    stack=Stackk()
    comment=re.compile('<!--.*?-->')
    cmm_list=re.findall(comment, text)
    pattern = re.compile('<.*?>')
    pattern_cl=  re.compile('</.*?>')
    tag_list = re.findall(pattern, text)
    print(cmm_list)

#removing comments
    for elem in cmm_list:
        for i in tag_list:
            if elem==i:
                tag_list.remove(elem)
    #print(tag_list)

#is removing tags that do not have its closing
    for elem in ignore:
        for i in tag_list:
            if elem==i:
                tag_list.remove(elem)
    #print(tag_list)            


    #print(tag_list)
    balanced = True
    index = 0
    while index < len(tag_list) and balanced:
        print(stack.show())
        tag = tag_list[index]
        if not pattern_cl.match(tag):
           stack.enqueue(tag)
           #print(stack.show())
        else:
            if stack.is_empty() or str.replace(tag, '/', '') != stack.peek():
    # s.peek() - function, which returns top of the stack without removing
                balanced = False
            else:                
                stack.pop()

        index = index + 1
        print(stack.show())
        if balanced and stack.is_empty():
            return True
        else:
            return False

#a=print(checking_HTML_correctness('L4_ZAD4_sampleHTML_3.txt'))
#a=print(checking_HTML_correctness('prawdo.txt'))
a=print(checking_HTML_correctness('moje.txt'))