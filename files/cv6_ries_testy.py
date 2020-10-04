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
    """   
    #Implementace s hlavou
    
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
    
                
    def to_list(self):
        l = []
        current = self.start
        while current:
            l.append(current.value)
            current = current.next
        return l

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
        
            
        
        
    """
    def remove_last(self):
        #TODO: Vrátí a odmaže poslední prvek se seznamu ... něco jako funkce pop pro zásobník (0.25 bodu)
        last = self.start
        current = self.start
        if current:
            if current.next==None:
                el = self.start
                self.start=None
                return el
            while current.next:
                last = current
                current = current.next
            el = last.next
            last.next = None
            return el
        else:
            return None
    """
    def remove_last (self): 
        current = self.start
        if not current:
            return None
        if not current.next:
            self.start = None
            return None
        while current.next.next:
            current = current.next
        current.next = None

    def insert_to_ordered_list(self, x): 
        el = Element(x)
        #Bez hlavy i s hlavou
        current = self.start
        if current.value > el.value:
            self.insert_first(x)
            return None
        while (current.next) and    (current.next.value < el.value):
            current = current.next
        following = current.next
        current.next = el
        el.next = following

    def find(self,x,pred=False):
        kontrola = self.start
        predchozi = None
        while kontrola != None:
            if kontrola.value == x:
                if pred==True:
                    return kontrola, predchozi
                else:
                    return kontrola
            else:
                predchozi = kontrola
                kontrola = kontrola.next
        return None

    def remove(self,x):
        el = Element(x)
        last = self.start
        current = self.start
        if current.value == el.value:
            self.remove_first()
            return None
        while (current.value != el.value) and (current.next):
            last = current
            current = current.next
        if (current.value != el.value):
            return "Element v seznamu není"
        last.next = current.next
        return current

    

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
        self.count=len(list_of_values)
        current = None
        self.start = None
        for v in list_of_values:
            el = ElementPlus(v)
            if self.start == None:
                self.start = el
            else:
                current.next = el
                el.before = current
            current = el
        self.end = current


    def to_list(self):
        l = []
        current = self.start
        while current:
            l.append(current.value)
            current = current.next
            assert(current==None or current.next==None or current.next.before == current)
        return l

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
        self.count = self.count+1
        el.next, self.start = self.start, el
        if el.next!=None:
            el.next.before = el
        else:
            self.end = el
        
        

    def insert_last(self,x):
        #TODO: Vloží prvek x na konec seznamu (0.25 bodu)
        el = ElementPlus(x)
        if (self.end != None):
            self.end.next = el
            el.before = self.end
        else:
            self.start = el
        self.end = el
        self.count += 1

    def remove_first(self):
        #TODO: Vrátí a odmaže první prvek se seznamu ... něco jako funkce deque pro frontu (0.25 bodu)
        if self.start==None:
            return None
        self.count=self.count-1
        el = self.start
        if el.next!=None:
            el.next.before = None
        else:
            self.end = None
        self.start = el.next
        return el

    def remove_last(self):
        #TODO: Vrátí a odmaže poslední prvek se seznamu ... něco jako funkce pop pro zásobník (0.25 bodu)
        el = self.end
        self.end = el.before
        if (self.end != None):
            self.end.next = None
        self.count -= 1
        return el.value
        pass

    def insert_to_ordered_list(self, x): 
        if self.start is None: 
            x.next = self.start 
            self.start = x 
        elif self.start.value >= x.value: 
            x.next = self.start 
            self.start = x 
        else: 
            current = self.start 
            while (current.next is not None and current.next.value < x.value): 
                current = current.next 
            x.next = current.next 
            current.next = x

    def remove(self,x):
        #TODO:Vraťe a smažte Element se spojového seznamu kterého value je x (0.25 bodu)
        current = self.start
        while (current.next.value != x) or (current.next == None):
            current = current.next
        y = current.next
        if y == None:
            return(y)
        current.next = current.next.next
        return(y)

    def __len__(self):
        return self._count
        
import random
class TestLinkedList:
    def test_remove_last(self):
        l = [1,2,3,4,5,6]
        ll = LinkedList(l)
        while len(l)>0:
            print(ll)
            if not ll.remove_last().value==l.pop():
                print('FAILED')
                return
        print('OK')

    def test_insert_in_order(self):
        l = [4,2,3,1,5,7,6]
        ll = LinkedList([])
        for i in range(len(l)):
            ll.insert_to_ordered_list(l[i])
        l.sort()
        if not ll.to_list()==l:
            print('FAILED')
            print(ll.to_list())
            print(l)
        else:
            print('OK')

    def test_remove(self):
        l = list(range(30))
        ll = LinkedList(l)
        while len(l)>0:
            r = random.random()
            if r<0.3:
                x = l[0] 
            elif r>0.7:
                x=l[len(l)-1]
            else:
                x = l[random.randint(0,len(l)-1)]
            l.remove(x)
            ll.remove(x)
            if not ll.to_list()==l:
                print(l)
                print(ll)
                print('FAILED')
                return
        print('OK')
    
    def run_all(self):
        print('Remove')
        #self.test_remove_last()
        print('In order')
        #self.test_insert_in_order()
        print('remove')
        self.test_remove()


t = TestLinkedList()
t.run_all()
quit()
b = BidirectionalLinkedList([3])
b.insert_first(2)
b.insert_first(1)
print(b)
b.insert_last(80)
b.insert_last(100)
print(b)
print(b.remove_first())
print(b)
print(b.remove_first())
print(b)
print(b.remove_first())
print(b)
print(b.remove_first())
print(b.remove_first())






