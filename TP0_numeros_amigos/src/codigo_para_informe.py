import sys, os, time, re
from pathlib import Path
import matplotlib.pyplot as plt
import math
from typing import Iterable, List

SRC_DIR = Path(__file__).resolve().parent
ROOT_DIR = SRC_DIR.parent
CORRIDAS_DIR = ROOT_DIR / "corridas"
CORRIDAS_DIR.mkdir(parents=True, exist_ok=True)

DEFAULTS_G = [
    50000, 100000, 150000, 200000, 250000, 350000,
    500000, 1000000, 2000000, 3000000, 5000000,
    7000000, 10000000, 20000000, 30000000, 40000000, 50000000
]


def sumas_divisores_propios(MAX: int) -> List[int]:
    sums = [1] * (MAX + 1)
    sums[0] = 0
    if MAX >= 1:
        sums[1] = 0
    for d in range(2, MAX // 2 + 1):
        for m in range(2 * d, MAX + 1, d):
            sums[m] += d
    return sums


def amigos(MAX: int) -> str:
    t1 = time.time()

    sum_div = sumas_divisores_propios(MAX)
    vistos = bytearray(MAX + 1)

    pares: List[tuple[int, int]] = []
    pares.append((0, 0))
    for a in range(1, MAX + 1):
        if vistos[a]:
            continue
        b = sum_div[a]

        if b == a:
            # perfecto
            pares.append((a, a))
        elif 1 <= b <= MAX and sum_div[b] == a:
            # par amigo
            if a < b:
                pares.append((a, b))
            vistos[a] = 1
            if 1 <= b <= MAX:
                vistos[b] = 1

    t2 = time.time()

    salida = []
    for a, b in pares:
        salida.append(f"{a} {b}")
    salida.append(f"Tiempo: {t2 - t1:.6f} s")
    return "\n".join(salida)


def crear_corridas(max_values: Iterable[int] | int):
    # Permitir int o iterable de int
    if isinstance(max_values, int):
        max_values = [max_values]

    for m in max_values:
        if not isinstance(m, int):
            raise TypeError(f"MAX debe ser int, recibido: {type(m)} -> {m}")
        print(f"Procesando MAX={m} ...")
        resultado = amigos(m)
        filename = CORRIDAS_DIR / f"{m}_refactor_amigos.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(resultado)


def crear_graficos_tiempo(max_values: List[int]):
    xs, ys = [], []
    patron = re.compile(r"Tiempo:\s*([0-9]+(?:\.[0-9]+)?)\s*s")

    for m in max_values:
        fname = CORRIDAS_DIR / f"{m}_refactor_amigos.txt"
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

        # Ajuste por n log n sin fijar estilo de color
        f = [n * math.log(n) for n in xs]
        sum_ff = sum(val * val for val in f)
        if sum_ff > 0:
            c = sum(y * fi for y, fi in zip(ys, f)) / sum_ff
            y_fit = [c * fi for fi in f]
            plt.plot(xs, y_fit, linestyle="--", marker=None, label=r"Ajuste $c \cdot n\log n$")
            plt.title("Tiempos por MAX – Refactor TP0 (ajuste ~ n log n)")
        else:
            plt.title("Tiempos por MAX – Refactor TP0")

    plt.xlabel("MAX (escala log)")
    plt.ylabel("Segundos (escala log)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xscale("log")
    plt.yscale("log")
    if xs:
        plt.xticks(xs, [str(v) for v in xs], rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(ROOT_DIR / "graficos_refactor_tp0.png", dpi=150)


def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python3 codigo_para_informe.py c <MAX>")
        print("  python3 codigo_para_informe.py g [<MAX1> <MAX2> ... <MAXN>]")
        sys.exit(1)

    modo = sys.argv[1].lower()

    if modo == "c":
        if len(sys.argv) < 3:
            print("Error: falta <MAX>")
            sys.exit(1)
        try:
            max_value = int(sys.argv[2])
        except ValueError:
            print("Error: <MAX> debe ser entero")
            sys.exit(1)
        crear_corridas([max_value])
        return

    if modo == "g":
        if len(sys.argv) == 2:
            valores = DEFAULTS_G[:]  # por defecto
        else:
            try:
                valores = [int(x) for x in sys.argv[2:]]
            except ValueError:
                print("Error: todos los valores deben ser enteros")
                sys.exit(1)
        crear_graficos_tiempo(valores)
        return

    print(f"Modo desconocido: {modo}")
    print("Opciones válidas: c (corrida), g (gráficos)")
    sys.exit(1)


if __name__ == "__main__":
    main()
