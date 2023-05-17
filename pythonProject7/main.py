class Magaza:
    def __init__(self, magaza_adi, satilan_urun,satici_adi):
        self.__magaza_adi = magaza_adi
        self.__satilan_urun = satilan_urun
        self.__satici_adi = satici_adi
        self.__satislar = {}

    def get_magaza_adi(self):
        return self.__magaza_adi

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_satilan_urun(self):
        return self.__satilan_urun

    def set_satilan_urun(self, satilan_urun):
        self.__satilan_urun = satilan_urun

    def get_satici_adi(self):
            return self.__satici_adi

    def set_satici_adi(self, satici_adi):
            self.__satici_adi = satici_adi

    def satis_ekle(self, satici_adi, satis_tutari):
        if satici_adi in self.__satislar:
            self.__satislar[satici_adi] += satis_tutari
        else:
            self.__satislar[satici_adi] = satis_tutari

    def magaza_satis_tutar(self):
        toplam_satis = sum(self.__satislar.values())
        return toplam_satis, self.__satislar

    def __str__(self):
        toplam_satis, satici_toplam_satislari = self.magaza_satis_tutar()
        s = f"Mağaza adı: {self.__magaza_adi}\nToplam satış tutarı: {toplam_satis}\n"
        for satici, satis in satici_toplam_satislari.items():
            s += f"{satici} satıcısının satışı: {satis}\n"
        return s
    
def main():
    sozluk = {}
    while True:
        magaza_adi = input("Mağaza adı: ")
        satilan_urun = input("Satılan ürün (tv, bilgisayar, beyaz eşya, diğer): ")
        satici_adi = input("Satıcı adı: ")
        satis_tutari = float(input("Satış tutarı: "))

        if magaza_adi not in sozluk:
            sozluk[magaza_adi] = Magaza(magaza_adi, satilan_urun,satici_adi)
        sozluk[magaza_adi].satis_ekle(satici_adi, satis_tutari)
        devam = input("Devam etmek istiyor musunuz? (e/h): ")
        if devam.lower() == "h":
            break

    for magaza_adi, magaza in sozluk.items():
        print(str(magaza))


if __name__ == "__main__":
    main()
