import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

# Inisialisasi DataFrame
df = pd.DataFrame(data)

# Menghitung gaji setelah peningkatan 5%
df['Gaji + 5%'] = df['Gaji'].apply(lambda x: x * 1.05)

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("DataFrame setelah peningkatan gaji sebesar 5%:")
print(df)
print("Ringkasan Peningkatan Gaji 5%:")
print(df['Gaji + 5%'])


# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
df['Gaji + 2%'] = df.apply(lambda row: row['Gaji + 5%'] * 1.02 if row['Usia'] > 30 else row['Gaji + 5%'], axis=1)

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan
print("\nDataFrame setelah peningkatan tambahan untuk karyawan di atas 30 tahun:")
print(df)

# Ringkasan hasilnya.
print("Gaji setelah di evaluasi umur :")
print(df['Gaji + 2%'])
