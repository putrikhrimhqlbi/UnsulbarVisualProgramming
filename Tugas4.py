class buku :

#putri Kharimah Qalbi
    
    def __init__(self,jenis):
        self.__jenis= jenis

    def tampilkan_jenis(self):
        print(f'Jenis Buku: {self.__jenis}')

bukugambar = buku('Gambar')
bukugambar.tampilkan_jenis()
