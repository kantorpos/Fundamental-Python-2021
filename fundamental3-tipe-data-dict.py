"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = dict(anak='son', istri='wive', ayah='father', ibu='mother')
print(kamus_ind_eng)
print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_gojek = dict(driver_list=[{'nama': 'Eko', 'jarak': 10}, {'nama': 'Dwi', 'jarak': 100}], tanggal='2021-06-08')
print(data_gojek)
print(f"Driver terdekat berjarak {data_gojek['driver_list'][0]['jarak']} meter")
