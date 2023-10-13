class SegiEmpat():
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        print("Luas Segi Empat = ", self.panjang * self.lebar ,"M^2")


class BujurSangkar(SegiEmpat):
    def __init__(self,sisi):
        self.side = sisi
        SegiEmpat.__init__(self,sisi,sisi)

    def hitung_luas(self):
        print("Luas Bujur Sangkar = ", self.side * self.side, "M^2")


b = BujurSangkar(4)
s = SegiEmpat(2,4)
b.hitung_luas()
s.hitung_luas()
