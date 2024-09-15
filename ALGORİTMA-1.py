S-1
-----------------------------------------------
S1=int(input("Lütfen birinci sayıyı giriniz: ")
S2=int(input("Lütfen ikinci sayıyı giriniz: ")
Toplam = S1+S2
print(Toplam)

PSEUDOCODE:
Başla
1. Birinci sayıyı kullanıcıdan al ve S1 olarak sakla
2. İkinci sayıyı kullanıcıdan al ve S2 olarak sakla
3. S1 ve S2'yi topla ve sonucu Toplam değişkeninde sakla
4. Toplam'ı ekrana yazdır
Bitir

------------------------------------------------

S-2
-------------------------------------------------
i = 0
Toplam = 0
while i <101:
  Toplam += i
  i += 1
print(Toplam)




PSEUDOCODE:
Başla
1. i'yi 0 olarak başlat
2. Toplam'ı 0 olarak başlat
3. i 101'den küçük olduğu sürece:
    a. Toplam'a i'yi ekle
    b. i'yi 1 artır
4. Toplam'ı ekrana yazdır
Bitir
--------------------------------------------------

S-3
--------------------------------------------------
while True:
  sayi = int(input("Lütfen bir sayı giriniz: "))
  if sayi > 1:
      for i in range(2, sayi):
          if (sayi % i) == 0:
              print(f"{sayi} asal sayı değildir.")
              break
      else:
          print(f"{sayi} asal sayıdır!")
          break
  else:
      print(f"{sayi} asal sayı değildir.")




PSEUDOCODE:

Başla
1. Kullanıcıdan bir sayı al ve sayi olarak sakla
2. Eğer sayi 1'den büyükse:
    a. 2'den sayi'ya kadar her i için:
        i. Eğer sayi, i'ye tam bölünüyorsa:
            1. sayi asal değildir mesajını yazdır
            2. Döngüyü kır
    b. Eğer hiçbiri tam bölünmediyse:
        i. sayi asal sayıdır mesajını yazdır
3. Eğer sayi 1'den küçük veya eşitse:
    a. sayi asal değildir mesajını yazdır
Bitir
------------------------------------------------------


S-4
-------------------------------------------------------------------------------------
elemans = []
while len(elemans) < 10:
    u_input = input("Elemans dizisine sayılar girin: ")
    if u_input.isdigit():
        number = int(u_input)
        
        if number == 0:
            break
        
        elemans.append(number)
    else:
        print("Lütfen sayısal bir değer giriniz.")

print("Girdiğiniz sayılar: ", elemans)

görülen_sayılar = set()
tekrar_eden_sayılar = set()

for i in elemans:
    if i in görülen_sayılar:
        tekrar_eden_sayılar.add(i)
    else:
        görülen_sayılar.add(i)

for sayı in tekrar_eden_sayılar:
    indeksler = [index for index, value in enumerate(elemans) if value == sayı]
    print(f"{sayı} sayısı dizide {len(indeksler)} defa geçiyor. İndeksleri: {indeksler}")

PSEUDOCODE:
Başla
1. Boş bir elemans dizisi oluştur
2. Dizinin uzunluğu 10 olana kadar:
    a. Kullanıcıdan bir sayı al
    b. Eğer sayı sayısalsa:
        i. Sayıyı elemans dizisine ekle
        ii. Eğer sayı 0 ise döngüden çık
    c. Eğer sayı sayısal değilse, kullanıcıya sayısal değer girmesini söyle
3. Girdiğin sayıları ekrana yazdır
4. Boş bir görülen_sayılar ve tekrar_eden_sayılar kümesi oluştur
5. elemans dizisindeki her sayı için:
    a. Eğer sayı görülen_sayılar kümesindeyse:
        i. Sayıyı tekrar_eden_sayılar kümesine ekle
    b. Değilse:
        i. Sayıyı görülen_sayılar kümesine ekle
6. tekrar_eden_sayılar kümesindeki her sayı için:
    a. Sayının dizide kaç kez geçtiğini ve indekslerini ekrana yazdır
Bitir
------------------------------------------------------------------------------------------
