class Base:
    def __init__(self, ürün_id = 0, ürün_ismi = ""):
        self.ürün_id = ürün_id
        self.ürün__ismi = ürün_ismi

    def ürün_kaydet(self):
        # Kullanıcıdan ID ve isim bilgilerini alır ve sınıfın özelliklerine atar.
        self.ürün_id = int(input('Ürün ID:'))
        self.ürün_ismi = input('Ürün İsmi:')

class Urun(Base):
    def __init__(self, ürün_fiyatı):
        super().__init__(ürün_id = 0, ürün_ismi = "", ürün_fiyatı = 0)
        self.ürün_fiyatı = ürün_fiyatı

    def ürün_kaydet(self):
        super().ürün_kaydet()
        self.ürün_fiyatı = float(input('Ürün Fiyatı: '))

    def ürün_silme(self, ürün_listesi):
        # Parametre olarak verilen ürün listesini siler.
        for i in ürün_listesi:
            print(f"{i.ürün_id} Id'si olan ismi {i.ürün_ismi}")
            
            # Silmesini istediğimiz ürünlerin id'sini alalım.
            id = int(input('Silecek İd: '))
            # Liste üzerinden gezinerek silenecek ürününü bulup kaldıralım.
            for i in ürün_listesi:
                if i.ürün_id == id:
                    ürün_listesi.remove(i)
    
    def Update(self,ürün_listesi):
        # Parametre olarak girilmiş ürün listesini görelim.
        for i in ürün_listesi:
            print(f"{i.ürün_id} olan Id 'li ürününün ismi {i.ürün_ismi}")

            #Gucelelenecek ürün idsini soralım
            id = int(input('Güncellenecek Id: '))

            #Liste üzerinde gezinerek güncellenecek ürünün isim ve fiyatını kullanıcıdan alarak ürünü günceller.
            for i in ürün_listesi:
                if i.ürün_id == id:
                    i.ürün_ismi = input('Yeni Ürün İsmi: ')
                    i.ürün_fiyatı = input('Güncel Fiyat: ')

class Kategori(Base):
    def __init__(self,ürün_tanımı = ""):
        self.ürün_tanımı = ürün_tanımı
    
    def ürün_kaydet(self):
        super().ürün_kaydet()
        self.ürün_tanımı = input('Ürün Açıklaması: ')

class Marka(Base):
    def __init__(self,ürün_markası = ""):
        self.ürün_markası = ürün_markası
    
    def ürün_kaydet(self):
        super().ürün_kaydet()
        self.ürün_markası = input('Ürün Markası: ')

# Ürün, kategori ve mrka listelerini ouşturalım.
ürünler = []
kategoriler = []
markalar = []

# Örnek bir ürün oluşturalım ve bilgilerini kullancıdan alalım.

ürün=Urun()
ürün.ürün_kaydet()
ürünler.append(ürün)
for i in ürünler:
    print(f"Ürün ID: {i.ürün_id}\nÜrün İsmi: {i.ürün_ismi}\nÜrün Fiyatı: {i.ürün_fiyatı}")

ürün.Update(ürünler)
for i in ürünler:
    print(f"Ürün ID: {i.ürün_id}\nÜrün İsmi: {i.ürün_ismi}\nÜrün Fiyatı: {i.ürün_fiyatı}")

