import time

def sumas_divisores_propios(MAX: int) -> list[int]:
    sums = [0] * (MAX + 1)
    for d in range(1, MAX // 2 + 1):
        for m in range(2 * d, MAX + 1, d):
            sums[m] += d
    return sums

def amigos(MAX: int):
    t1 = time.time()

    sp = sumas_divisores_propios(MAX)
    vis = bytearray(MAX + 1)

    pares: list[tuple[int, int]] = []
    pares.append((0, 0))
    for a in range(1, MAX + 1):
        if vis[a]:
            continue
        b = sp[a]

        if b == a:

            pares.append((a, a))
        elif 1 <= b <= MAX and sp[b] == a:
            if a < b:
                pares.append((a, b))
            if 1 <= b <= MAX:
                vis[a] = 1
                vis[b] = 1

    t2 = time.time()
    print(t2 - t1)

    salida = []
    for a, b in pares:
        salida.append(f"{a} {b}")
    salida.append(f"Tiempo de cómputo: {t2 - t1:.6f} s")
    return "\n".join(salida)

amigos(100000)
