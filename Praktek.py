class Toko():
    def __init__(self,nama, jenis, alamat):
        self.nama = nama
        self.jenis = jenis
        self.alamat = alamat

    def cek_id_toko(self):
        print('nama:',self.nama,'\njenis:',self.jenis,'\nalamat:',self.alamat)

class Tokoped(Toko):
    pass
    

toko1 = Toko('Hp','Gadget','Majene')
toko2 = Toko('Kayu','Meja','Polewali')
toko1.cek_id_toko()
toko2.cek_id_toko()

