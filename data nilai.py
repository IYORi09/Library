import pandas as pd

file_path = 'data_nilai.csv'  
df = pd.read_csv(file_path)

print("=== Data Nilai Siswa ===")
print(df)

print("\n=== Statistik ===")
print("Rata-rata nilai:", df['nilai'].mean())
print("Nilai tertinggi:", df['nilai'].max())
print("Nilai terendah :", df['nilai'].min())

print("\nSiswa dengan nilai tertinggi:")
print(df[df['nilai'] == df['nilai'].max()])

print("\nSiswa dengan nilai terendah:")
print(df[df['nilai'] == df['nilai'].min()])
