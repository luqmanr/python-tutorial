# Refresh Python Knowledge

# Part 1

1. Create sebuah python script bernama `hello_world.py` untuk print ke layar/terminal `hello world!`
```bash
$ python3 hello_world.py
> hello world!
```

2. Create sebuah python script bernama `loop.py` yang akan print `0 1 2 3 4 5`
```bash
$ python3 1to5.py
> 0
> 1
> 2
> 3
> 4
> 5
```
HINT:
```
for <VARIABLE> in range(<INSERT NUMBER HERE>):
    # DO SOMETHING HERE
```

3.a. Create sebuah script `sum.py` yang berisikan variable `a`, `b`, & `c` dimana `c = a + b`. Kemudian print value dari variable `a,b,c`
```bash
$ python3 sum.py
> a = 5
> b = 6
> c = 11
```
HINT:
```
fungsi print() bisa menerima beberapa parameter sekaligus

contoh:
print("a =", a)  # print 2 parameter sekaligus
print("b = ", b) # print 2 parameter sekaligus
print("c = ", c) # print 2 parameter sekaligus
```

4. Create sebuah script `loop2.py` berisikan sebuah loop 5 kali iterasi, yang akan menambahkan bilangan antara `a & b`, dimana `a` akan bertambah `1` di setiap iterasi loop
```bash
$ python3 loop2.py
> eg. b = 4
> c = 4
> c = 5
> c = 6
> c = 7
> ...
```

5. Create sebuah script `loop3.py`, yang berisikan sebuah 5xloop di dalam 5xloop, dimana di **LOOP PERTAMA** `a` akan bertambah `1`, di dalam **LOOP KEDUA** `b` akan bertambah `1`. Setiap iterasi loop akan menambahkan antara bilangan `a & b`
```bash
$ python3 loop3.py
> c = 0
> c = 1
> c = 2
> c = 3
> c = 4
> c = 1
> c = 2
> c = 3
> c = 4
> c = 5
> ...
> c = 8
```

6. Create sebuah script bernama `hello.py` berisikan function bernama `hello_world()`, yang akan print `HELLO WORLD`
```bash
$ python3 hello.py 
> HELLO WORLD
```
HINT:
```
def <FUNCTION NAME>:
    # DO SOMETHING HERE
```

7. Create script `nambah.py`, yang ada definisi function `tambah(a, b)`. Dimana `a & b` adalah sebuah bilangan. Kemudian kembalikan hasil `a + b` dari fungsi tersebut
```bash
$ python3 nambah.py
> eg. a = 20 , b = 10
> c = 30
```
HINT:
```
def nambah(a, b):
    # z = a + b
    # kembalikan z
    return <KEMBALIKAN SESUATU>
```

# Part 2

Dalam python juga kita bisa cek sebuah kondisi menggunakan program. Kita bisa mengecek sebuah kondisi di python menggunakan ekspresi `if` `elif` dan `else`
contoh:
```
if x == 5:
    print("x adalah 5")
elif x == 1:
    print("x adalah 1")
else:
    print("x bukan 5 bukan 1")
```

Di contoh di atas, ada juga yang kita sebut `comparison operator` (di contoh di atas operator `==` -> cek sama dengan)

| Operator | Name                     | Example |
| -------- | ------------------------ | ------- |
| ==       | Equal 	                  | x == y  | 	
| !=       | Not equal                | x != y  |	
| >        | Greater than             | x > y   |	
| <        | Less than 	              | x < y   |
| >=       | Greater than or equal to | x >= y  |	
| <=       | Less than or equal to    | x <= y  |

8. Create sebuah script bernama `even_odd.py` yang mengecek apakah sebuah bilangan merupakan bilangan ganjil atau genap
```bash
$ python3 even_odd.py
```

6. Create sebuah script `bool.py` yang menyimpan value `boolean`, kemudian print value tersebut
```bash
$ python3 bool.py
> True
```

HINT:
```
boolean adalah tipe data yang hanya punya 2 values, Benar & Salah, True & False
```

9. Create sebuah script bernama `while.py` yang akan print `Hello!` selamanya jika tidak distop
```bash
$ python3 while.py
> Hello!
> Hello!
> Hello!
> Hello!
> Hello!
> Hello!
> Hello!
> 
> ...
> Hello!
$ Ctrl+C
```
HINT:
```
# cek nomor 5, karena kita pakai value boolean (True,False) di sini
while <BLANK>:
    # DO SOMETHING HERE
```
