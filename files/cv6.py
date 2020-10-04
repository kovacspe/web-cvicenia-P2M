class ElementPlus:
    def __init__(self,x):
        self.value = x
        self.next = None
        self.before = None

    def __str__(self):
        return str(self.value)



# Za implementaci je možné získat maximálně 1 bod
class Element:
    def __init__(self,x):
        self.value = x
        self.next = None

    def __str__(self):
        return str(self.value)


el = Element(6)     

class LinkedList:
    def __init__(self):
        head = None
        #head = Element(None)
        self.start = head
        # Je možné pamatovat si konec seznamu
        #self.end = None
        # Je možné udržovat si počet prvku
        #self.count = 0        

    def __init__(self,list_of_values):
        current = None
        self.start=None
        self.count = len(list_of_values)
        for val in list_of_values:
            el = Element(val)
            if not self.start:
                
                self.start = el
                current = el
            else:
                current.next = el
                current = el
    
    #Implementace s hlavou
    """
    def __init__(self,list_of_values):
        current = None
        head = Element(None)
        self.start = head
        current = head
        for val in list_of_values:
            el = Element(val)
            current.next = el
            current = el
            
    """
                
            

    def __str__(self):
        current = self.start
        s = ''
        while current:
            s+=' -> '+str(current.value)
            current = current.next
        return s

    
    def insert_first(self,x):
        # bez hlavy
        el = Element(x)
        el.next = self.start
        self.start = el
        self.count+=1
        #Implementace s hlavou
        #el = Element(x)
        #el.next = self.start.next
        #self.start.next = el
        

    # Bez hlavy
    def insert_last(self,x):
        # Bez hlavy
        last = self.start
        current = self.start
        while current:
            last = current
            current = current.next
        el = Element(x)
        if last:
            last.next = el
        else:
            self.start = el

        #Implementace s hlavou
        #last = self.start
        #current = self.start
        #while current:
        #    last = current
        #    current = current.next
        #el = Element(x)
        #last.next = el


    def remove_first(self):
        #bez hlavy
        if self.start:
            self.start = self.start.next
        #Implementace s hlavou
        #if self.start.next:
        #    self.start.next = self.start.next.next
        
            
        
        

    def remove_last(self):
        #TODO: Vrátí a odmaže poslední prvek se seznamu ... něco jako funkce pop pro zásobník (0.25 bodu)
        pass

    def insert_to_ordered_list(self,x):
        #TODO: predpokladame že seznam je setrideny od nejmensiho prvku po najvetsi, vlozte novy prvek x na správné místo (0.25 bodu)
        pass

    def find(self,x):
        #TODO: Vraťte Element se spojového seznamu kterého value je x (0.25 bodu)
        pass

    def remove(self,x):
        #TODO:Vraťe a smažte Element se spojového seznamu kterého value je x (0.25 bodu)
        pass

    def find_middle(self):
        #TODO: Vrátí prvek, který je v prostředku seznamu (pokud to není jednoznačné vraťte druhý v pořadí). Při implementaci nepoužívejte znalost o délce seznamu. (0.25 bodu)
        pass 

    # Co znamena __len__ + rychla a pomala implementace
    def __len__(self):
        current = self.start
        counter = 0
        while current:
            current = current.next
            counter+=1
        return counter
        # Je možné si držať v pamäti counter a upraovavť ho vždy keď je potrebné. Potom stačí:
        #return self.count


# Za implementaci je možné získat maximálně 1 bod
class BidirectionalLinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        # Udrzujeme pocet prvku
        self._count = 0

    def __init__(self,list_of_values):
        # Vytvoťí dvoujcestný spojový seznam z listu list_of_values. (0.25 bodu)
        pass 

    def __str__(self):
        current = self.start
        s = ''
        while current:
            s+=' <-> '+current.value
            current = current.next
            assert(current==None or current.next==None or current.next.before == current)
        return s

    def insert_first(self,x):
        #TODO: Vloží prvek x na první místo v seznamu, nezapomeňte aktualizovat count (0.25 bodu)
        pass

    def insert_last(self,x):
        #TODO: Vloží prvek x na konec seznamu (0.25 bodu)
        pass

    def remove_first(self):
        #TODO: Vrátí a odmaže první prvek se seznamu ... něco jako funkce deque pro frontu (0.25 bodu)
        pass

    def remove_last(self):
        #TODO: Vrátí a odmaže poslední prvek se seznamu ... něco jako funkce pop pro zásobník (0.25 bodu)
        pass

    def insert_to_ordered_list(self,x):
        #TODO: predpokladame že seznam je setrideny od nejmensiho prvku po najvetsi, vlozte novy prvek x na správné místo (0.25 bodu)
        pass

    def remove(self,x):
        #TODO:Vraťe a smažte Element se spojového seznamu kterého value je x (0.25 bodu)
        pass

    def __len__(self):
        return self._count
        
l = [1,2,3,4,5]
print(len(l))


d = {'car':'auto',
 'house':'dum'}
print(d['car'])


# Test spojoveho seznamu
x = LinkedList([1,2,3,4,5,6])
print(x)
x.insert_first(0)
print(x)
x.insert_last(200)
print(x)
x.remove_first()
print(x)
print(len(x))


