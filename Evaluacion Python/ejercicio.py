class Votaciones:
    def __init__(self):  
        self.votantesAdmitidos = [] 
        self.votantesRechazados = []
        self.candidatos = ["camila", "stiven", "melissa", "voto en blanco"]
        self.contadorVotos = 0 
        self.contadorVotosR = 0

    def ingresoVotantes(self):
        continuarIngreso = True 
        while continuarIngreso:
            nombre = input("Ingresa su nombre: ")
            id = int(input("Ingrese su id: "))
            print(f"Lista de candidatos {self.candidatos}")
            voto = input("Ingrese  su voto (recuerde que hay ¡voto en blanco!): ").lower() 
            if  voto in self.candidatos :
                print("Gracias por Votar")
                self.votantesAdmitidos.append(f"Nombre Aprediz: {nombre}, id: {id}, Su voto a sido: {voto}")
                self.contadorVotos += 1
            else:
                print("Lo siento no puedes votar")
                motivoRechazo = "no existe el canditado en el sistema"
                self.votantesRechazados.append(f"Aprendiz {nombre}, de ID: {id}, a votado por: {voto}, Motivo anulacion del voto: {motivoRechazo}")
                self.contadorVotosR += 1
respuesta = input("¿Desea votar otro aprendiz diferente?(recuerda que solo puede votar 2 veces) (si/no): ")
continuarIngreso = respuesta.lower() == 'si' 
def generarReporte(self):
        print(f"\nReporte de aprendices que han votado:")
        for votante in self.votantesAdmitidos:
            print(votante)
        print("\nReporte de Asistentes Rechazados:")
        for asistente in self.votantesRechazados:
            print(asistente)
        print(f"\nTotal de votos contabilizados: {self.contadorVotos}")
        print(f"Reporte votos anullados: {self.contadorVotosR}")

votos = Votaciones()
votos.ingresoVotantes()
votos.generarReporte()