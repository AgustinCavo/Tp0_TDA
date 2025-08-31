# Tp0_TDA

1) Extraer el contenido del .zip

# Ejecutar refactor del codigo con 1000000

1) moverse a la carpeta de destino en caso de no haber modificado el nombre:
    cd Tp0_TDA-main
    cd TP0_numeros_amigos
    cd src
2) ejecutar el tp:co
    python3 TP0.py

en caso de querer cambiar el MAX modificar linea 42 por el numero deseado.

# Ejecutar el codgio para el informe
1) moverse a la carpeta de destino en caso de no haber modificado el nombre:
    cd Tp0_TDA-main
    cd TP0_numeros_amigos
    cd src

2) Para crear el csv con una corrida especifica:
    python3 codigo_para_informe.py c <valor de max>

    ejemplo: python3 codigo_para_informe.py c 150000

3) Para crear el csv el grafico de determinados puntos:
    python3 codigo_para_informe.py g <valor de max1> <valor de max2> ... <valor de maxn> 

    ejemplo: python3 codigo_para_informe.py g 150000 200000 300000 1000000

    si no se indica cual usa por defecto los puntos 50000, 100000, 150000, 200000, 250000, 350000,
    500000, 1000000, 2000000, 3000000, 5000000,7000000, 10000000, 20000000, 30000000, 40000000, 50000000

# Ejecutar el codigo amigos_rust

1) moverse a la carpeta de destino en caso de no haber modificado el nombre:
    cd Tp0_TDA-main
    cd amigos_rust

2) ejecutar comandos para ejecutarlo:
    cargo build
    cargo run