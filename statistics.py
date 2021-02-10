# Jumlah teman untuk setiap user
jml_teman = [100.0,49,41,40,25,21,21,19,19,18,
    18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,
    10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,
    9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,
    7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,
    5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
    3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,
    2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# Waktu yang dihabiskan di site tersebut untuk setiap user
waktu =  [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,
    27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,
    21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,
    23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,
    37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,
    24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,
    35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,
    20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,
    32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,
    32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,
    20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,
    9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]


# nilai terbesar = 100

from collections import Counter
import matplotlib.pyplot as plt
from typing import List

hitungteman = Counter(jml_teman)
hitungwaktu = Counter(waktu)
terbanyak = max(jml_teman)
tersedikit = min(jml_teman)
terlama = max(waktu)
tersebentar = min(waktu)
jml_data_teman = len(jml_teman)
jml_data_waktu = len(waktu)
urut = sorted(jml_teman)

# print("\n", hitungteman)
# print("\n", hitungwaktu)
print("Jumlah teman terbanyak:", terbanyak)
print("Jumlah teman tersedikit:", tersedikit)
print("Waktu terlama di site:", terlama, "menit")
print("Waktu terpendek di site:", tersebentar, "menit")
print("Jumlah data teman dan waktu = ", jml_data_teman, "dan", jml_data_waktu)
# print(urut)


# ==================== GRAFIK KEDUA DATA =================================
"""
# Jumlah Teman (Histogram)
xs = range(int(terbanyak) + 1)
ys = [hitungteman[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, terbanyak+1, 0, 25])
plt.title("Histogram Jumlah Teman")
plt.xlabel("Jumlah teman")
plt.ylabel("Jumlah orang pada data")
# plt.show()

# Waktu di site (Scatterplot)
x = range(len(waktu))
plt.scatter(x, waktu)
plt.title("Waktu Untuk Setiap User")
plt.xlabel("Index User")
plt.ylabel("Waktu di Site (menit)")
# plt.show()
"""


# ======================== DISPERSION =================================
from algebra_vector import sum_of_squares
from algebra_vector import dot
import math

# Mean
def mean(v: List[float]) -> float:
    return sum(v) / len(v)
print("\nRata-rata jumlah teman = ", mean(jml_teman))
print("Rata-rata waktu yang dihabiskan di site (menit) = ", mean(waktu))

# Variance
# Cek pengurangan tiap elemen dengan mean:
def selisih_mean(v: List[float]) -> float:
    daftar = []
    for elemen in v:
        pengurangan = elemen - mean(v)
        daftar.append(pengurangan)
    return daftar

# Hitung variance
def variance(v: List[float]) -> float:
    """ Cek di https://www.mathsisfun.com/data/standard-deviation.html """
    # Cek jumlah data, lalu gunakan rumus variance:
    N = len(v)
    selisih = selisih_mean(v)
    return sum_of_squares(selisih) / (N-1)
print("\nVariance dari jumlah teman = ", variance(jml_teman))

# Standard Deviation
def standard_deviation(v: List[float]) -> float:
    """ Cek di https://www.mathsisfun.com/data/standard-deviation.html """
    return math.sqrt(variance(v))
print("Standar Deviasi dari jumlah teman = ", standard_deviation(jml_teman))

# Covariance
# Cek hubungan antara jumlah teman & waktu yang dihabiskan di site
def covariance(v: List[float], w: List[float]) -> float:
    """ https://towardsdatascience.com/getting-the-basics-of-correlation-covariance-c8fc110b90b4 """
    assert len(v) == len(w), "jumlah elemen v dan w harus sama"
    return dot(selisih_mean(v), selisih_mean(w)) / (len(v) - 1)
print("Covariance jumlah teman dan waktu di site = ", covariance(jml_teman, waktu))

# Correlation
def correlation(v: List[float], w: List[float]) -> float:
    """ https://www.mathsisfun.com/data/correlation.html """
    stdev_V = standard_deviation(v)
    stdev_W = standard_deviation(w)
    if stdev_V > 0 and stdev_W > 0:
        return covariance(v, w) / (stdev_V * stdev_W)
    else:
        return 0 # Jika tidak ada variation, maka correlation = 0
print("Correlation jumlah teman dan waktu di site = ", correlation(jml_teman, waktu))

# Kenapa correlation rendah?? Cek ada outliers = Index pertama (list[0]) = Orang dengan 100 teman hanya 1 menit di site


# ======================== CHECK THE CORRELATION =================================
# First Correlation Plot
"""
x2 = max(jml_teman) + 5
y2 = max(waktu) + 5
plt.axis([0, 105, 0, 75])
plt.scatter(jml_teman, waktu, s=10)
plt.title("Korelasi Jumlah Teman dan Waktu")
plt.xlabel("Jumlah Teman")
plt.ylabel("Waktu di Site (menit)")
plt.show()
"""

# Cek outlier
outlier = jml_teman.index(100)  # outlier = 0 (index pertama)

# List jumlah teman baru dan waktu yang baru:
jml_teman2 = [x for i, x in enumerate(jml_teman) if i != outlier]
waktu2 = [x for i, x in enumerate(waktu) if i != outlier]

# Second Correlation Plot
x2 = max(jml_teman2) + 5
y2 = max(waktu2) + 5
plt.axis([0, x2, 0, y2])
plt.scatter(jml_teman2, waktu2, s=10)
plt.title("Korelasi Jumlah Teman dan Waktu")
plt.xlabel("Jumlah Teman")
plt.ylabel("Waktu di Site (menit)")
plt.show()

# Cek Korelasi yang baru
print("\nCovariance jumlah teman dan waktu di site = ", covariance(jml_teman2, waktu2))
print("Correlation jumlah teman dan waktu di site = ", correlation(jml_teman2, waktu2))
