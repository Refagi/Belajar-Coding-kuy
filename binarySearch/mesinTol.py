# class MesinTol:
#     def __init__(self, username, saldo):
#         self.username = username
#         self.saldo = saldo

#     def tambah_saldo(self, jumlah):
#         self.saldo += jumlah
#         print(f"Saldo berhasil ditambahkan. Saldo sekarang: Rp {self.saldo}")

#     def tol_masuk(self, gerbang_tol, golongan_kendaraan):
#         tarif_golongan = [5000, 8000, 10000, 15000, 20000]
#         tarif = tarif_golongan[golongan_kendaraan - 1]
#         if self.saldo >= tarif:
#             self.saldo -= tarif
#             print(f"Selamat datang, {self.username}! Anda memasuki gerbang tol {gerbang_tol}. Saldo terpotong: Rp {tarif}. Saldo sekarang: Rp {self.saldo}")
#         else:
#             print("Saldo tidak mencukupi. Mohon isi ulang saldo terlebih dahulu.")

# # Input user name dan saldo awal
# print("Selamat datang di Mesin Tol Otomatis Tangerang-Merak")
# username = input("Masukkan username: ")
# saldo_awal = int(input("Masukkan saldo awal (Rp): "))
# mesin_tol = MesinTol(username, saldo_awal)

# # Menu utama
# while True:
#     # print("Selamat datang di Mesin Tol Otomatis Tangerang-Merak")
#     print("1. Tambah Saldo")
#     print("2. Masuk Tol")
#     print("3. Keluar")
    
#     pilihan = input("Silakan pilih menu (1/2/3): ")

#     if pilihan == "1":
#         jumlah_saldo = int(input("Masukkan jumlah saldo yang ingin ditambahkan (Rp): "))
#         mesin_tol.tambah_saldo(jumlah_saldo)
#     elif pilihan == "2":
#         gerbang_tol = input("Masukkan nama gerbang tol: ")
#         print("Golongan Kendaraan:")
#         print("1. Golongan 1 (motor)")
#         print("2. Golongan 2 (mobil)")
#         print("3. Golongan 3 (bus kecil/truk kecil)")
#         print("4. Golongan 4 (bus besar/truk besar)")
#         print("5. Golongan 5 (truk besar dengan trailer)")
#         golongan = int(input("Pilih golongan kendaraan (1/2/3/4/5): "))
#         mesin_tol.tol_masuk(gerbang_tol, golongan)
#     elif pilihan == "3":
#         print("Terima kasih. Sampai jumpa lagi!")
#         break
#     else:
#         print("Pilihan tidak valid. Silakan pilih menu yang benar.")



class MesinTol:
    def __init__(self, username, saldo):
        self.username = username
        self.saldo = saldo

    def tambah_saldo(self, jumlah):
        self.saldo += jumlah
        print(f"Saldo berhasil ditambahkan. Saldo sekarang: Rp {self.saldo}")

    def tol_masuk_tunai(self, gerbang_tol, golongan_kendaraan):
        tarif_golongan = [5000, 8000, 10000, 15000, 20000]
        jarak_tol = {
            "cikupa": 5,
            "balaraja timur": 10,
            "balaraja barat": 15,
            "cikande": 20,
            "ciujung": 25,
            "serang timur": 30,
            "serang barat": 35,
            "cilegon timur": 40,
            "cilegon barat": 45,
            "merak": 50
        }

        jarak = jarak_tol.get(gerbang_tol.lower(), -1)

        if jarak != -1:
            tarif = tarif_golongan[golongan_kendaraan - 1] * jarak
            if self.saldo >= tarif:
                self.saldo -= tarif
                print(f"Selamat datang, {self.username}! Anda memasuki gerbang tol {gerbang_tol}. Saldo terpotong: Rp {tarif}. Saldo sekarang: Rp {self.saldo}")
            else:
                print("Saldo tidak mencukupi. Mohon isi ulang saldo terlebih dahulu.")
        else:
            print("Gerbang tol salah. Mohon pilih gerbang tol yang benar.")

    def tol_masuk_non_tunai(self, gerbang_tol, golongan_kendaraan):
        tarif_golongan = [5000, 8000, 10000, 15000, 20000]
        jarak_tol = {
            "cikupa": 5,
            "balaraja timur": 10,
            "balaraja barat": 15,
            "cikande": 20,
            "ciujung": 25,
            "serang timur": 30,
            "serang barat": 35,
            "cilegon timur": 40,
            "cilegon barat": 45,
            "merak": 50
        }

        jarak = jarak_tol.get(gerbang_tol.lower(), -1)

        if jarak != -1:
            tarif = tarif_golongan[golongan_kendaraan - 1] * jarak
            return tarif
        else:
            return -1

# Input user name dan saldo awal
print("   Selamat Datang Di Pembayaran Tol Tangerang - Merak   ")
print("========================================================")
username = input("Masukkan username: ")
saldo_awal = int(input("Masukkan saldo awal (Rp): "))
mesin_tol = MesinTol(username, saldo_awal)

# Menu utama
while True:
    print("Selamat datang di Mesin Tol Otomatis Tangerang - Merak")
    print("1. Tambah Saldo")
    print("2. Masuk Tol Tunai")
    print("3. Masuk Tol Non Tunai")
    print("4. Keluar")

    pilihan = input("Silakan pilih menu (1/2/3/4): ")

    if pilihan == "1":
        jumlah_saldo = int(input("Masukkan jumlah saldo yang ingin ditambahkan (Rp): "))
        mesin_tol.tambah_saldo(jumlah_saldo)
    elif pilihan == "2":
        gerbang_tol = input("Masukkan nama gerbang tol: ")
        print("Golongan Kendaraan:")
        print("1. Golongan 1 (motor)")
        print("2. Golongan 2 (mobil)")
        print("3. Golongan 3 (bus kecil/truk kecil)")
        print("4. Golongan 4 (bus besar/truk besar)")
        print("5. Golongan 5 (truk besar dengan trailer)")
        golongan = int(input("Pilih golongan kendaraan (1/2/3/4/5): "))
        mesin_tol.tol_masuk_tunai(gerbang_tol, golongan)
    elif pilihan == "3":
        gerbang_tol = input("Masukkan nama gerbang tol: ")
        print("Golongan Kendaraan:")
        print("1. Golongan 1 (motor)")
        print("2. Golongan 2 (mobil)")
        print("3. Golongan 3 (bus kecil/truk kecil)")
        print("4. Golongan 4 (bus besar/truk besar)")
        print("5. Golongan 5 (truk besar dengan trailer)")
        golongan = int(input("Pilih golongan kendaraan (1/2/3/4/5): "))
        tarif = mesin_tol.tol_masuk_non_tunai(gerbang_tol, golongan)
        if tarif != -1:
            print(f"Total tarif: Rp {tarif}")
            if mesin_tol.saldo >= tarif:
                mesin_tol.saldo -= tarif
                print(f"Selamat datang, {mesin_tol.username}! Anda memasuki gerbang tol {gerbang_tol}. Saldo terpotong: Rp {tarif}. Saldo sekarang: Rp {mesin_tol.saldo}")
            else:
                print("Saldo tidak mencukupi. Mohon isi ulang saldo terlebih dahulu.")
        else:
            print("Gerbang tol salah. Mohon pilih gerbang tol yang benar.")
    elif pilihan == "4":
        print("Terima kasih. Sampai jumpa lagi!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")

