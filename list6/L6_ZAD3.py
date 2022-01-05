class BinHeap:
    def __init__(self, capacity):
        self.heap_list = [0]
        self.current_size = 0
        self.capacity = capacity

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        if self.current_size < self.capacity:
            self.heap_list.append(k)
            self.current_size = self.current_size + 1
            self.perc_up(self.current_size)
        else:
            BinHeap.keep_max(self, k)

    def find_min(self):
        return self.heap_list[1]

    def perc_down(self, i):  # complexity O(logn)  (?)
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):  # complexity przejmuje od percDown
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def build_heap(self, alist):  # complexity O(n) (?)
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1

    def size(self):
        return self.current_size

    def is_empty(self):
        return self.current_size == 0

    def keep_max(self, k):
        if k > BinHeap.find_min(self):
            self.heap_list.append(k)
            BinHeap.del_min(self)
            self.current_size = self.current_size + 1
        else:
            raise Exception("Heap already reached max capacity and item is smaller than root")

    def __str__(self):
        txt = "{}".format(self.heap_list[1:])
        return txt


bh = BinHeap(8)
bh.build_heap([44, 33, 77, 11, 55, 88, 66, 22])
bh.insert(28)
print(bh.current_size)
bh.insert(11)
print(bh)
