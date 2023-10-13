class UTY(object):
    def __init__(self,status,nama,prodi):
        self.nama = nama
        self.status = status
        self.prodi = prodi
    def semangat(self):
        print('Indonesia Maju Indonesia Tumbuh UTY Hebat')
    def info(self):
        print('-- INFORMASI --')
        print('Nama             :'+self.nama)
        print('Status           :'+self.status)
        print('Program Studi    :'+self.prodi)


class Dosen(UTY):
    def __init__(self,status,nama,prodi,nip):
        super().__init__(status,nama,prodi)
        self.nip = nip
    def semangatDosen(self):
        self.semangat()
        print('Dosen UTY Bermartabat')
    def infoDosen(self):
        print('NIP              :'+self.nip)