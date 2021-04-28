class Person:
    '''Clase de Persona
    recibe el nombre y apellido como parametro'''
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, clave):
        super().__init__(fname , lname)
        self.__carrera = 'medicina'
        self.__clave = clave

    def getClave(self):
        return self.__clave

    def setClave(esta, clave):
        esta.__clave = clave

    def getCarrera(self):
        return self.__carrera 

    def setCarrera(esta, carrera):
        esta.__carrera = 'enfermeria'

    def printname(self):
        super().printname()
        print("Soy estudiante")

Cristian = Person('Cristian', 'Flores')
Cristian.printname()
print()
Pedro = Student('Pedro', 'Jimenez', 200977)
Pedro.printname()
print('Mi clave es:', Pedro.getClave())
print('Mi carrera es:', Pedro.getCarrera())
print()
Raquel = Student('Raquel', 'Garcia', 200896)
Raquel.printname()
Raquel.setClave(200896)
print('Mi clave es:', Raquel.getClave())
Raquel.setCarrera('Enfermera')
print('Mi carrera es:', Raquel.getCarrera())