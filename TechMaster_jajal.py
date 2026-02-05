from abc import ABC, abstractmethod

# ================== ABSTRACT CLASS ==================
class BarangElektronik(ABC):
    def __init__(self, nama, harga):
        self.nama = nama
        self.__harga = harga
        self.__stok = 0

    # ---------- ENCAPSULATION ----------
    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    def _harga(self):
        return self.__harga

    # ---------- ABSTRACTION ----------
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_total(self, jumlah):
        pass


# ================== LAPTOP ==================
class Laptop(BarangElektronik):
    def __init__(self, nama, harga, processor):
        super().__init__(nama, harga)
        self.processor = processor

    def tampilkan_detail(self):
        pajak = self._harga() * 0.10
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f" Harga: Rp {self._harga():,} | Pajak(10%): Rp {int(pajak):,}")

    def hitung_total(self, jumlah):
        return (self._harga() * 1.10) * jumlah


# ================== SMARTPHONE ==================
class Smartphone(BarangElektronik):
    def __init__(self, nama, harga, kamera):
        super().__init__(nama, harga)
        self.kamera = kamera

    def tampilkan_detail(self):
        pajak = self._harga() * 0.05
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f" Harga: Rp {self._harga():,} | Pajak(5%): Rp {int(pajak):,}")

    def hitung_total(self, jumlah):
        return (self._harga() * 1.05) * jumlah


# ================== TRANSAKSI ==================
def proses_transaksi(keranjang):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0
    for i, (barang, qty) in enumerate(keranjang, start=1):
        print(f"{i}. ", end="")
        barang.tampilkan_detail()
        subtotal = barang.hitung_total(qty)
        print(f" Beli: {qty} unit | Subtotal: Rp {int(subtotal):,}")
        total += subtotal
    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total):,}")
    print("----------------------------------------")


# ================== ALUR PROGRAM ==================
print("--- SETUP DATA ---")
laptop = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
hp = Smartphone("iPhone 13", 15_000_000, "12MP")

laptop.tambah_stok(10)
hp.tambah_stok(-5)
hp.tambah_stok(20)

keranjang = [
    (laptop, 2),
    (hp, 1)
]

proses_transaksi(keranjang)
