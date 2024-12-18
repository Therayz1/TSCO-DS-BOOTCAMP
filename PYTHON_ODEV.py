**************** SORU-1 *****************************

class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Görev eklendi: {task_name}")

    def list_tasks(self):
        if not self.tasks:
            print("Henüz görev bulunmamaktadır.")
            return

        print("\nTamamlanmamış Görevler:")
        for i, task in enumerate(self.tasks, 1):
            if not task.completed:
                print(f"{i}. {task.name}")

        print("\nTamamlanmış Görevler:")
        for i, task in enumerate(self.tasks, 1):
            if task.completed:
                print(f"{i}. {task.name}")

    def complete_task(self, task_index):
        try:
            task = self.tasks[task_index - 1]
            task.completed = True
            self.save_tasks()
            print(f"Görev tamamlandı: {task.name}")
        except IndexError:
            print("Geçersiz görev numarası.")

    def delete_task(self, task_index):
        try:
            deleted_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"Görev silindi: {deleted_task.name}")
        except IndexError:
            print("Geçersiz görev numarası.")

    def save_tasks(self):
        with open('tasks.txt', 'w') as f:
            for task in self.tasks:
                f.write(f"{task.name},{task.completed}\n")

    def load_tasks(self):
        try:
            with open('tasks.txt', 'r') as f:
                self.tasks = []
                for line in f:
                    name, completed = line.strip().split(',')
                    task = Task(name)
                    task.completed = completed == 'True'
                    self.tasks.append(task)
        except FileNotFoundError:
            self.tasks = []

def main():
    task_manager = TaskManager()

    while True:
        print("\n--- Yapılacaklar Listesi ---")
        print("1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Görevi Tamamla")
        print("4. Görevi Sil")
        print("5. Çıkış")

        secim = input("Seçiminizi yapın (1-5): ")

        if secim == '1':
            task_name = input("Görevi girin: ")
            task_manager.add_task(task_name)
        elif secim == '2':
            task_manager.list_tasks()
        elif secim == '3':
            task_manager.list_tasks()
            task_index = int(input("Tamamlamak istediğiniz görevin numarasını girin: "))
            task_manager.complete_task(task_index)
        elif secim == '4':
            task_manager.list_tasks()
            task_index = int(input("Silmek istediğiniz görevin numarasını girin: "))
            task_manager.delete_task(task_index)
        elif secim == '5':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()




******************************** SORU-2*********************************

class Kullanici:
    def __init__(self, ad, hesap_numarasi, bakiye=0):
        self.ad = ad
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = bakiye

class Banka:
    def __init__(self):
        self.kullanicilar = {}

    def hesap_ac(self, ad, hesap_numarasi, baslangic_bakiyesi=0):
        # Hesap numarası daha önce kullanılmış mı kontrolü
        if hesap_numarasi in self.kullanicilar:
            print("Bu hesap numarası zaten mevcut. Farklı bir numara seçin.")
            return None
        
        # Yeni kullanıcı oluştur
        yeni_kullanici = Kullanici(ad, hesap_numarasi, baslangic_bakiyesi)
        self.kullanicilar[hesap_numarasi] = yeni_kullanici
        print(f"{ad} adına hesap açıldı. Hesap numarası: {hesap_numarasi}")
        return yeni_kullanici

    def para_yatir(self, hesap_numarasi, miktar):
        # Hesap kontrolü
        kullanici = self.kullanicilar.get(hesap_numarasi)
        if not kullanici:
            print("Hesap bulunamadı.")
            return False
        
        # Geçerli miktar kontrolü
        if miktar <= 0:
            print("Geçersiz miktar. Pozitif bir değer girin.")
            return False
        
        # Para yatırma işlemi
        kullanici.bakiye += miktar
        print(f"{miktar} TL hesabınıza yatırıldı. Güncel bakiye: {kullanici.bakiye} TL")
        return True

    def para_cek(self, hesap_numarasi, miktar):
        # Hesap kontrolü
        kullanici = self.kullanicilar.get(hesap_numarasi)
        if not kullanici:
            print("Hesap bulunamadı.")
            return False
        
        # Bakiye kontrolü
        if miktar <= 0:
            print("Geçersiz miktar. Pozitif bir değer girin.")
            return False
        
        if miktar > kullanici.bakiye:
            print("Yetersiz bakiye. İşlem gerçekleştirilemedi.")
            return False
        
        # Para çekme işlemi
        kullanici.bakiye -= miktar
        print(f"{miktar} TL hesabınızdan çekildi. Güncel bakiye: {kullanici.bakiye} TL")
        return True

    def bakiye_sorgula(self, hesap_numarasi):
        # Hesap kontrolü
        kullanici = self.kullanicilar.get(hesap_numarasi)
        if not kullanici:
            print("Hesap bulunamadı.")
            return None
        
        print(f"{kullanici.ad} - Hesap Bakiyesi: {kullanici.bakiye} TL")
        return kullanici.bakiye

def main():
    banka = Banka()

    while True:
        print("\n--- Basit Banka Sistemi ---")
        print("1. Yeni Hesap Aç")
        print("2. Para Yatır")
        print("3. Para Çek")
        print("4. Bakiye Sorgula")
        print("5. Çıkış")

        secim = input("İşlem seçin (1-5): ")

        if secim == '1':
            ad = input("Ad Soyad: ")
            hesap_numarasi = input("Hesap Numarası: ")
            baslangic_bakiyesi = float(input("Başlangıç Bakiyesi: "))
            banka.hesap_ac(ad, hesap_numarasi, baslangic_bakiyesi)

        elif secim == '2':
            hesap_numarasi = input("Hesap Numarası: ")
            miktar = float(input("Yatırmak istediğiniz miktar: "))
            banka.para_yatir(hesap_numarasi, miktar)

        elif secim == '3':
            hesap_numarasi = input("Hesap Numarası: ")
            miktar = float(input("Çekmek istediğiniz miktar: "))
            banka.para_cek(hesap_numarasi, miktar)

        elif secim == '4':
            hesap_numarasi = input("Hesap Numarası: ")
            banka.bakiye_sorgula(hesap_numarasi)

        elif secim == '5':
            print("Bankacılık sisteminden çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()


****************************** SORU-3 **********************************************************

class Kitap:
    def __init__(self, ad, yazar):
        self.ad = ad
        self.yazar = yazar
        self.odunc_durumu = False

class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.odunc_kitaplar = []

    def kitap_ekle(self, ad, yazar):
        # Aynı kitabın daha önce eklenip eklenmediğini kontrol et
        for kitap in self.kitaplar:
            if kitap.ad == ad and kitap.yazar == yazar:
                print(f"{ad} kitabı zaten kütüphanede mevcut.")
                return None
        
        # Yeni kitap oluştur
        yeni_kitap = Kitap(ad, yazar)
        self.kitaplar.append(yeni_kitap)
        print(f"{ad} kitabı kütüphaneye eklendi.")
        return yeni_kitap

    def kitaplari_listele(self, odunc_durumu=None):
        print("\n--- Kütüphane Kitapları ---")
        
        # Filtreleme yapmadan tüm kitapları listele
        if odunc_durumu is None:
            for kitap in self.kitaplar:
                durum = "Ödünç Alınabilir" if not kitap.odunc_durumu else "Ödünç Verildi"
                print(f"Kitap: {kitap.ad} - Yazar: {kitap.yazar} - Durum: {durum}")
        
        # Ödünç durumuna göre filtrele
        else:
            filtrelenmis_kitaplar = [k for k in self.kitaplar if k.odunc_durumu == odunc_durumu]
            
            if not filtrelenmis_kitaplar:
                print(f"{'Ödünç alınabilir' if not odunc_durumu else 'Ödünç verilmiş'} kitap bulunmamaktadır.")
                return
            
            for kitap in filtrelenmis_kitaplar:
                print(f"Kitap: {kitap.ad} - Yazar: {kitap.yazar}")

    def kitap_odunc_ver(self, ad):
        # Kitap var mı kontrolü
        kitap = self.kitap_bul(ad)
        
        if not kitap:
            print(f"{ad} isimli kitap bulunamadı.")
            return False
        
        # Ödünç durumu kontrolü
        if kitap.odunc_durumu:
            print(f"{ad} kitabı zaten ödünç verilmiş.")
            return False
        
        # Ödünç verme işlemi
        kitap.odunc_durumu = True
        self.odunc_kitaplar.append(kitap)
        print(f"{ad} kitabı ödünç verildi.")
        return True

    def kitap_geri_al(self, ad):
        # Kitap var mı kontrolü
        kitap = self.kitap_bul(ad)
        
        if not kitap:
            print(f"{ad} isimli kitap bulunamadı.")
            return False
        
        # Ödünç durumu kontrolü
        if not kitap.odunc_durumu:
            print(f"{ad} kitabı zaten kütüphanede.")
            return False
        
        # Geri alma işlemi
        kitap.odunc_durumu = False
        self.odunc_kitaplar.remove(kitap)
        print(f"{ad} kitabı kütüphaneye geri alındı.")
        return True

    def kitap_bul(self, ad):
        # Adına göre kitap bulma
        for kitap in self.kitaplar:
            if kitap.ad.lower() == ad.lower():
                return kitap
        return None

def main():
    kutuphane = Kutuphane()

    while True:
        print("\n--- Kütüphane Yönetim Sistemi ---")
        print("1. Kitap Ekle")
        print("2. Tüm Kitapları Listele")
        print("3. Ödünç Alınabilir Kitapları Listele")
        print("4. Ödünç Verilmiş Kitapları Listele")
        print("5. Kitap Ödünç Ver")
        print("6. Kitap Geri Al")
        print("7. Çıkış")

        secim = input("İşlem seçin (1-7): ")

        if secim == '1':
            ad = input("Kitap adını girin: ")
            yazar = input("Yazar adını girin: ")
            kutuphane.kitap_ekle(ad, yazar)

        elif secim == '2':
            kutuphane.kitaplari_listele()

        elif secim == '3':
            kutuphane.kitaplari_listele(odunc_durumu=False)

        elif secim == '4':
            kutuphane.kitaplari_listele(odunc_durumu=True)

        elif secim == '5':
            ad = input("Ödünç vermek istediğiniz kitabın adını girin: ")
            kutuphane.kitap_odunc_ver(ad)

        elif secim == '6':
            ad = input("Geri almak istediğiniz kitabın adını girin: ")
            kutuphane.kitap_geri_al(ad)

        elif secim == '7':
            print("Kütüphane sisteminden çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()


*****************************SORU-4******************************************

class Sehir:
    def __init__(self, ad, sicaklik=0):
        self.ad = ad
        self.sicaklik = sicaklik

class HavaDurumu:
    def __init__(self):
        self.sehirler = {}

    def sehir_ekle(self, ad, sicaklik):
        # Aynı şehrin daha önce eklenip eklenmediğini kontrol et
        if ad in self.sehirler:
            print(f"{ad} zaten sistemde mevcut. Sıcaklığı güncelleyebilirsiniz.")
            return None
        
        # Yeni şehir oluştur
        yeni_sehir = Sehir(ad, sicaklik)
        self.sehirler[ad] = yeni_sehir
        print(f"{ad} şehri sisteme eklendi. Sıcaklık: {sicaklik}°C")
        return yeni_sehir

    def sicaklik_guncelle(self, ad, sicaklik):
        # Şehir var mı kontrolü
        sehir = self.sehirler.get(ad)
        if not sehir:
            print(f"{ad} şehri bulunamadı.")
            return False
        
        # Sıcaklık güncelleme
        sehir.sicaklik = sicaklik
        print(f"{ad} şehrinin sıcaklığı {sicaklik}°C olarak güncellendi.")
        return True

    def hava_durumu_sorgula(self, ad):
        # Şehir var mı kontrolü
        sehir = self.sehirler.get(ad)
        if not sehir:
            print(f"{ad} şehri bulunamadı.")
            return None
        
        # Sıcaklığa göre tavsiye
        tavsiye = self.sicaklik_tavsiyesi(sehir.sicaklik)
        print(f"{ad} şehri - Sıcaklık: {sehir.sicaklik}°C")
        print(f"Tavsiye: {tavsiye}")
        return sehir.sicaklik, tavsiye

    def sicaklik_tavsiyesi(self, sicaklik):
        # Sıcaklığa göre tavsiye verme
        if sicaklik < 0:
            return "Soğuk, sıkı giyinin."
        elif 0 <= sicaklik < 15:
            return "Serin, mont almayı unutmayın."
        else:
            return "Hava güzel, rahat giyin."

    def tum_sehirleri_listele(self):
        if not self.sehirler:
            print("Sistemde kayıtlı şehir bulunmamaktadır.")
            return

        print("\n--- Kayıtlı Şehirler ---")
        for sehir in self.sehirler.values():
            tavsiye = self.sicaklik_tavsiyesi(sehir.sicaklik)
            print(f"Şehir: {sehir.ad} - Sıcaklık: {sehir.sicaklik}°C - Tavsiye: {tavsiye}")

def main():
    hava_durumu = HavaDurumu()

    while True:
        print("\n--- Hava Durumu Uygulaması ---")
        print("1. Şehir Ekle")
        print("2. Sıcaklık Güncelle")
        print("3. Hava Durumu Sorgula")
        print("4. Tüm Şehirleri Listele")
        print("5. Çıkış")

        secim = input("İşlem seçin (1-5): ")

        if secim == '1':
            ad = input("Şehir adını girin: ")
            sicaklik = float(input("Sıcaklığı girin (°C): "))
            hava_durumu.sehir_ekle(ad, sicaklik)

        elif secim == '2':
            ad = input("Sıcaklığını güncellemek istediğiniz şehrin adını girin: ")
            sicaklik = float(input("Yeni sıcaklığı girin (°C): "))
            hava_durumu.sicaklik_guncelle(ad, sicaklik)

        elif secim == '3':
            ad = input("Hava durumunu sorgulamak istediğiniz şehrin adını girin: ")
            hava_durumu.hava_durumu_sorgula(ad)

        elif secim == '4':
            hava_durumu.tum_sehirleri_listele()

        elif secim == '5':
            print("Hava durumu uygulamasından çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()



********************************** SORU-5********************************************

class Urun:
    def __init__(self, ad, fiyat, miktar):
        self.ad = ad
        self.fiyat = fiyat
        self.miktar = miktar

    def toplam_fiyat(self):
        return self.fiyat * self.miktar

class Sepet:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, ad, fiyat, miktar):
        # Aynı üründen varsa miktarını güncelle
        for urun in self.urunler:
            if urun.ad.lower() == ad.lower():
                urun.miktar += miktar
                print(f"{ad} ürünün miktarı güncellendi. Yeni miktar: {urun.miktar}")
                return

        # Yeni ürün ekle
        yeni_urun = Urun(ad, fiyat, miktar)
        self.urunler.append(yeni_urun)
        print(f"{ad} ürünü sepete eklendi.")

    def urun_cikar(self, ad, miktar=None):
        # Ürün var mı kontrolü
        for urun in self.urunler:
            if urun.ad.lower() == ad.lower():
                # Miktar belirtilmemişse tüm ürünü çıkar
                if miktar is None or miktar >= urun.miktar:
                    self.urunler.remove(urun)
                    print(f"{ad} ürünü sepetten tamamen çıkarıldı.")
                    return True
                
                # Kısmi çıkarma
                urun.miktar -= miktar
                print(f"{ad} ürününden {miktar} adet çıkarıldı. Kalan miktar: {urun.miktar}")
                return True
        
        print(f"{ad} ürünü sepette bulunamadı.")
        return False

    def sepeti_listele(self):
        if not self.urunler:
            print("Sepet boş.")
            return

        print("\n--- Sepet İçeriği ---")
        for urun in self.urunler:
            print(f"Ürün: {urun.ad} - Birim Fiyat: {urun.fiyat} TL - Miktar: {urun.miktar} - Toplam: {urun.toplam_fiyat()} TL")

    def toplam_tutar(self):
        toplam = sum(urun.toplam_fiyat() for urun in self.urunler)
        print(f"\nSepet Toplam Tutarı: {toplam} TL")
        return toplam

def main():
    sepet = Sepet()

    while True:
        print("\n--- Alışveriş Sepeti ---")
        print("1. Ürün Ekle")
        print("2. Ürün Çıkar")
        print("3. Sepeti Listele")
        print("4. Toplam Tutarı Göster")
        print("5. Çıkış")

        secim = input("İşlem seçin (1-5): ")

        if secim == '1':
            ad = input("Ürün adını girin: ")
            fiyat = float(input("Ürün birim fiyatını girin: "))
            miktar = int(input("Ürün miktarını girin: "))
            sepet.urun_ekle(ad, fiyat, miktar)

        elif secim == '2':
            ad = input("Çıkarmak istediğiniz ürünün adını girin: ")
            miktar_secim = input("Tüm ürünü mü çıkarmak istiyorsunuz? (E/H): ").upper()
            
            if miktar_secim == 'E':
                sepet.urun_cikar(ad)
            else:
                miktar = int(input("Çıkarmak istediğiniz miktarı girin: "))
                sepet.urun_cikar(ad, miktar)

        elif secim == '3':
            sepet.sepeti_listele()

        elif secim == '4':
            sepet.toplam_tutar()

        elif secim == '5':
            print("Alışveriş sepeti uygulamasından çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()





********************************SORU-6*****************************************
import json

# Notları saklamak için bir liste
notlar = []

# Notları dosyadan yükleme
def dosyadan_yukle():
    global notlar
    try:
        with open("notlar.json", "r") as dosya:
            notlar = json.load(dosya)
    except FileNotFoundError:
        notlar = []

# Notları dosyaya kaydetme
def dosyaya_kaydet():
    with open("notlar.json", "w") as dosya:
        json.dump(notlar, dosya)

# Not ekleme
def not_ekle():
    baslik = input("Not başlığı: ")
    icerik = input("Not içeriği: ")
    notlar.append({"baslik": baslik, "icerik": icerik})
    dosyaya_kaydet()
    print("Not eklendi.")

# Notları listeleme
def notlari_listele():
    if not notlar:
        print("Hiç not yok.")
        return
    for i, not_ in enumerate(notlar):
        print(f"{i + 1}. {not_['baslik']}")

# Not düzenleme
def not_duzenle():
    notlari_listele()
    secim = int(input("Düzenlemek istediğiniz notun numarasını seçin: ")) - 1
    if 0 <= secim < len(notlar):
        notlar[secim]['baslik'] = input("Yeni başlık: ")
        notlar[secim]['icerik'] = input("Yeni içerik: ")
        dosyaya_kaydet()
        print("Not düzenlendi.")
    else:
        print("Geçersiz seçim.")

# Not silme
def not_sil():
    notlari_listele()
    secim = int(input("Silmek istediğiniz notun numarasını seçin: ")) - 1
    if 0 <= secim < len(notlar):
        notlar.pop(secim)
        dosyaya_kaydet()
        print("Not silindi.")
    else:
        print("Geçersiz seçim.")

# Menü
def menu():
    dosyadan_yukle()
    while True:
        print("\n1. Not Ekle\n2. Notları Listele\n3. Not Düzenle\n4. Not Sil\n5. Çıkış")
        secim = input("Bir seçenek seçin: ")
        if secim == "1":
            not_ekle()
        elif secim == "2":
            notlari_listele()
        elif secim == "3":
            not_duzenle()
        elif secim == "4":
            not_sil()
        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.")

menu()





***************************************SORU-7************************************************

  film_listesi = []

# Film ekleme
def film_ekle():
    isim = input("Film adı: ")
    yil = input("Yayın yılı: ")
    tur = input("Film türü: ")
    film_listesi.append({"isim": isim, "yil": yil, "tur": tur})
    print("Film eklendi.")

# Filmleri listeleme
def filmleri_listele():
    if not film_listesi:
        print("Film listesi boş.")
        return
    for i, film in enumerate(film_listesi):
        print(f"{i + 1}. {film['isim']} ({film['yil']}) - Tür: {film['tur']}")

# Film düzenleme
def film_duzenle():
    filmleri_listele()
    secim = int(input("Düzenlemek istediğiniz filmin numarasını seçin: ")) - 1
    if 0 <= secim < len(film_listesi):
        film_listesi[secim]['isim'] = input("Yeni film adı: ")
        film_listesi[secim]['yil'] = input("Yeni yayın yılı: ")
        film_listesi[secim]['tur'] = input("Yeni tür: ")
        print("Film düzenlendi.")
    else:
        print("Geçersiz seçim.")

# Film silme
def film_sil():
    filmleri_listele()
    secim = int(input("Silmek istediğiniz filmin numarasını seçin: ")) - 1
    if 0 <= secim < len(film_listesi):
        film_listesi.pop(secim)
        print("Film silindi.")
    else:
        print("Geçersiz seçim.")

# Film arama
def film_ara():
    arama = input("Aramak istediğiniz film adı: ").lower()
    bulunanlar = [film for film in film_listesi if arama in film['isim'].lower()]
    if bulunanlar:
        for film in bulunanlar:
            print(f"{film['isim']} ({film['yil']}) - Tür: {film['tur']}")
    else:
        print("Film bulunamadı.")

# Menü
def menu():
    while True:
        print("\n1. Film Ekle\n2. Filmleri Listele\n3. Film Düzenle\n4. Film Sil\n5. Film Ara\n6. Çıkış")
        secim = input("Bir seçenek seçin: ")
        if secim == "1":
            film_ekle()
        elif secim == "2":
            filmleri_listele()
        elif secim == "3":
            film_duzenle()
        elif secim == "4":
            film_sil()
        elif secim == "5":
            film_ara()
        elif secim == "6":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.")

menu()

