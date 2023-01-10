# KULLANICI TARAFINDAN TUTULAN SAYIYI TAHMİN ETME 

import random
input("Tahmin etmem için 1 ve 100 arasında bir sayı tutun ve başlamak için 'Enter' basın, 7 hakkım var. ")
tahmin = 50
ustsinir = 101
altsinir = 0
kalanhak = [1,2,3,4,5,6]
x = 6
for i in kalanhak:
    print("Tuttuğunuz sayı -->",tahmin,"<-- ? Doğru için (d), Aşağı için (a), Yukarı için (y)")
    print("kalan hak:",x)
    cevap = input("Giriniz ==> d / a / y ?: ")
    if cevap=="y" or cevap=="a" or cevap=="d":
                
        if cevap=="d":
            if i==5:
                print("Nasıl bildim demi ? Hemde 2 hakkım daha vardı.")
            elif i==4:
                print("Oo daha 3 hakkım varmış, şans değil bu arada.")
            elif i==3:
                print("Çok kolaysın ya bir daha sor.")
            elif i==1:
                print("One Shot One Kill!")
            elif i==2:
                print("Vallahamı!! Ben hemmen piyango bileti almaya gidiyorum görüşürüüz.. :)")
            else:
                print("Bildim sonunda :)")
            break
        elif cevap=="y":
            altsinir=tahmin 
            tahmin= int(((ustsinir-altsinir)/2)+tahmin)        
        elif cevap=="a":              
            ustsinir=tahmin        
            tahmin= int(tahmin-((ustsinir-altsinir)/2))
        if i==6:
            print(tahmin,"!!!!")        
            cevap = print("Tutuğun sayı kesinlikle: -->",tahmin,"<-- bilemeyeceğim sandın ama yanıldın, bu arada yalan soylemek yok ha!")
            break  
        x -= 1
    else:
        print("HATALI GİRİŞ!! Sana d / a / y den birisini gir diyorum sen gidip",cevap,"giriyorsun daha nasıl anlatayım?")
        kalanhak.insert(i,i)
        
        
        
        
        