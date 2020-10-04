class Foo:

    def bar(self,x,y,slova=False,a=True,b=False):
        if slova:
            return x.find(y)
        else:
            return x*10+y




 



f = Foo()
print(f.bar(5,4))
print(f.bar('programko','gram',False))

class Genome:
    def create_from_genome(self):
        # return Person with genotype
        pass

    def combine_genes(self,genes):
        g = []
        for gene in genes:
            g=g+gene

class Person:
    def __init__(self,x):
        if isinstance(x,Genome):
            self.features = x.create_from_genome()
        elif isinstance(x,str):
            self.name = x

class Person2:
    def __init__(self,*args,**kwargs):
        self.name = kwargs.get('name','Nobody')

def vypis(*args,**kwargs):
    word=''
    for i in args:
        word+=i
        print(word)
    if kwargs['meno']:
        x = kwargs['meno']
        print(f'Meno:{x}')
    for i in kwargs.items():
        print(i)

vypis('ahoj','ludia',meno='Peter',priezvisko='Kovacs')
