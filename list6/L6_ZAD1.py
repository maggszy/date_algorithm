class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key=key
        self.payload=[val]
        self.left_child=left
        self.right_child=right
        self.parent=parent
        self.counter=1
        
    def has_left_child(self):
        return self.left_child
        
    def has_right_child(self):
        return self.right_child
        
    def is_left_child(self):
        return self.parent and self.parent.left_child==self 
    
    def is_right_child(self):
        return self.parent and self.parent.right_child==self 
        
    def is_root(self):
        return not self.parent 
        
    def is_leaf(self):
        return not (self.right_child or self.left_child)
        
    def has_any_children(self):
        return self.right_child or self.left_child
        
    def has_both_children(self):
        return self.right_child and self.left_child
        
    def replace_node_data(self,key,value,lc,rc):
        self.key=key
        self.payload=[value] 
        self.left_child=lc
        self.right_child=rc
        if self.has_left_child():
            self.left_child.parent=self
        if self.has_right_child():
            self.right_child.parent=self

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0
        
    def length(self):
        return self.size
        
    def __len__(self):
        return self.size
        
    def __iter__(self):
        return self.root.__iter__()
        
    def put(self,key,val): 
        if self.root:
            self._put(key,val,self.root) #_put is a helper function
        else:
            self.root=TreeNode(key,val)
        self.size=self.size+1 
            
    def _put(self,key,val,currentNode):
        if key<currentNode.key:
            if currentNode.has_left_child():
                self._put(key,val,currentNode.left_child)
            else:
                currentNode.left_child=TreeNode(key,val,parent=currentNode)
        elif key == currentNode.key:
            currentNode.counter +=1
            currentNode.payload.append(val)
        else:
            if currentNode.has_right_child():
                self._put(key,val,currentNode.right_child)
            else:
                currentNode.right_child=TreeNode(key,val,parent=currentNode)
                
    def __setitem__(self,k,v): #overloading of [] operator 
        self.put(k,v)
        
    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None 
        else:
            return None
            
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key==key:
            return currentNode 
        elif key<currentNode.key:
            return self._get(key,currentNode.left_child)
        else:
            return self._get(key,currentNode.right_child)
            
    def __getitem__(self,key):#overloading of [] operator
        return self.get(key)
        
    def __contains__(self,key):#overloading of in operator
        if self._get(key,self.root):
            return True 
        else:
            return False


    def delete(self,key):
        if self.size>1:
            nodeToRemove=self._get(key,self.root)
            if nodeToRemove.counter > 1:
                nodeToRemove.counter -=1
                nodeToRemove.payload.pop() 
                self.size = self.size -1 
            else:
                if nodeToRemove:
                    self.remove(nodeToRemove)
                    self.size=self.size-1
                else:
                    raiseKeyError('Error, key not in tree')
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size=self.size-1
        else:
            raiseKeyError('Error, key not in tree')

    def __delitem__(self,key):#overloading of del operator
        self.delete(key)

    def spliceOut(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child=None
            else:
                self.parent.right_child=None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child=self.left_child
                else:
                    self.parent.right_child=self.left_child
                    self.left_child.parent=self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child=self.right_child
                else:
                    self.parent.right_child=self.right_child
                    self.right_child.parent=self.parent
                    
    def findSuccessor(self):
        succ=None
        if self.has_right_child():
            succ=self.right_child.findMin()
        else:
            if self.parent:
                if self.is_left_child():
                    succ=self.parent
                else:
                    self.parent.right_child=None
                    succ=self.parent.findSuccessor()
                    self.parent.right_child=self
        return succ
        
    def findMin(self):
        current=self
        while current.has_left_child():
            current=current.left_child
        return current
        
    def remove(self,currentNode):
        if currentNode.is_leaf():#leaf 
            if currentNode==currentNode.parent.left_child:
                currentNode.parent.left_child=None
            else:
                currentNode.parent.right_child=None
        elif currentNode.has_both_children(): #interior
            succ=currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key=succ.key
            currentNode.payload=succ.payload
        else: #this node has one child
            if currentNode.has_left_child():
                if currentNode.is_left_child():
                    currentNode.left_child.parent=currentNode.parent
                    currentNode.parent.left_child=currentNode.left_child
                elif currentNode.is_right_child():
                    currentNode.left_child.parent=currentNode.parent
                    currentNode.parent.right_child=currentNode.left_child
                else:
                    currentNode.replace_node_data(currentNode.left_child.key,
                                            currentNode.left_child.payload,
                                            currentNode.left_child.left_child,
                                            currentNode.left_child.right_child)
            else:
                if currentNode.is_left_child():
                    currentNode.right_child.parent=currentNode.parent
                    currentNode.parent.left_child=currentNode.right_child
                elif currentNode.is_right_child():
                    currentNode.right_child.parent=currentNode.parent
                    currentNode.parent.right_child=currentNode.right_child
                else:

                    currentNode.replace_node_data(currentNode.right_child.key,
                                            currentNode.right_child.payload,
                                            currentNode.right_child.left_child,
                                            currentNode.right_child.right_child)

    
# BST = BinarySearchTree()
# BST.put(3, 'third')
# BST.put(4,'fourth')
# BST.put(5,'fifth')
# BST.put(1,'first')
# BST.put(2, 'second')
# BST.put(3, 'thid')
# BST.put(3, 'thid')

# print('Tree root key: ', BST.root.key)
# print('Tree root left child key', BST.root.left_child.key)
# print('Tree root left child child key', BST.root.left_child.right_child.key)
# #print('Proba znalezienia drugiej 3', BST.root.left_child.left_child.key)
# print('Tree root right child key', BST.root.right_child.key)
# print('Tree root right child child key', BST.root.right_child.right_child.key)
# print('Tree root powtarzalność: ', BST.root.counter)
# print('wartość podwojonego klucza:',BST.root.payload)
# print('get get:', BST.get(5))
# print('------------------------------------')
# BST.delete(3)
# print('wielkość:', BST.length())

# print('Tree root powtarzalność: ', BST.root.counter)
# print('tree root value:',BST.root.payload)
# print('Tree root left child key', BST.root.left_child.key)
# # print('Tree root right child key', BST.root.right_child.key)
# #print(BST[0],BST[1],BST[2],BST[3],BST[4])
# #print(BST) dupaaa
# print('-------------------------------')
# # # BST.delete(1)
# # print('Tree root left child key', BST.root.left_child.key)
# print('Tree root left child value', BST.root.left_child.payload)