# Basic Concept:  https://saylordotorg.github.io/text_introductory-statistics/s07-basic-concepts-of-probability.html

# Tes Rumus Conditional Probability untuk keluarga dengan 2 anak

import enum, random
import matplotlib.pyplot as plt
from collections import Counter

class Anak(enum.Enum):
    LAKI = 0
    PEREMPUAN = 1

def random_anak() -> Anak:
    return random.choice([Anak.LAKI, Anak.PEREMPUAN])

keduanya_perempuan = 0
tertua_perempuan = 0
salah_satu_perempuan = 0

# gunakan seed (di bawah ini) untuk menghasilkan nilai yang sama setiap kali generate
# random.seed(0)
for keluarga in range(10000):
    anak_pertama = random_anak()
    anak_kedua = random_anak()
    if anak_pertama == Anak.PEREMPUAN:
        tertua_perempuan += 1
    if anak_pertama == Anak.PEREMPUAN and anak_kedua == Anak.PEREMPUAN:
        keduanya_perempuan += 1
    if anak_pertama == Anak.PEREMPUAN or anak_kedua == Anak.PEREMPUAN:
        salah_satu_perempuan += 1
# print("\nP(Keduanya | Tertua): ", keduanya_perempuan / tertua_perempuan)   # ~ 1/2
# print("P(Keduanya | Salah_Satu): ", keduanya_perempuan / salah_satu_perempuan)   # ~ 1/3


#===================== DISCRETE RANDOM VARIABLE ===========================================
# Jumlah lemparan dari dua dadu
# Sample space: 11  12  13  14  15  16
#               21  22  23  24  25  26
#               31  32  33  34  35  36
#               41  42  43  44  45  46
#               51  52  53  54  55  56
#               61  62  63  64  65  66

dadu1 = [1,2,3,4,5,6]
dadu2 = [1,2,3,4,5,6]
kombinasi = []
jumlah = []

# Seluruh kombinasi angka dadu
for x in dadu1:
    daftar = []
    for y in dadu2:
        angka = str(x) + str(y)
        daftar.append(angka)
    kombinasi.append(daftar)

print("\nKombinasi seluruh angka dari dua dadu:")
for elemen in kombinasi:
    print(elemen)

# Jumlah angka dari masing-masing kombinasi
for x in dadu1:
    for y in dadu2:
        angka = x + y
        jumlah.append(angka)
print("\nSample Spaces jumlah lemparan dadu:\n", sorted(jumlah))
print("\n", Counter(jumlah))



#===================== CONTINUOUS DISTRIBUTION ===========================================
# Probability Density Function (PDF)
# density function for uniform distribution:
def uniform_pdf(x: float) -> float:
    return 1 if 0 <= x < 1 else 0

# Cumulative Distribution Function (CDF)
def uniform_cdf(x: float) -> float:
    if x < 0: return 0      # uniform random tidak pernah kurang dari 0
    elif x < 1: return x
    else: return 1          # uniform random selalu kurang dari 1

x = random.random()
# print(uniform_pdf(x))
# print(uniform_cdf(x))


#===================== NORMAL DISTRIBUTION ===========================================
import math
SQRT_TWO_PI = math.sqrt(2 * math.pi)
def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))

#  plot BELL CURVE
"""
xs = [x/10 for x in range(-50, 50)]

y1 = [normal_pdf(x, sigma=1) for x in xs]
y2 = [normal_pdf(x, sigma=2) for x in xs]
y3 = [normal_pdf(x, sigma=0.5) for x in xs]
y4 = [normal_pdf(x, mu=-1) for x in xs]

plt.plot(xs, y1, '-', label='mu=0, sigma=1')
plt.plot(xs, y2, '--', label='mu=0, sigma=2')
plt.plot(xs, y3, ':', label='mu=0, sigma=0.5')
plt.plot(xs, y4, '-.', label='mu=-1, sigma=1')

plt.legend()
plt.title("Various Normal pdfs")
plt.show()
"""
