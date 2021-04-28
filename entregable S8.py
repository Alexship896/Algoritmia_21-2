
class Examen:
    def __init__(self, materia, calificacion):
        self.materia = materia
        self.calificacion = calificacion

    def __str__(self):
        return f'{self.materia} {self.calificacion}'

class Alumno:
 
    def __init__(self, nombre):
        self.nombre = nombre
        self.examenes = []
    
    def agregarExamen(self, nombreExamen, calificacion):
        self.examenes.append(Examen(nombreExamen, calificacion))

listaMaterias = ['Matematicas', 'Fisica', 'Historia', 'Quimica']

cristian = Alumno('cristian')
i = 0
while (i < len(listaMaterias)):
    calificacion = int(input(f'Ingrese calificacion para {listaMaterias[i]}: '))
    cristian.agregarExamen(listaMaterias[i], calificacion)  #mandar objeto examen
    i+=1 

print(f'\nExamenes de {cristian.nombre}')
for examen in cristian.examenes:
    print(examen)