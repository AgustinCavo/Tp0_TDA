import time

def sumas_divisores_propios(MAX: int) -> list[int]:
    sums = [0] * (MAX + 1)
    for d in range(1, MAX // 2 + 1):
        for m in range(2 * d, MAX + 1, d):
            sums[m] += d
    return sums

def amigos(MAX: int):
    t1 = time.time()
    lista_suma_divisores = sumas_divisores_propios(MAX)
    vis = bytearray(MAX + 1) 

    for a in range(1, MAX + 1):
        if vis[a]:
            continue
        b = lista_suma_divisores[a]
        
        if b != a and 1 <= b <= MAX and lista_suma_divisores[b] == a:
            print(a, b) if a < b else print(b, a)
            if 1 <= b <= MAX:
                vis[a] = 1
                vis[b] = 1

    t2 = time.time()
    print(t2 - t1)


amigos(100000)
