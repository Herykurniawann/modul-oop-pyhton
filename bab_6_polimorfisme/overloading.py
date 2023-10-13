class Pegawai:
    def __init__(self,nama,gaji):
        self.nama = nama
        self.gaji = gaji
        Pegawai.jumlah += 1

    def tampilJumlah(self):
        print("Total Pegawai :",Pegawai.jumlah)

    def tampilPegawai(self):
        print("Nama :",self.nama , ", Gaji :",self.gaji)


    # Overloading
    def tunjangan(self, istri = None, anak = None):
        if anak != None and istri != None:
            total = anak + istri
            print("Tunjangan anak + istri :",total)
        else:
            total = istri
            print("Tunjangan istri :",total)


# Memanggil Class
peg1 = Pegawai("Riyanto",2000)
peg2 = Pegawai("Aria Anggara",5000)
peg1.tampilPegawai()
peg2.tampilPegawai()
peg1.tunjangan(2500,2000)
peg2.tunjangan(2500)

print("Total Pegawai %d" % Pegawai.jumlah)
rataGaji = (peg1.gaji + peg2.gaji) / Pegawai.jumlah
print("Rata-rata Gaji :"+ str(rataGaji))



