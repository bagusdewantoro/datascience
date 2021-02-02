from typing import List
Matrix = List[List[float]]
Vector = List[float]

A = [[1, 2, 3], # 2 baris, 3 kolom
    [4, 5, 6]]

B = [[1, 2], # 3 baris, 2 kolom
    [3, 4],
    [5, 6]]

print("Matrix A:", A)
print("Matrix B:", B)


# ================== JUMLAH BARIS DAN KOLOM DALAM MATRIX =====================
from typing import Tuple
def bentukMatrix(A: Matrix) -> Tuple[int, int]:
    jml_baris = len(A)
    jml_kolom = len(A[0]) if A else 0  # Jumlah elemen di baris pertama
    return jml_baris, jml_kolom

# Tes fungsi shape dengan assert.
assert bentukMatrix(A) == (2, 3)   # 2 baris, 3 kolom

print("\n(baris, kolom) di Matrix A:", bentukMatrix(A))
print("(baris, kolom) di Matrix B:", bentukMatrix(B))


# =============== CEK NILAI MATRIX DI BARIS / KOLOM TERTENTU =====================
def nilai_di_baris(A: Matrix, i: int) -> Vector:
    return A[i]

def nilai_di_kolom(A: Matrix, j: int) -> Vector:
    return [baris[j]
    for baris in A]

print("\nNilai di baris ke-0 pada Matrix A:", nilai_di_baris(A, 0))
print("Nilai di kolom ke-1 pada Matrix B:", nilai_di_kolom(B, 1))

# =============== MEMBUAT MATRIX DARI DENGAN SHAPE TERTENTU =====================
from typing import Callable

def buat_matrix(jml_baris: int, jml_kolom: int, masukkan: Callable[[int, int], str]) -> Matrix:
    return [[masukkan(i, j) 
        for j in range(jml_kolom)]
        for i in range(jml_baris)]

print("\nMatrix 3 x 5 dengan nilai diagonal = 5 dan selain itu 0'")
print(buat_matrix(3, 5, lambda x, y: 5 if x == y else 0))