# Basic Concept:  https://saylordotorg.github.io/text_introductory-statistics/s07-basic-concepts-of-probability.html

# Tes Rumus Conditional Probability untuk keluarga dengan 2 anak

import enum, random

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

print("\nP(Keduanya | Tertua): ", keduanya_perempuan / tertua_perempuan)   # ~ 1/2
print("P(Keduanya | Salah_Satu): ", keduanya_perempuan / salah_satu_perempuan)   # ~ 1/3
