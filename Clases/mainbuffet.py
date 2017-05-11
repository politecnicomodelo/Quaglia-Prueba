from Buffet import *

Rancio = Colegio()
unAlumno = Alumno()
unProfesor = Profesor()
unPlato = Plato()
unPedido = Pedido()


while 1:
    print("1) Agregar Alumnos")
    print("2) Agregar Profesor")
    print("3) Agregar Plato")
    print("4) Agregar Pedido")
    print("-----------------------")
    print("5) Eliminar Persona ")
    print("6) Modificar Persona")
    print("-----------------------")
    print("7) Guardar")
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
        for person in Rancio.listaPersonas:
            if person.DNI==dni:
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
        print("DNI: ")
        dni=input()
        for alumn in Rancio.listaPersonas:
            if alumn.DNI==dni:
                Rancio.eliminarPersona(alumn)
    elif dato == 6:
        print("DNI: ")
        dni = input()
        for alumn in Rancio.listaPersonas:
            if alumn.DNI==dni:
                print("1)Modificar Nombre: ")
                print("2)Modificar Apellido: ")
                print("3)Modificar Descuento: ")
                datom=int(input())
                if datom == 1:
                    person.Nombre=input()
                elif datom == 2:
                    person.Apellido=input()
                elif datom == 3:
                    if person.getDescuento()==0:
                        print("Un alumno no posee descuento.")
                        input()
                        break
                    else:
                        print("Descuento: ")
                        desc=input()
                        person.Descuento=desc
    elif dato == 7:
        Rancio.guardar()


