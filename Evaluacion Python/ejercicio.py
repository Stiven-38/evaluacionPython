class Votaciones:
    def __init__(self):  
        # Listas para almacenar votantes admitidos y rechazados
        self.votantesAdmitidos = [] 
        self.votantesRechazados = []
        
        # Lista de candidatos
        self.candidatos = ["camila", "stiven", "melissa", "voto en blanco"]
        
        # Contadores de votos admitidos y rechazados
        self.contadorVotos = 0 
        self.contadorVotosR = 0

    def ingresoVotantes(self):
        # Funcion para ingresar votantes
        continuarIngreso = True 
        while continuarIngreso:
            # Solicitar información del votante
            nombre = input("Ingresa su nombre: ")
            id = int(input("Ingrese su id: "))
            
            # Mostrar la lista de candidatos y solicitar el voto
            print(f"Lista de candidatos {self.candidatos}")
            voto = input("Ingrese su voto (recuerde que hay ¡voto en blanco!): ").lower() 
            
            # Verificar si el voto es valido y actualizar las listas y contadores
            if voto in self.candidatos:
                print("Gracias por Votar")
                self.votantesAdmitidos.append(f"Nombre Aprendiz: {nombre}, ID: {id}, Voto: {voto}")
                self.contadorVotos += 1
            else:
                print("Lo siento, no puedes votar")
                motivoRechazo = "no existe el candidato en el sistema"
                self.votantesRechazados.append(f"Aprendiz {nombre}, ID: {id}, Voto: {voto}, Motivo de anulación del voto: {motivoRechazo}")
                self.contadorVotosR += 1
            
            # Preguntar si desea ingresar otro votante
            respuesta = input("¿Desea votar otro aprendiz diferente? (recuerda que solo puede votar 1o veces) (si/no): ")
            continuarIngreso = respuesta.lower() == 'si'

    def generarReporte(self):
        # Funcion para generar un informe de votacion
        print(f"\nReporte de aprendices que han votado:")
        for votante in self.votantesAdmitidos:
            print(votante)
        
        print("\nReporte de Aprendices Rechazados:")
        for asistente in self.votantesRechazados:
            print(asistente)
        
        print(f"\nTotal de votos contabilizados: {self.contadorVotos}")
        print(f"Reporte votos anulados: {self.contadorVotosR}")

# Crear una instancia de la clase Votaciones
votos = Votaciones()

# Llamar al metodo para ingresar votantes
votos.ingresoVotantes()

# Llamar al metodo para generar el reporte
votos.generarReporte()
