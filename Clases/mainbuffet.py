from Buffet import *

Rancio = Colegio()
unAlumno = Alumno()
unProfesor = Profesor()
unPlato = Plato()
unPedido = Pedido()


while 1:
    print("!) Agregar ALumnos")
    print("2) Agregar Profesor")
    print("3) Agregar Plato")
    print("4) Agregar Pedido")
    print("-----------------------")
    print("5) Eliminar Alumno: ")
    dato=int(input())
    if dato == 1:
        unAlumno = Alumno()
        print("Nombre: ")
        unAlumno.Nombre= input()
        print("Apellido: ")
        unAlumno.Apellido = input()
        print("DNI: ")
        unAlumno.DNI = input()
        print("Division: ")
        unAlumno.Division = input()
        Rancio.listaPersonas.append(unAlumno)
    elif dato == 2:
        unProfesor = Profesor()
        print("Nombre: ")
        unProfesor.Nombre = input()
        print("Apellido: ")
        unProfesor.Apellido = input()
        print("DNI: ")
        unProfesor.DNI = input()
        print("Descuento: ")
        unProfesor.Descuento = input()
        Rancio.listaPersonas.append(unProfesor)
    elif dato == 3:
        unPlato = Plato()
        print("Nombre: ")
        unPlato.Nombre=input()
        print("Precio: ")
        unPlato.Precio=input()
        Rancio.listaPlatos.append(unPlato)
    elif dato == 4:
        unPedido = Pedido()
        print("Fecha de Entrega: ")
        unPedido.FechaEntrega=input()
        print("DNI del Comprador: ")
        dni = input()
        for person in Rancio.listaPersonas
            if person.DNI=dni:
                unPedido.Comprador=person
                break
        print("Plato: ")
        plato = input()
        for platox in listaPlatos:
            if platox.Nombre == plato:
                unPlato.Nombre=platox
        print("HoraEntrega: ")
        unPedido.HoraEntrega=input()
        print("Entregado: ")
        unPedido.Entregado=input()
        Rancio.listaPedidos.append(unPedido)
    elif dato == 5:
        print("DNI del ALumno: ")
        dni=input()
        for alumn in Rancio.listaPersonas
            if alumn.DNI=dni:
                Rancio.eliminarPersona(alumn)

    elif dato == 6:
        print("DNI del Profesor: ")
        dni=input()
        for profe in Rancio.listaPersonas
            if profe.DNI=dni:
                Rancio.eliminarPersona(profe)

    break

