import datetime


capitulos_pasado = ["2023-05-03 23:59:59.999999", "2023-05-04 23:59:59.999999", "2023-05-04 23:59:59.999999", "2023-05-05 23:59:59.999999", "2023-05-05 23:59:59.999999"]
hoy = datetime.datetime.now()
#hoy = datetime.datetime.strptime(str(hoy.date()), "%Y-%m-%d")

reciente = False

for x in capitulos_pasado:
    fecha_proximo_capitulo = datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f")

    if  fecha_proximo_capitulo < hoy:
        reciente=True
        proximo_capitulo = fecha_proximo_capitulo + datetime.timedelta(weeks=1)
        #proximo_capitulo = datetime.datetime.strftime(proximo_capitulo, "%Y-%m-%d")

    
        print("Próximo capitulo: {}".format(proximo_capitulo))
    else:
        print(capitulos_pasado)
        reciente=False
print(reciente)
print(hoy)
print(fecha_proximo_capitulo)
print(datetime.datetime.now())
