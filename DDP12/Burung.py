from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
    def cetak_Burung(self):
        super().cetak()
        print("Jenis \t\t\t: ", self.jenis,
              "\nBunyi \t\t\t: ", self.bunyi)
love_Bird = Burung("Love Bird", "Sayuran", "Udara", "Bertelur", "Misty", "Kicauan")
love_Bird.cetak_Burung()

Kolibri = Burung("Kolibri", "Nektar", "Udara", "Bertelur", "Spatuletail", "Kicauan")
Kolibri.cetak_Burung()

cendrawasih = Burung("Cendrawasih", "Serangga", "Udara", "Bertelur", "Cendrawasih Biru", "Mencicit")
cendrawasih.cetak_Burung()
