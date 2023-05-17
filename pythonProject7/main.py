class Magaza:
    def __init__(self, magaza_adi,satici_adi,satilan_urun):
        self.__magaza_adi = magaza_adi          #private şekilde tanımlar erişilemez
        self.__satici_adi = satici_adi
        self.__satilan_urun = satilan_urun
        self.__satislar = []

    def get_magaza_adi(self):
        return self.__magaza_adi                #get ve self ile erişilebilir hale getirir

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def get_satilan_urun(self):
        return self.__satilan_urun

    def set_satilan_urun(self, satilan_urun):
        self.__satilan_urun = satilan_urun

    def satis_ekle(self, satis):
        self.__satislar.append(satis)

    def magaza_satis_tutar(self):
        toplam_satis = 0
        satici_toplam_satislari = {}    #liste oluşturulur
        for satis in self.__satislar:       #satislar listesindeki satislari taoplam_satisa ekler
            toplam_satis += satis
            if self.__satici_adi in satici_toplam_satislari:    #satici adi sözlükte var mı kontrol eder
                satici_toplam_satislari[self.__satici_adi] += satis     #varsa saticinin satışına bunu ekler
            else:
                satici_toplam_satislari[self.__satici_adi] = satis
        return toplam_satis, satici_toplam_satislari
    def __str__(self):      #toplam satışları ekrana yazdırmamızı sağlar
        toplam_satis,satici_toplam_satislari =self.magaza_satis_tutar()
        s = f"Mağaza adı: {self.__magaza_adi}\ntoplam satış tutarı: {toplam_satis}\n"
        s += "{} satıcısının satışı: {}".format(self.__satici_adi,satici_toplam_satislari[self.__satici_adi])
        return s

def main():
    sozluk ={}
    while True:
        magaza_adi = input("Mağaza adı: ")
        satici_adi = input("Satıcı adı: ")
        satilan_urun = input("Satılan ürün(tv, bilgisayar, beyaz eşya, diğer):")
        satis_tutari = float(input("Satış tutarı: "))
        if magaza_adi not in sozluk:    #magaza adı sözlükte var mı kontrol eder
            sozluk[magaza_adi] = Magaza(magaza_adi, satici_adi, satilan_urun)
        sozluk[magaza_adi].satis_ekle(satis_tutari)     #satis_ekle fonksiyonunu çağırır.
        devam = input("Devam etmek istiyor musunuz? (e/h): ")
        if devam == "h":        #döngüden çıkmamızı sağlar
            break
    for magaza_adi, magaza in sozluk.items():
        print(str(magaza))                  #ekrana yazdırma

if __name__ == "__main__":
    main()
