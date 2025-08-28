# Escritura de datos en un archivo CSV 

import csv
csv.writer
# listado de frutas 
frutas=[
    ["manzana","roja","dulce"],
    ["platáno","amarillo","dulce"],
    ["lima","verde","ácida"],
]


from pathlib import Path
#creamos y abrimos el archivo en csv 

ruta_archivo = Path() / "frutas.csv"
with ruta_archivo.open(mode="w", encoding="utf-8") as archivo:
 escritor_csv = csv.writer(archivo)
# Escribir los datos
#escribir todas las sublistas como filas
 escritor_csv.writerows(frutas)

print("se ha creado el archivo")