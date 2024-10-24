import random

x = random(6,9)
inp = int(input("tebak angka x (antara 6-9)"))

while True:
    if inp == x:
        print("benar!")
        break
    else:
        print("salah, coba lagi!")