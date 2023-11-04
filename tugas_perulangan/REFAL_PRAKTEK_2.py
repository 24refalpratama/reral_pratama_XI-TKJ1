jarak = 5  # Jarak awal yang ditempuh oleh pelari
minggu = 0  # Inisialisasi jumlah minggu

while jarak <= 10:
    minggu += 1  # Increment jumlah minggu
    pertambahan = jarak * 0.10  # Menghitung 10% dari jarak minggu sebelumnya
    jarak += pertambahan  # Menambahkan pertambahan pada jarak

print(f"Butuh {minggu} minggu agar pelari dapat berlari lebih dari 10 kilometer.")