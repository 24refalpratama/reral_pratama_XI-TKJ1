# Input total belanjaan pelanggan
total_belanjaan = float(input("Masukkan total belanjaan: "))

# Inisialisasi variabel diskon
diskon = 0

# Tentukan diskon berdasarkan aturan
if total_belanjaan > 500000:
    diskon = 0.10  # Diskon 10%
elif 300000 <= total_belanjaan <= 500000:
    diskon = 0.05  # Diskon 5%

# Hitung jumlah diskon
jumlah_diskon = total_belanjaan * diskon

# Hitung total yang harus dibayarkan setelah diskon
total_setelah_diskon = total_belanjaan - jumlah_diskon

# Output hasil
print(f"Total belanjaan: {total_belanjaan}")
print(f"Diskon yang diberikan: {diskon * 100}%")
print(f"Jumlah diskon: {jumlah_diskon}")
print(f"Total yang harus dibayarkan setelah diskon: {total_setelah_diskon}")