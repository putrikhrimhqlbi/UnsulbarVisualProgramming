class handphone:
    def __init__(self, inputmerek, inputjumlah, inputharga):
        
        self.merek = inputmerek
        self.jumlah = inputjumlah
        self.harga = inputharga


hp1 = handphone("xiomi",10, 2000000)
hp2 = handphone("vivo",15, 3000000)

print (hp1.harga)
