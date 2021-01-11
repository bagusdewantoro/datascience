a = [0, 0]
b = [2, 2]
c = [1, 3]
d = [2, 4]
e = [3, 3]

def jarak(v, w):
    return [vi + wi for vi, wi in zip(v,w)]

d0 = jarak(a, b)
d1 = jarak(d0, c)
d2 = jarak(d1, d)
d3 = jarak(d2, e)

koordinat = [a, d0, d1, d2, d3]

def axis(delta, sumbu):
    """Delta untuk list vectornya. Sumbu 0 = X, Sumbu 1 = Y""" 
    n = []
    for titik in delta:
        titik2 = titik[sumbu]
        n.append(titik2)
    return n

sumbuX = axis(koordinat, 0)
sumbuY = axis(koordinat, 1)

#print(koordinat)
#print(sumbuX)
#print(sumbuY)
