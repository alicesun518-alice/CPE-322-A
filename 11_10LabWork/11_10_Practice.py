def hello():
    print("Hello World")
hello()

def show(a, b, c):
    print(a, b, c)
show(1, 2, 3)         
show(c=3, a=1, b=2)     

def pack_cats(*cats):
    print("Cats:", cats)
pack_cats('kat', 'niki', 'max')

def pack_dogs(**dogs):
    print("Dogs:", dogs)
pack_dogs(spot=3, rex=5, loki=2)

def mix_animals(a, b, *cats, **dogs):
    print("a,b:", a, b)
    print("Cats:", cats)
    print("Dogs:", dogs)
mix_animals('tom', 'max', 'niki', 'persian', rex=4, buddy=1)

