class Mobil :
    def __init__(self,merk,warna,CC):
        self.__merk = merk      # private attribute
        self.warna = warna      # public attribute
        self.CC = CC            # public attribute

    def tampilkan_merk(self):
        print(f'Merk : {self.__merk}')      # Cara Mengakses attribute private

jip = Mobil('jeep','hitam',3000)
jip.tampilkan_merk()    # Sehingga attribute private bisa ditampilkan

print(jip.warna)
print(jip.CC)