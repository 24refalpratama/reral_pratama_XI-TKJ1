jumlah_apel = 100  # Jumlah apel awal
hari = 0  # Inisialisasi jumlah hari

while jumlah_apel > 20:
    hari += 1  # Increment jumlah hari
    terjual = jumlah_apel * 0.10  # Menghitung 10% dari jumlah apel yang tersisa
    jumlah_apel -= terjual  # Mengurangi apel yang terjual dari jumlah apel

print(f"Butuh {hari} hari agar sisa apel kurang dari 20 buah.")