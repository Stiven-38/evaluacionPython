votantes = {}

# Funcion para agregar un equipo
def agregarVotante(idVotantes,registroVotante):
    votantes[idVotantes] = {'idVotantes': idVotantes, 'registro':registroVotante}
    

# Funcion para mostrar todos los equipos
def mostrarVotantes():
    for votantes in votantes.values():
        print("ID: {}".format(votantes['ID']))
        print("registro: {}".format(votantes['registro']))
        print("-------------")


# Funcion principal que maneja el bucle y las opciones del usuario
def menu():
    while True:
        print("Opciones:")
        print("1. candidatos")
        print("2. registro de votante")
        print("3, id del votante para realizar su votacion")
        print("8. Salir")

        opcion = input("Digite la opcion que desea realizar: ")

        if opcion.lower() == '1':
            print("1. Stiven Ramirez")
            print("2. Camila Alape")
            print("3. Melissa Lopez")
        elif opcion.lower() == '2':
            idVotantes = input("Ingrese un id: ")
            registroVotante = input("ingrese su nombre: ")
            agregarVotante(idVotantes,registroVotante)
        elif opcion.lower() == '3':
            idVotantes = input("Ingrese su ID: ")
            if idVotantes in votantes:
                print("ID: {}".format(votantes[idVotantes]['ID']))
            
            else:
                print("El usted no se encuentra en la base de datos")

        elif opcion.lower() == '4':#al momento de que el usuario ponga la opcion se cerrar el bucle while
            break#se termina el bucle while
        else:
            print("La opcion que ingreso no es valida, verifique las opciones e ingrese una correcta")

    print("El programa ha terminado con exito :D.")
menu()