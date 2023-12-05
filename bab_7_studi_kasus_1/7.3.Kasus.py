class Kalkulator: #
    def __init__(self,x,y): #ini disrbut class constructor
        self.A = x #argument x dijadikan atribut A
        self.B = y #argument y dijadikan atribut B
        print("A="+str(x)+",B="+str(y))

    def tambah(self): # class method tambah
        self.hasil = self.A + self.B
        print("A+B="+str(self.hasil))

    def kurang(self): # class method kurang
        self.hasil = self.A - self.B
        print("A-B="+str(self.hasil))

    def kali(self): # class method kali
        self.hasil = self.A * self.B
        print("A*B="+str(self.hasil))

    def bagi(self): # class method bagi
        if self.B == 0: #antisipasi
            print("Pembagian dengan nol")
        else:
            self.hasil = self.A / self.B
            print("A/B="+str(self.hasil))


# Membuat object pertama
object1 = Kalkulator(1,2) #membuat object sebagai representasi class kalkulator
object1.tambah() #menggunakan class method tambah
object1.kurang() #menggunakan class method kurang
object1.kali() #menggunakan class method kali
object1.bagi() #menggunakan class method bagi

# Membuat object kedua
object2 = Kalkulator(2,0) #membuat object sebagai representasi class kalkulator
object2.bagi() #menggunakan class method bagi2