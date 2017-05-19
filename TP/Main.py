from Aviones import *

listaAviones= []
listaPasajeros=[]
listaPilotos=[]
listaServicios=[]
listaVuelos=[]

auxAvion = Avion()
auxPasajero = Pasajero()
auxPiloto = Piloto()
auxServicio = Servicio()
auxVuelo = Vuelo()

f = open("personas.dat", "r")
for line in f:
    a=line.split("|")
    if a[0]=="Pasajero":
        auxPasajero=Pasajero()
        auxPasajero.Nombre = a[1]
        auxPasajero.Apellido = a[2]
        auxPasajero.FechaNacimiento = a[3]
        auxPasajero.DNI = a[4]
        auxPasajero.VIP = a[5] == '1'
        if a[6] != "":
            auxPasajero.Necesidades = a[6]
        listaPasajeros.append(auxPasajero)
    elif a[0] == "Piloto":
        auxPiloto=Piloto()
        auxPiloto.Nombre = a[1]
        auxPiloto.Apellido = a[2]
        auxPiloto.FechaNacimiento = a[3]
        auxPiloto.DNI = a[4]
        modelo = a[5].split(",")
        auxPiloto.modeloAviones = modelo
        listaPilotos.append(auxPiloto)
    elif a[0] == "Servicio":
        auxServicio=Servicio()
        auxServicio.Nombre = a[1]
        auxServicio.Apellido = a[2]
        auxServicio.FechaNacimiento = a[3]
        auxServicio.DNI = a[4]
        modelo = a[5].split(",")
        auxServicio.modeloAviones = modelo
        idioma = a[6].split(",")
        auxServicio.Idiomas = idioma
        listaServicios.append(auxServicio)
f.close()
f = open("aviones.dat", "r")
for line in f:
    a = line.split("|")
    auxAvion = Avion()
    auxAvion.codigoUnico = a[0]
    auxAvion.cantidadPasajeros = a[1]
    auxAvion.cantidadTripulacion = a[2]
    listaAviones.append(auxAvion)
f.close()
f = open("vuelos.dat", "r")

for line in f:
    a = line.split("|")
    auxVuelo = Vuelo()
    for avion in listaAviones:
        if avion.codigoUnico == a[0]:
            auxVuelo.Avion = avion
        auxVuelo.Fecha = a[1]
        auxVuelo.Hora = a[2]
        auxVuelo.Origen = a[3]
        auxVuelo.Destino = a[4]
        tripulacion = a[5].split(",")
    for tripulante in tripulacion:
        for serv in listaServicios:
            if tripulante == serv.DNI:
                 auxVuelo.agregarTripulacion(serv)
        for piloto in listaPilotos:
              if piloto == serv.DNI:
                auxVuelo.agregarTripulacion(piloto)
        pasajeros = a[6].split(",")
        for pasajero in pasajeros:
            for pasajero1 in listaPasajeros:
                if pasajero == pasajero1.DNI:
                    auxVuelo.agregarPasajero(pasajero1)
    listaVuelos.append(auxVuelo)

