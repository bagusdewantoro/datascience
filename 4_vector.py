vector = [
    [0, 0],
    [2, 5],
    [1, 3],
    [3, 6],
    [5, 7]
    ]

def jarak(v, w):
    return [vi + wi for vi, wi in zip(v,w)]

Notes = """
    1. Perlu fungsi untuk bikin list vector:
        [0, 0], [2, 5], [3, 8], [6, 14], [11, 21]
        Caranya:
        - initial   = vector[0] --> sama dengan vector[-1]                  = [0,0]
        - titik2    = jarak(vector[0], vector[1])   = jarak([0,0], [2,5])   = [2,5]
        - titik3    = jarak(titik2, vector[2])      = jarak([2,5], [1,3])   = [3,8]
        - titik4    = jarak(titik3, vector[3])      = jarak([3,8], [3,6])   = [6,14]
        - titik5    = jarak(titik4, vector[4])      = jarak([6,14], [5,7])  = [11,21]

    2. Perlu fungsi untuk pilih axis X atau Y (karena matplotlib akan ambil masing-masing axis)
"""

def axis(delta, sumbu):
    """Delta untuk list vectornya. Sumbu 0 = X, Sumbu 1 = Y"""
    a = [delta[0]]                      # loop_pertama: a = [[0,0]]
    for titik in delta:
        ulang = len(a)                  # loop_pertama: len(a) = 1
        if ulang == len(delta):         # loop_pertama: ulang=1. len(delta)=5. jadi belum break
            break
        new1 = jarak(a[-1], delta[ulang])   # loop_pertama: jarak([0,0], [2,5]) = [2,5]
        a.append(new1)                  # loop_pertama: a.append([2,5]) = [[0,0], [2,5]]
    # print(a)

    b = []
    for posisi in a:                # assume sumbu = 1
        koordinat = posisi[sumbu]   # loop_pertama: koordinat = [0,0][1]    = 0
        b.append(koordinat)         # loop_pertama: b = [0]
    # print(b)
    return b

sumbuX = axis(vector, 0)
sumbuY = axis(vector, 1)

#===================================================================
from matplotlib import pyplot as plt

plt.plot(sumbuX, sumbuY, color='green', marker='o', linestyle='solid')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
