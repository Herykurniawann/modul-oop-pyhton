class Mobil :
    def __init__(self,merk,warna,CC):
        self.__merk = merk      # private attribute
        self.warna = warna      # public attribute
        self.CC = CC            # public attribute

jip = Mobil('jip','hitam',3000)

print(jip.merk)
print(jip.warna)
print(jip.CC)