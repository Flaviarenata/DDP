from Animal import *

class Kucing(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, Negara_asal, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.Negara_asal = Negara_asal
        self.warna = warna
    def cetak_Kucing(self):
        super().cetak()
        print("Negara Asal\t\t: ", self.Negara_asal,
              "\nWarna \t\t\t: ", self.warna)
Persia = Kucing("Persia", "Pur", "Darat", "Melahirkan", "Iran", "Coklat kekuningan")
Persia.cetak_Kucing()

Siberia = Kucing("Siberia", "Pur", "Darat", "Melahirkan", "Rusia", "Cream & Hitam")
Siberia.cetak_Kucing()

Scottish_Fold = Kucing("Scottish Fold", "Pur", "Darat", "Melahirkan", "Skotlandia", "Putih,Abu & Cream")
Scottish_Fold.cetak_Kucing()
