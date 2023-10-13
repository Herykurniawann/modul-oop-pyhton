class Gaji:
    def __init__(self, gaji_bulanan):
        self.gaji_bulanan = gaji_bulanan

    def total(self):
        return (self.gaji_bulanan * 12)

class Pegawai:
    def __init__(self,gaji_bulanan,bonus):
        self.gaji_bulanan = gaji_bulanan
        self.bonus = bonus
        self.obj_gaji = Gaji(self.gaji_bulanan)

    def hasil_tahunan(self):
        return "Total : " + str(self.obj_gaji.total() + self.bonus) + " Rupiah"

obj_pegawai = Pegawai(2600,500)
print(obj_pegawai.hasil_tahunan())
