class TiketBioskop:
    def __init__(self):
        self.daftar_film = {
            "1": {"judul": "SI DULL", "harga": 25000},
            "2": {"judul": "THE BEEKEEPER", "harga": 25000},
            "3": {"judul": "FILM DINOSAURUS: Dominion", "harga": 30000},
            "4": {"judul": "FILM YANG BELUM TAYANG", "harga": 20000}
        }

    def tampilkan_daftar_film(self):
        print("Daftar Film:")
        print("-------------------------------------------------")
        for kode, film in self.daftar_film.items():
            print(f"{kode}. {film['judul']} - Rp{film['harga']}")
        print("-------------------------------------------------")

    def pesan_tiket(self):
        self.tampilkan_daftar_film()
        kode_film = input("Pilih film (masukkan kode film): ")
        jumlah_tiket = int(input("Masukkan jumlah tiket: "))

        if kode_film in self.daftar_film:
            harga_tiket = self.daftar_film[kode_film]['harga']
            total_harga = harga_tiket * jumlah_tiket
            print(f"\nAnda memesan {jumlah_tiket} tiket untuk film {self.daftar_film[kode_film]['judul']}.")
            print(f"Total harga yang harus dibayar: Rp{total_harga}")
        else:
            print("Kode film tidak valid.")

if __name__ == "__main__":
    tiket_bioskop = TiketBioskop()
    tiket_bioskop.pesan_tiket()
