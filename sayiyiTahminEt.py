

# PC TARAFINDAN TUTULAN SAYIYI TAHMİN EDİN

import random
sayi = random.randint(1,100)
print("1 ile 100 arasında bir tam sayı tuttum tahmin et! (6 hakkın var.): ")
for i in range(6):
    x = int(input("Tahmininiz ? --> "))
    if sayi == x :
        print("Bildiniz. Tebrikler. Tuttuğum sayı:",sayi)
        
        break
    elif sayi > x:
        print("Bilemediniz. Yukarı ")
        print("Kalan Hak: ", 5-i)
    elif sayi < x:
        print("Bilemediniz. Asağı ")
        print("Kalan Hak: ", 5-i)
if sayi!=x:
    print("Malesef Bilemediniz. :( Tuttuğum sayı:",sayi)


           
        
       
    
    
    

