# Ukázková implementace zásobníku
class Stack:
    def __init__(self):
        self._arr = []

    def push(self,it):
        self._arr.append(it)

    def pop(self):
        return self._arr.pop()
    
    def print(self):
        print(self._arr)

stack = Stack()
stack.push(1)
stack.push(2)
stack2 = Stack()
stack2.push(8)
stack.push(3)
stack.print()
print(stack.pop())
print(stack.pop())
print(stack.pop())



#Implementace fronty přes cyklické pole
class Queue():
    def __init__(self,capacity):
        self._arr = [0]*(capacity+1) # rovno naalokuju kapacitu celé fronty
        self.capacity = capacity+1 # +1 kvuli zarazce
        self.start_index = 0
        self.end_index = 0
    
    def enque(self,it): # Jako push v zasobniku
        if self.is_full():
            raise Exception("Cannot push any item. Queue is full.")
        else:
            self._arr[self.end_index] = it
            self.end_index = (self.end_index+1)%self.capacity

    def deque(self): # jako pop v zásobníku ale zepredu fronty
        if self.is_empty():
            raise Exception("Cannot pop any item. Queue is empty.")
        else:
            ind = self.start_index
            self.start_index = (self.start_index+1)%self.capacity
            return self._arr[ind]


    def is_empty(self):
        return self.start_index==self.end_index

    def is_full(self):
        return (self.start_index-1)%self.capacity==self.end_index

    def print(self):
        print(self._arr)

q = Queue(5)
q.enque(1)   
q.enque(2) 
q.enque(3) 
q.enque(4) 
q.enque(5)     
# q.enque(6)    
print(q.deque())     
print(q.deque())  
print(q.deque())  
print(q.deque())  
print(q.deque())  
#print(q.deque())  
###########################################################################################################


# Uzátvorkovania - tuto funkci upravte

def skontroluj_uzavorkovani(zavorky):
    typ_chybne_zavorky = None
    #TODO: Skontroluje uzátvorkovanie. Ak je správne vypíše OK ak nie vypíše označenie prvej chybnej zátvorky

    if typ_chybne_zavorky:
        return typ_chybne_zavorky
    else:
        return 'OK'

############Testovací funkce - s touto částí nemanipulujte##################################################

class Test:
    test_id = 0
    def __init__(self,uzavorkovani,spravna_odpoved):
        self.zadani = uzavorkovani
        self.klic = spravna_odpoved
        self.id = Test.test_id
        Test.test_id+=1
    
    def evaluate(self,vysledek_testu):
        if self.klic==vysledek_testu:
            print(f'Test {self.id}: OK')
        else:
            print(f'Test {self.id}: Vaše odpověd byla {vysledek_testu} ale správná odpověď je {self.klic}')

####################################################################################################

testy = []
testy.append(Test([3, 2, 1, -1, -2, -3],'OK'))
testy.append(Test([3, 2, 1, -2, -1, -3],2))
testy.append(Test([3, 2, 1, -1, 5, 6, 7, -7, -2, -3],2))
testy.append(Test([3, 2, 1, -1, -2, 1, -1, 2, -2, 100, -100, -3],'OK'))
testy.append(Test([3, 2, 1, -1, -2, -4, -3],4))
testy.append(Test([3, 2, 1, 1, -1, -1, -2, -3],'OK'))
testy.append(Test([3, 2, 1, 1, 1, -1, -1, -3, -2, -1],3))
# Yde můžete doplnit vlastní testy zavolním testy.append(Test(posloupnost zavorek, spravna odpoved))

for test in testy:
    out = skontroluj_uzavorkovani(test.zadani)
    test.evaluate(out)







