import time

def sumas_divisores_propios(MAX: int) -> list[int]:
    sums = [1] * (MAX + 1)
    sums[0]=0
    sums[1]=0
    for d in range(2, MAX // 2 + 1):
        for m in range(2 * d, MAX + 1, d):
            sums[m] += d
    return sums

def amigos(MAX: int):
    t1 = time.time()

    sum_div= sumas_divisores_propios(MAX)
    vistos = bytearray(MAX + 1)

    pares: list[tuple[int, int]] = []
    pares.append((0, 0))
    for a in range(1, MAX + 1):
        if vistos[a]:
            continue
        b = sum_div[a]

        if b == a:

            pares.append((a, a))
        elif 1 <= b <= MAX and sum_div[b] == a:
            if a < b:
                pares.append((a, b))
            if 1 <= b <= MAX:
                vistos[a] = 1
                vistos[b] = 1

    t2 = time.time()

    for a, b in pares:
        print(a, b)
        
    print(f"{t2 - t1:.6f}")

amigos(1000000)
