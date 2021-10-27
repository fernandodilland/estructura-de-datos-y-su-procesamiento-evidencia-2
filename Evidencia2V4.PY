# Evidencia 2, Estructura de datos y su procesamiento.

from collections import namedtuple
import os
import csv

Venta = namedtuple('Ventas', ('descripcion', 'cantidadVenta', 'precioVenta', 'fechaVenta'))
DiccionarioVentas = {}
ListaVentas = []
separador = ('-' * 45)
subtotal = 0
numFila=1

print('Bienvenido(a) al negocio de ventas de llantas')
print(separador)

if os.path.exists('ventas.csv'):
    print('Ya existe un archivo \"ventas.csv" en el mismo directorio')
    with open('ventas.csv','r')as archivo:
        ContenidoArchivo = csv.reader(archivo)
        #DiccionarioVentas=ContenidoArchivo
        
        for fila in ContenidoArchivo: # Lector fila por fila del archivo
            contadorTamanioFila = 5
            detectoAlMenosUnElementoEnFila = False

            while True:
                if len(fila) == contadorTamanioFila: # Solo 1 elemento en fila
                    if detectoAlMenosUnElementoEnFila == True:
                    
                        folio = int(fila[0])
                        
                        buscadorTemporal = 21
                        datoExtraidoTemporal = fila[contadorInternoTamanioFila-4][buscadorTemporal:len(fila[contadorInternoTamanioFila-4])-1]
                        print("\nDescripción:", datoExtraidoTemporal)
                        descripcion = str(datoExtraidoTemporal)
                        
                        buscadorTemporal = 15
                        datoExtraidoTemporal = fila[contadorInternoTamanioFila-3][buscadorTemporal:len(fila[contadorInternoTamanioFila-3])]
                        print("Cantidad vendida:", datoExtraidoTemporal)
                        cantidadVenta = int(datoExtraidoTemporal)
                        
                        buscadorTemporal = 13
                        datoExtraidoTemporal = fila[contadorInternoTamanioFila-2][buscadorTemporal:len(fila[contadorInternoTamanioFila-2])]
                        print("Precio Venta:", datoExtraidoTemporal)
                        precioVenta = float(datoExtraidoTemporal)
                        
                        buscadorTemporal = 13
                        datoExtraidoTemporal = fila[contadorInternoTamanioFila-1][buscadorTemporal:len(fila[contadorInternoTamanioFila-1])-3]
                        print("Fecha venta:", datoExtraidoTemporal)
                        fecha = str(datoExtraidoTemporal)
                        
                        # Inyección de datos a Diccionario
                        organizacionVenta = Venta(descripcion,cantidadVenta, precioVenta, fecha)
                        ListaVentas.append(organizacionVenta)
                        DiccionarioVentas[folio] = ListaVentas
                        
                        break
                    
                    ListaVentas=[] # Limpieza de la lista

                    print("\n-- Venta ID: {} (se detectó solo 1 producto)".format(fila[0]))
                    folio = int(fila[0])
                    
                    buscadorTemporal = 21
                    datoExtraidoTemporal = fila[1][buscadorTemporal:len(fila[1])-1]
                    print("\nDescripción:", datoExtraidoTemporal)
                    descripcion = str(datoExtraidoTemporal)
                    
                    buscadorTemporal = 15
                    datoExtraidoTemporal = fila[2][buscadorTemporal:len(fila[2])]
                    print("Cantidad vendida:", datoExtraidoTemporal)
                    cantidadVenta = int(datoExtraidoTemporal)
                    
                    buscadorTemporal = 13
                    datoExtraidoTemporal = fila[3][buscadorTemporal:len(fila[3])]
                    print("Precio Venta:", datoExtraidoTemporal)
                    precioVenta = float(datoExtraidoTemporal)
                    
                    buscadorTemporal = 13
                    datoExtraidoTemporal = fila[4][buscadorTemporal:len(fila[4])-3]
                    print("Fecha venta:", datoExtraidoTemporal)
                    fecha = str(datoExtraidoTemporal)
                    
                    # Inyección de datos a Diccionario
                    organizacionVenta = Venta(descripcion,cantidadVenta, precioVenta, fecha)
                    ListaVentas.append(organizacionVenta)
                    DiccionarioVentas[folio] = ListaVentas
                    
                    break
    
                else: # En caso de que haya más de 1 elemento en la misma fila
                    
                    
                    if detectoAlMenosUnElementoEnFila == False:
                        print("\n-- Venta ID: {} (se detectó más de 1 producto)".format(fila[0]))
                        folio = int(fila[0])
                    
                    contadorInternoTamanioFila = contadorTamanioFila
                    buscadorTemporal = 21
                    datoExtraidoTemporal = fila[contadorInternoTamanioFila-4][buscadorTemporal:len(fila[contadorInternoTamanioFila-4])-1]
                    print("\nDescripción:", datoExtraidoTemporal)
                    descripcion = str(datoExtraidoTemporal)
                    
                    buscadorTemporal = 15
                    datoExtraidoTemporal = fila[contadorInternoTamanioFila-3][buscadorTemporal:len(fila[contadorInternoTamanioFila-3])]
                    print("Cantidad vendida:", datoExtraidoTemporal)
                    cantidadVenta = int(datoExtraidoTemporal)
                    
                    buscadorTemporal = 13
                    datoExtraidoTemporal = fila[contadorInternoTamanioFila-2][buscadorTemporal:len(fila[contadorInternoTamanioFila-2])]
                    print("Precio Venta:", datoExtraidoTemporal)
                    precioVenta = float(datoExtraidoTemporal)
                    
                    buscadorTemporal = 13
                    datoExtraidoTemporal = fila[contadorInternoTamanioFila-1][buscadorTemporal:len(fila[contadorInternoTamanioFila-1])-2]
                    print("Fecha venta:", datoExtraidoTemporal)
                    fecha = str(datoExtraidoTemporal)
                    
                    # Inyección de datos a Diccionario
                    organizacionVenta = Venta(descripcion,cantidadVenta, precioVenta, fecha)
                    ListaVentas.append(organizacionVenta) #<<<<<<<
                    DiccionarioVentas[folio] = ListaVentas
            
                    contadorInternoTamanioFila += 4
                    
                    detectoAlMenosUnElementoEnFila = True
                    
                    
                contadorTamanioFila = contadorTamanioFila + 4 # Para encontrar siguiente conjunto dentro de Fila
            numFila += 1
        
            print("\nAgregado a Diccionario venta ID {}".format(fila[0]))
   
            ListaVentas=[] # Limpieza de la lista
   
    print("\n-- Se ha importado del .csv\n")
    print(separador)

else:
    print("No existe archivo .csv creado")
    print(separador)

def Menu():
    opcion = int(input('Menú de opciones:\n[1] Registrar una venta\n[2] Consultar una venta\n[3] Reporte de ventas de fecha\n[4] Mostrar todas las ventas\n[5] Salir y guardar archivo .csv\n» '))
    return opcion

def RegistrarVenta():
    ListaVentas=[] # Limpieza de la lista
    print('\n--------- Registro de venta ---------')
    
    fecha = input('Introduzca la fecha de venta (ej. 10/10/2021)\n» ')
    while True:
        folio = int(input(f'Introduzca folio de venta de llanta(s)\n» '))

        if folio in DiccionarioVentas.keys():
            print('Error, ya existe una venta con ese folio de venta')
        else:
            break

    while True:
        descripcion = input('Introduzca descripción del tipo de llanta\n» ')
        cantidadVenta = int(input('Introduzca cantidad a vender del tipo de llanta mencionado\n» '))
        precioVenta = float(input('Introduzca precio (sin iva) del tipo de llanta (por unidad)\n» $'))
        print(separador)
        subtotal = (cantidadVenta * precioVenta)
        print(f'Subtotal (sin iva) de las llantas tipo {descripcion}:','${:.2f}'.format(subtotal))
        print(separador)
        organizacionVenta = Venta(descripcion,cantidadVenta, precioVenta, fecha)
        ListaVentas.append(organizacionVenta)
        DiccionarioVentas[folio] = ListaVentas
        agregaOtraLlantaMismaVenta = int(input('¿Desea agregar otra(s) venta(s) de llanta(s) a la misma venta?\n[1] Si \n[2] No\n» '))

        if agregaOtraLlantaMismaVenta == 2:
            dimensionVentas, acumuladoVentas = 0 , 0
            while dimensionVentas < len(DiccionarioVentas[folio]):
                aculumador = (float(DiccionarioVentas[folio][dimensionVentas].precioVenta) * int(DiccionarioVentas[folio][dimensionVentas].cantidadVenta))
                acumuladoVentas =  aculumador + acumuladoVentas
                dimensionVentas += 1
            print(separador)
            print('Subtotal: ${:.2f}'.format(acumuladoVentas),'\nIVA:','${:.2f}'.format(acumuladoVentas * .16))
            print('-' * 16,'\n\nTotal: ${:.2f}'.format(acumuladoVentas*1.16, 2),f'\nVenta realizada el: {fecha}\n')
            print(separador)
            break

def ConsultarVenta():
    consulta = int(input('Folio a consultar: '))
    dimension, totalVentas = 0 , 0

    if consulta in DiccionarioVentas.keys():

        while dimension < len(DiccionarioVentas[consulta]):
            print(separador)
            print(f'Descripción del tipo de llanta: {DiccionarioVentas[consulta][dimension].descripcion}')
            print(f'Cantidad de llantas: {DiccionarioVentas[consulta][dimension].cantidadVenta}')
            print('Precio: ${:.2f}'.format(DiccionarioVentas[consulta][dimension].precioVenta, 2))
            print(f'Fecha: {DiccionarioVentas[consulta][dimension].fechaVenta}')
            totalVentas = (float(DiccionarioVentas[consulta][dimension].precioVenta) * float(DiccionarioVentas[consulta][dimension].cantidadVenta)) + totalVentas
            dimension += 1
        print(separador)
        print('Subtotal: ${:.2f}'.format(totalVentas),'\nIVA:','${:.2f}'.format(totalVentas * .16))
        print('-' * 16,'\n\nTotal: ${:.2f}\n'.format(totalVentas + totalVentas * .16, 2))
        print(separador)

    else:
        print('La clave no esta registrada')

def ReporteVentas():
    fechaBusqueda = input("Ingrese la fecha para encontrar las ventas de ese día (ej: dd/mm/yyyy)\n» ")
    encontroAlMenosUnDato = False
    Subtotal = 0
    GranTotalVenta = 0
    GranTotalVentasDiaSinIva = 0
    GranTotalVentasDiaConIva = 0

    for key, value in DiccionarioVentas.items() :
        diferentesLlantasDentroMismaVenta = len(value)
        contador = 0
        while contador < diferentesLlantasDentroMismaVenta:
            fechaExtraida = value[contador].fechaVenta # Se evitó el [:-15] en "fechaVenta"

            if fechaBusqueda == fechaExtraida:

                if encontroAlMenosUnDato == False:
                    print("\nSe ha encontrado ventas del día",fechaBusqueda)
                    print("      Folio    |   Descripcion   |  Cantidad  |  Precio c/u  |    Fecha   |  Subtotal    |   IVA      |  Total")
                    encontroAlMenosUnDato = True # Temporal

            if fechaBusqueda == fechaExtraida:
                Subtotal = value[contador].precioVenta*value[contador].cantidadVenta
                IVA = (value[contador].precioVenta*value[contador].cantidadVenta)*.16
                GranTotalVenta = IVA + (value[contador].precioVenta*value[contador].cantidadVenta)
                print(f'\t{key:<6} | {value[contador].descripcion:^15} | {value[contador].cantidadVenta:^10} |   ${value[contador].precioVenta:<9} | {value[contador].fechaVenta[-10:]:<8} |   ${Subtotal:<9} |   ${IVA:<7} |  ${GranTotalVenta:<10}')
                GranTotalVentasDiaSinIva = GranTotalVentasDiaSinIva + (value[contador].precioVenta*value[contador].cantidadVenta)
                GranTotalVentasDiaConIva = GranTotalVentasDiaConIva + GranTotalVenta
            contador+= 1

    if encontroAlMenosUnDato == True:
        print("\nEl día", fechaBusqueda, " se vendió en total:",'${:.2f}'.format(GranTotalVentasDiaSinIva),"con iva:",'${:.2f}'.format(GranTotalVentasDiaConIva))    
    print("")

    if encontroAlMenosUnDato == False:
        print("Error, no se encuentra datos de esa fecha")

def GuardarCSV():
    print("Guardando archivo .csv")
    with open('ventas.csv', 'w') as f:
            for key in DiccionarioVentas.keys():
                f.write("%s,%s\n"%(key,DiccionarioVentas[key]))
    print("Se ha guardado archivo .csv en el mismo directorio")
    
def MostrarVentas():
    print(DiccionarioVentas)
    print("Todas las ventas")

while True:
    opcionElegida = Menu()
    if opcionElegida == 1:
        RegistrarVenta()
    if opcionElegida == 2:
        ConsultarVenta()
    if opcionElegida == 3:
        ReporteVentas()
    if opcionElegida == 4:
        MostrarVentas()
    if opcionElegida == 5:
        GuardarCSV()
        break
