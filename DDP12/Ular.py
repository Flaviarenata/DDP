from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, corak, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.corak = corak
        self.racun = racun

    def cetak_Ular(self):
        super().cetak()
        print("Corak \t\t\t: ", self.corak,
              "\nRacun \t\t\t: ", self.racun)
        
anaconda = Ular("Anaconda", "Rusa", "Amazon", "Bertelur", "Tutul Hitam", "Tidak Berbisa")
anaconda.cetak_Ular()

sanca = Ular("Sanca", "Ayam", "Tropis", "Bertelur", "Bercak Hitam", "Tidak Berbisa")
sanca.cetak_Ular()

cabi = Ular("Cabai", "Kadal kecil", "Hutan Lembab", "Bertelur", "Bergaris Merah", "Berbisa")
sanca.cetak_Ular()