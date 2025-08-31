import time
import os
import gc
import re
import matplotlib.pyplot as plt
import math

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
    print(t2 - t1)

    salida = []
    for a, b in pares:
        salida.append(f"{a} {b}")
    salida.append(f"Tiempo: {t2 - t1:.6f} s")
    return "\n".join(salida)

def crear_corridas(max_values):

    carpeta = "TP0_numeros_amigos/corridas"
    os.makedirs(carpeta, exist_ok=True)

    for m in max_values:
        print(f"Procesando MAX={m} ...")
        resultado = amigos(m)
        filename = os.path.join(carpeta, f"{m}_refactor_amigos.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(resultado)
        del resultado
        gc.collect()

def crear_graficos_tiempo(max_values):
    carpeta = "TP0_numeros_amigos/corridas"
    xs, ys = [], []
    patron = re.compile(r"Tiempo:\s*([0-9]+(?:\.[0-9]+)?)\s*s")
    for m in max_values:
        fname = os.path.join(carpeta, f"{m}_refactor_amigos.txt")
        try:
            with open(fname, "r", encoding="utf-8") as f:
                contenido = f.read()
            mat = patron.search(contenido)
            if mat:
                tiempo = float(mat.group(1))
                xs.append(m)
                ys.append(tiempo)
        except FileNotFoundError:
            print(f"Archivo no encontrado (omitido): {fname}")

    plt.figure(figsize=(10, 6))
    if xs:
        
        plt.plot(xs, ys, marker="o", label="TP0 refactor")

        f = [n * math.log(n) for n in xs] 
        sum_ff = sum(val * val for val in f)
        if sum_ff > 0:
            c = sum(y * fi for y, fi in zip(ys, f)) / sum_ff
            y_fit = [c * fi for fi in f]
            plt.plot(xs, y_fit, linestyle="--", marker=None, label=r"Ajuste $c \cdot n\log n$")
            plt.title(f"Tiempos por MAX – Refactor TP0 (ajuste ~ n log n")
        else:
            plt.title("Tiempos por MAX – Refactor TP0")

    plt.xlabel("MAX (escala log)")
    plt.ylabel("Segundos (escala log)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xscale("log")
    plt.yscale("log")
    plt.xticks(xs, [str(v) for v in xs], rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficos_refactor_tp0.png", dpi=150)
    


max_values = [50000, 100000,150000,200000,250000,350000,500000,1000000,2000000,3000000,5000000,7000000,10000000,20000000,30000000,40000000,50000000]
#max_values = [50000, 100000,150000,250000,350000,500000,1000000]
#crear_corridas(max_values)
crear_graficos_tiempo(max_values)
