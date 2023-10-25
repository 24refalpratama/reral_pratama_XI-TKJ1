from datetime import datetime

# Input estimasi waktu selesai proyek (dalam format YYYY-MM-DD)
estimasi_selesai_str = input("Masukkan estimasi waktu selesai proyek (YYYY-MM-DD): ")

# Input tanggal target selesai (dalam format YYYY-MM-DD)
target_selesai_str = input("Masukkan tanggal target selesai (YYYY-MM-DD): ")

# Konversi input menjadi objek datetime
estimasi_selesai = datetime.strptime(estimasi_selesai_str, "%Y-%m-%d")
target_selesai = datetime.strptime(target_selesai_str, "%Y-%m-%d")

# Bandingkan estimasi dan target selesai
if estimasi_selesai <= target_selesai:
    print("Tepat waktu")
else:
    print("Terlambat")