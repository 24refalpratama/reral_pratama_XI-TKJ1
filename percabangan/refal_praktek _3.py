# Nama file yang ingin diperiksa
nama_file = "data.txt"

# Daftar file di server
daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

# Periksa apakah file sudah ada dalam daftar
if nama_file in daftar_file_di_server:
    print("File sudah ada.")
else:
    print("File belum ada.")