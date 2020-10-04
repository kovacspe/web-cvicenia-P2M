class Node:
    def __init__(self,value : int):
        self.left_son = None
        self.right_son = None
        self.value = value

    def is_leaf(self):
        return not self.left_son and not self.right_son

    def diam(self):
        if self.is_leaf():
            return (1,1)
        else:
            (left_diam,left_depth) = self.left_son.diam() if self.left_son else (0,0)
            (right_diam,right_depth) = self.right_son.diam() if self.right_son else (0,0)
            max_diam = max(max(left_diam,right_diam),left_depth+right_depth+1)
            depth = 1+max(left_depth,right_depth)
        return max_diam,depth
    
    def number_of_nodes_in_subtree(self):
        left = self.left_son.number_of_nodes_in_subtree() if self.left_son else 0
        right = self.right_son.number_of_nodes_in_subtree() if self.right_son else 0
        return left+1+right

    def find(self,value):
        if value<self.value:
            if self.left_son:
                return self.left_son.find(value)
            else:
                raise KeyError(f'Key \"{value}\" not found')
        elif value>self.value:
            if self.right_son:
                return self.right_son.find(value)
            else:
                raise KeyError(f'Key \"{value}\" not found')
        else:
            return self

    def add(self,node):
        if node.value<self.value:
            if self.left_son:
                self.left_son.add(node)
            else:
                self.left_son = node
        else:
            if self.right_son:
                self.right_son.find(node)
            else:
                self.right_son = node

    def delete_inorder_successor(self):
        if self.left_son:
            self.left_son, deleted_node = self.left_son.delete_inorder_successor()
            return self, deleted_node
        else:
            return self.right_son, self
        

    def delete(self,value):
        if value < self.value: 
            if self.left_son:
                self.left_son = self.left_son.delete(value) 
            else:
                raise KeyError(f'Key \"{value}\" not found')
        elif value > self.value:
            if self.right_son:
                self.right_son = self.right_son.delete(value) 
            else:
                raise KeyError(f'Key \"{value}\" not found')
        else: 
            # Tento vrchol sa bude odstranovat
            
            if not self.left_son: 
                tmp = self.right_son  
                self.right_son = None
                return tmp  
            
            elif not self.right_son: 
                tmp = self.left_son  
                self.left_son = None
                return tmp   
            else:
                # Má dvoch potomkov, hľadáme najmenšieho z pravého podstromu
                self.right_son, tmp = self.right_son.delete_inorder_successor()
                tmp.right_son = self.right_son
                tmp.left_son = self.left_son
                self.right_son = None
                self.left_son = None
                return tmp
        return self

    def __str__(self):
        if self.is_leaf():
            return str(self.value) 
        left = str(self.left_son) if self.left_son else ''
        right = str(self.right_son) if self.right_son else ''
        return f'[{left}] {self.value} [{right}]'

        rohliky = 10
        housky = 5
        # Rohliky: 10, Housky: 5
        print('Rohliky: ',rohliky,' Housky: ',housky)
        print(f'Rohliky: {rohliky}, Housky: {housky}')
        print(''.format())

    
    # POkojne si doplňte vlastné metódy aj na Node

t = Tree()
t2 = Tree()
t2.find('5')


l.append()
#

x = 5

class Tree:
    def __init__(self,root_node : Node):
        self.root = root_node

    def _build_tree(self,l):
        #Postaví strom a vráti vrchol
        if len(l) == 1:
            return Node(l[0])
        else:
            mid = (len(l)-1)//2
            parent = Node(l[mid])
            if mid>=1:
                parent.left_son= self._build_tree(l[0:mid])
            if mid < len(l)-1:
                parent.right_son = self._build_tree(l[mid+1:len(l)])
            return parent

    def __init__(self,list : list):
        list.sort()
        self.root = self._build_tree(list)

    def add_recursive(self,value):
        node = Node(value)
        if self.root:
            self.root.add(node)
        else:
            self.root = node

    def add(self,value):
        node = Node(value)
        current = self.root
        while current:
            if value>current.value:
                if current.right_son:
                    current = current.right_son
                else:
                    current.right_son = node
                    return
            else: 
                if current.left_son:
                    current = current.left_son
                else:
                    current.left_son = node
                    return
        self.root= node
        
    def find_recursive(self,value):
        if self.root:
            return self.root.find(value)
        else:
            raise KeyError(f'Key \"{value}\" not found')

    def find(self,value):   
        current = self.root
        while current and current.value!=value:
            if value>current.value:
                current = current.right_son
            else: 
                current = current.left_son

        if not current:
            raise ValueError(f'Element \"{value}\" not found')
        return current

    def recursive_delete(self,value):
        if self.root:
            self.root = self.root.delete(value)
        else:
            raise KeyError(f'Key \"{value}\" not found')
   

    def diameter(self):
        if self.root:
            return self.root.diam()[0]
        else:
            return 0

    def __len__(self):
        if self.root:
            return self.root.number_of_nodes_in_subtree()
        else:
            return 0

    def __str__(self):
        return str(self.root)


t = Tree([1,2,3,40,50,60])
print(t)
t.recursive_delete(60)
print(t)
t.add(0)
print(t)
t.add(10)
t.add(8)
print(t)
print(len(t))
print(t.find(10))
t.add(41)
t.add(42)
t.add(43)
print(t)

print('DIAM:',t.diameter())

print(t.find(11))











def fib(n):
    if n<2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fakt(n):
    if n==1:
        return 1
    else:
        return n*fakt(n-1)


def nsd(x, y):
    if x > y:
        return nsd(x-y, y)
    elif x < y:
        return nsd(x, y-x)
    else:
        return x



    