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
            el = self.start
            self.start = self.start.next
            return self.start
        #Implementace s hlavou
        #if self.start.next:
        #    self.start.next = self.start.next.next
        
            
        
        

    def remove_last(self):
        #TODO: Vrátí a odmaže poslední prvek se seznamu ... něco jako funkce pop pro zásobník (0.25 bodu)
        last = self.start
        current = self.start
        if current:
            while current.next:
                last = current
                current = current.next
            el = last.next
            last.next = None
            return el
        else:
            return None
        

    def insert_to_ordered_list(self,x):
        #TODO: predpokladame že seznam je setrideny od nejmensiho prvku po najvetsi, vlozte novy prvek x na správné místo (0.25 bodu)
        el = Element(x)
        if self.start==None:
            self.start = el
        elif x<=self.start.value:
            self.insert_first(x)
        else:
            current = self.start
            while current.next:
                if  x<=current.next.value:
                    el.next = current.next
                    current.next = el
                    return
                else: 
                    current = current.next
            current.next = el
            

    def find(self,x):
        #TODO: Vraťte Element se spojového seznamu kterého value je x (0.25 bodu)
        current = self.start
        while current:
            if current.value==x:
                return current
            else: 
                current = current.next
        return None

    def remove(self,x):
        #TODO:Vraťe a smažte Element se spojového seznamu kterého value je x (0.25 bodu)
        if self.start==None:
            return None
        current = self.start
        if current.value==x:
            return self.remove_first()
        while current.next:
            if current.next.value==x:
                el = current.next
                current.next = current.next.next
                el.next = None
                return el
            else: 
                current = current.next
        return None

    def find_middle(self):
        #TODO: Vrátí prvek, který je v prostředku seznamu (pokud to není jednoznačné vraťte druhý v pořadí). Při implementaci nepoužívejte znalost o délce seznamu. (0.25 bodu)
        slow = self.start
        fast = self.start

        while fast:
            if fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return slow
        return slow

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
        current = None
        self.start=None
        self._count = len(list_of_values)
        for val in list_of_values:
            el = ElementPlus(val)
            if not self.start:
                
                self.start = el
                el.before = None
                current = el
            else:
                el.before = current
                current.next = el
                current = el
        self.end = current

    def __str__(self):
        current = self.start
        s = ''
        while current:
            s+=' <-> '+str(current)
            current = current.next
            assert(current==None or current.next==None or current.next.before == current)
        return s

    def insert_first(self,x):
        #TODO: Vloží prvek x na první místo v seznamu, nezapomeňte aktualizovat count (0.25 bodu)
        el = ElementPlus(x)
        el.next = self.start
        if self.start:
            self.start.before = el
        else:
            self.end = el
        self.start = el
        self._count+=1
        
        

    def insert_last(self,x):
        #TODO: Vloží prvek x na konec seznamu (0.25 bodu)
        el = ElementPlus(x)
        el.before = self.end
        if self.end:
            self.end.next = el
        else:
            self.start = el
        self.end = el
        self._count+=1

    def remove_first(self):
        #TODO: Vrátí a odmaže první prvek se seznamu ... něco jako funkce deque pro frontu (0.25 bodu)
        if self.start:
            if self.start.next:
                self.start.next.before = None
            else:
                self.end = None
            el = self.start
            self.start = self.start.next
            self._count-=1
            return el
        return None

    def remove_last(self):
        #TODO: Vrátí a odmaže poslední prvek se seznamu ... něco jako funkce pop pro zásobník (0.25 bodu)
        if self.end:
            if self.end.before:
                self.end.before.next = None
            else:
                self.start = None
            el = self.end
            self.end = self.end.before
            self._count-=1
            return el
        return None

    def insert_to_ordered_list(self,x):
        #TODO: predpokladame že seznam je setrideny od nejmensiho prvku po najvetsi, vlozte novy prvek x na správné místo (0.25 bodu)
        el = Element(x)
        
        if self.start==None:
            self._count+=1
            self.start = el
            self.end = el
        elif x<=self.start.value:
            self.insert_first(x)
        else:
            current = self.start
            while current.next:
                if x<=current.next.value:
                    self._count+=1
                    el.next = current.next
                    el.before = current

                    current.next.before = el
                    current.next = el
                    return
                else: 
                    current = current.next
            self.insert_last(x)

    def remove(self,x):
        #TODO:Vraťe a smažte Element se spojového seznamu kterého value je x (0.25 bodu)
        if self.start==None:
            return None
        current = self.start
        if current.value==x:
            return self.remove_first()
        while current.next:
            if current.next.value==x:
                el = current.next
                if current.next.next:
                    current.next.next.before = current
                else:
                    self.end = current
                current.next = current.next.next
                
                el.next = None
                el.before = None
                self._count-=1
                return el
            else: 
                current = current.next
        return None

    def __len__(self):
        return self._count
        
l = [1,2,3,4,5]
print(len(l))

#Slovnik - dictionary
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
x.remove_last()
print(x)
print('Len:',len(x))
print(x.find_middle().value)
x.insert_to_ordered_list(10)
print(x)
print(x.find_middle().value)
x.insert_to_ordered_list(10)
x.insert_to_ordered_list(0)
print(x.find(3))
print(x.find(20))
print(x)
x.remove(4)
print(x)
x.insert_to_ordered_list(4)
print(x)
x = LinkedList([1])
print(x.find_middle())

#Test obojsmerneho spojoveho zoznamu
x = BidirectionalLinkedList([1,2,3,4,5,6])
print(x)
x.insert_first(0)
print(x)
x.insert_last(200)
print(x)
x.remove_first()
x.remove_last()
x.insert_last(200)
x.insert_last(200)
x.insert_first(0)
print(x)
print('Len:',len(x))
x.insert_to_ordered_list(10)
x.remove(4)
print(x)
x.insert_to_ordered_list(10)
x.insert_to_ordered_list(0)
x.remove(200)
x.remove(200)
print(x)
x = BidirectionalLinkedList([])
print(x)
x.insert_last(5)
print(x)
x.remove_first()
print(x)
x.insert_first(10)
print(x)
x.remove_last()
x.insert_to_ordered_list(100)
print(x)
x.remove(100)
print(x)





