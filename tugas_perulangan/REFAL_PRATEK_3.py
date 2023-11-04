nilai_investasi = 10000  # Nilai investasi awal dalam dollar
tahun = 0  # Inisialisasi jumlah tahun

while nilai_investasi <= 20000:
    tahun += 1  # Increment jumlah tahun
    pertumbuhan = nilai_investasi * 0.06  # Menghitung pertumbuhan 6% dari nilai investasi tahun sebelumnya
    nilai_investasi += pertumbuhan  # Menambahkan pertumbuhan pada nilai investasi

print(f"Butuh {tahun} tahun agar nilai investasi melebihi 20.000 dollar.")