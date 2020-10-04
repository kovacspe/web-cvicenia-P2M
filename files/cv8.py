class MyDict():
    def __init__(self,max):
        self._arr = [None]*max
        self._max = max
        pass

    def _hash_function(self,val):
        return val % self._max
        pass

    def insert(self,key,val):
        h = self._hash_function(key)
        self._arr[h]=(key,val)
        pass

    def __getitem__(self,key):
        h = self._hash_function(key)
        # kontrola či som to naozaj našiel
        return self._arr[h][0]
        pass


    def delete(self,key):
        pass

# 
#Vystup>
# 1 2 3 4 5
def recursive_print(list):
    if len(list)==0:
        print()
    else:
        print(list[0],end=' ')
        recursive_print(list[1:len(list)])

recursive_print([1,2,3,4,5,6,7,8,9])

def recursive_merge(l1,l2):
    #TODO: Bez použití for/while... jenom pomocí rekurze slejte dva listy(jako v merge sortu) (1 bod)
    pass

# Vzorový výstup pro recursive_merge([1,5,8,9],[2,3,10])
# >> [1,2,3,5,8,9,10]


