# Refresh Python Knowledge

# Part 1

1. Create sebuah python script bernama `hello_world.py` untuk print ke layar/terminal `hello world!`
```bash
$ python3 hello_world.py
> hello world!
```

2. Create sebuah python script bernama `loop.py` yang akan print `0 1 2 3 4 5`
```bash
$ python3 loop.py
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

4. Create sebuah script `loop2.py` berisikan sebuah loop 5 kali iterasi, dimana `a` akan bertambah `1` di setiap iterasi loop
```bash
$ python3 loop2.py
> eg. a = 4
> a = 5 # loop 1
> a = 6 # loop 2
> a = 7 # loop 3
> a = 8 # loop 4
> a = 9 # loop 5
```

5. Create sebuah script `loop3.py`, yang akan looping sebanyak 2 kali, dimana di dalam setiap loop, akan ada loop 2 kali lagis. Pada **LOOP PERTAMA** `a` akan bertambah `1`, di dalam **LOOP KEDUA** `b` akan bertambah `1`. Setiap iterasi loop paling dalam, akan menambahkan antara bilangan `a & b`
```bash
$ python3 loop3.py
> 0
> 1
> 2
> 3
> 4
> 1
> 2
> 3
> 4
> 5
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
def tambah(a, b):
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

Di contoh di atas, ada juga yang kita sebut `comparison operator` (di contoh di atas operator `==` -> cek sama dengan. Bedakan dengan `=` -> ini assignment operator)

| Operator | Name                     | Example |
| -------- | ------------------------ | ------- |
| ==       | Equal 	                  | x == y  | 	
| !=       | Not equal                | x != y  |	
| >        | Greater than             | x > y   |	
| <        | Less than 	              | x < y   |
| >=       | Greater than or equal to | x >= y  |	
| <=       | Less than or equal to    | x <= y  |

Selain itu juga ada operasi matematik di python
| Operator | Name                     | Example |
| -------- | ------------------------ | ------- |
| +       | tambah 	                  | 5 + 3 = 8  | 	
| -      | kurang             | 5 - 3 = 2  |
| / | bagi | 5 / 2 = 2.5 |
| % | modulus | 5 % 2 = 1|
| * | kali | 2 * 3 = 6 |
| ** | pangkat | 2**2 = 4 |

8. Create sebuah script bernama `even_odd.py` yang mengecek apakah sebuah bilangan merupakan bilangan ganjil atau genap
```bash
$ python3 even_odd.py
def even_odd(a):
    if ...:
        print("ganjil")
    else:
        print("genap")
> a = 5
> ganjil
> a = 4
> genap
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
# cek bagian boolean, karena kita pakai value boolean (True,False) di sini
while <BLANK>:
    # DO SOMETHING HERE
```

JAWABAN:
```
while True:
    print("HELLO!")
```

sekarang buat jika setiap iterasi while, ada variable `a` yang akan bertambah `1` setiap iterasi,
bagaimana cara cek agar angka `a` tidak melebihi `10`?
```python
def cek_sampai_sepuluh(a):
    while ...:
        print(a)
    print("beres")

a = 1
cek_sampai_sepuluh(a)

> 1
> 2
> 3
> ...
> 10
> beres
```

Di python juga ada built-in function `input()` untuk menangkap input data dari terminal.

Coba buat sebuah script `input.py`, di mana user akan input x & y
```python
x: int = float(input("masukkan x: "))
print(x)
y: int = float(input("masukkan y: "))
print(y)
z: int = x + y
print(z)

> masukkan x: 5
> masukkan y: 10
> 15
```

10. Buat script `incrementwhile.py` yang akan print `hello` sebanyak `10x` menggunakan `while loop`
HINT:
```
i = 0
i += 1 # i akan bertambah 1. 

eg. 
i = 0
i += 1
# i = 1
```

11. Coba buat sebuah script yang menanyakan pertanyaan berikut. Kalau salah, tanya lagi
```
"Apakah beruang merupakan binatang: jawab: yes | no "

kalau benar:
print("benar!")
kemudian exit

kalau salah:
print("salah, coba lagi")
```

HINT:
1. gunakan `while loop`
2. gunakan `input()`
3. gunakan `conditional ==`