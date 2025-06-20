contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

print(contoh_list)

#jumlah data pada list
print(len(contoh_list))

#nilai terkecil pada list
print(min(contoh_list))

#nilai terbesar pada list
print(max(contoh_list))

#hitung nilai 5 pada list
print(contoh_list.count(5))

#akses list
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]

#atau bisa menggunakan
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

#sorting asc (menggunakan ASCII/huruf kapital akan di dahulukan)
kendaraan = ['motor', 'Mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)

#desc
kendaraan.sort(reverse=True)
print(kendaraan)