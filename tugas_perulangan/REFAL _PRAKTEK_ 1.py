jumlah_ayam = 100  # Jumlah ayam awal
bulan = 0  # Inisialisasi jumlah bulan

while jumlah_ayam <= 200:
    bulan += 1  # Increment jumlah bulan
    pertambahan = jumlah_ayam * 0.05  # Menghitung 5% dari jumlah ayam bulan sebelumnya
    jumlah_ayam += pertambahan  # Menambahkan pertambahan pada jumlah ayam

print(f"Butuh {bulan} bulan agar jumlah ayam melebihi 200 ekor.")