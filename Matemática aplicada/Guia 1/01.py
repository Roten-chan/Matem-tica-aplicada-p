def transmisionDatos(segundos):
    return 100 * segundos

datos_transmitidos_1 = transmisionDatos(45)
datos_transmitidos_2 = transmisionDatos(1.5 * 60)
datos_transmitidos_3 = transmisionDatos(60 * 60)

print(f"1) 45 segundos = {(datos_transmitidos_1)} Mb/s")
print(f"2) 1.5 minutos = {datos_transmitidos_2} Mb/s")
print(f"3) 1 hora = {datos_transmitidos_3} Mb/s")