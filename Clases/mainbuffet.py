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
    print("8) Modificar Plato")
    print("9) Eliminar Plato")
    print("10) Eliminar Pedido")
    print("11) Modificar pedido")
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
        unPedido.Comprador=input()
        print("Plato: ")
        unPlato.Nombre=input()
        print("HoraEntrega: ")
        unPedido.HoraEntrega=input()
        unPedido.Entregado=False
        for persona in Rancio.listaPersonas:
            if unPedido.Comprador == persona.DNI:
                if persona.Descuento !=0:
                    unPedido.Plato.Precio= unPedido.Plato.Precio - persona.Descuento*unPedido.Plato.Precio/100

        Rancio.listaPedidos.append(unPedido)
    elif dato == 5:
        print("DNI: ")
        dni=input()
        for persona in Rancio.listaPersonas:
            if persona.DNI==dni:
                Rancio.eliminarPersona(alumn)
    elif dato == 6:
        print("DNI: ")
        dni = input()
        for person in Rancio.listaPersonas:
            if person.DNI==dni:
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
    elif dato == 8:
        print("Nombre del Plato: ")
        namePlato = input()
        for a in Rancio.listaPlatos:
            if a.Nombre == namePlato:
                print("1)Modificar Nombre: ")
                print("2)Modificar Precio: ")
                datomod = int(input())
                if datomod == 1:
                    print("Nuevo nombre del plato: ")
                    a.Nombre=input()
                if datomod == 2:
                    print("Nuevo precio del plato: ")
                    a.Precio=input()
    elif dato == 9:
        print("Nombre del plato: ")
        nomb = input()
        for plato in Rancio.listaPlatos:
            if plato.Nombre == nomb:
                Rancio.eliminarPlato(plato)
    elif dato == 10:
        print("ID del plato: ")
        id = input()
        for pedido in Rancio.listaPedidos:
            if pedido.IDpedido==id:
                Rancio.eliminarPedido(pedido)
    elif dato == 11:
        print("ID del pedido: ")
        pedi2=input()
        for p in Rancio.listaPedidos:
            if p.IDpedido == pedi2:
                print("1) Modificar fecha de entrega: ")
                print("2) Modificar DNI del comprador: ")
                print("3) Modificar hora de entrega: ")
                print("4) Modificar Plato: ")
                print("5) MOdificar confirmacion de entrega: ")
                daton = input()
                if daton == 1:
                    print("Nueva entrega: ")
                    p.FechaEntrega=input()
                if daton == 2:
                    print("Nueva DNI del comprador: ")
                    p.Comprador=input()
                if daton == 3:
                    print("Nueva hora de entrega: ")
                    p.HoraEntrega=input()
                if daton == 1:
                    print("Nuevo plato: ")
                    p.Plato=input()
                if daton == 1:
                    print("Nueva confirmacion de entrega: ")
                    p.Entregado=input()


