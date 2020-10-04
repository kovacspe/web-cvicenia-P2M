class Node:
    def __init__(self,value):
        self.left_son = None
        self.right_son = None
        self.value = value
    
    def number_of_nodes_in_subtree(self):
        left = self.left_son.number_of_nodes_in_subtree() if self.left_son else 0
        right = self.right_son.number_of_nodes_in_subtree() if self.right_son else 0
        return left+1+right

    # POkojne si doplňte vlastné metódy aj na Node


#
class Tree:
    def __init__(self,root_node : Node):
        self.root = root_node

    def __init__(self,list : list):
        #TODO: Naincializovať vyvážený strom z listu (0.5 bodu)
        pass

    def add(self,value):
        #TODO: Pridajte prvok do stromu (0.5 bodu)
        pass

    def find(self,value):   
        #TODO: Vráťe ukazateľ na prvok, ktorý má kľúč rovný value (0.5 bodu)
        pass

    def __len__(self):
        if self.root:
            return self.root.number_of_nodes_in_subtree()
        else:
            return 0

    def __str__(self):
        #TODO: Naprogramujte čo naprehľadnejší výpis stromu (0.5 bodu)
        pass

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



    