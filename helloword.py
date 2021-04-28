#un programa que guarde datos, realice ciclos y haga consultas
class Usuario:
    def __init__(self, clave, nombre, apellido, correo, telefono):
        self.clave = clave
        self.apellido = apellido
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
    def setClave(self, clave):
        self.clave = clave
    def getClave(self):
        return self.clave
    def getAtributes(self):
        return f'nombre: {self.nombre}, apellido: {self.apellido}, correo: {self.correo}, telefono; {self.telefono}'
    def __str__(self):
        return self.nombre + '' +self.apellido
    
if __name__ =='__main__': #para hacer un diccionario
    baseDatos = {}

    rodrigo = Usuario(17, 'Rodrigo', 'Perez', 'rp@gmail.com', 5548192634)
    juan = Usuario(18,'Juan', 'Alcala', 'juan.a@gmail.com', 5519263485)
    cristian = Usuario(19, 'Cristian', 'Flores', 'eloygarcia896@hotmail.com', 5586113009)
    raquel = Usuario(20, 'Raquel', 'Garcia', 'elodiagar@gmail.com', 5519511700)
    antonio = Usuario(21, 'Antonio', 'Bernal', 'juanbernal@hotmail.com', 5547537953)

    baseDatos [rodrigo.getClave()] = rodrigo
    baseDatos [juan.getClave()] = juan
    baseDatos [cristian.getClave()] = cristian
    baseDatos [raquel.getClave()] = raquel
    baseDatos [antonio.getClave()] =antonio

    salir = False

    while(salir == False):
        print ('Bienvenidx, seleccione una opcion.')
        print('1. Busqueda de usuario\n2. Añadir usuario\n3. Modificar usuario\n4. Eliminar usuario\n5. Salir')
        opcion = int(input('Opcion: '))

        if opcion == 1: #búsqueda de ususario
            clave = int(input('Clave: '))

            if clave in baseDatos:
                print (print (baseDatos[clave].getAtributes()))
            else: 
                print ('Usuario no encontrado')
        
        if opcion == 2: #añadir usuario
            clave = int(input('Clave: '))
            nombre = input('Nombre: ')
            apellido = input ('Apellido: ') 
            correo = input('Correo: ') 
            telefono = int(input('Telefono: '))

            if clave in baseDatos:
                print('Ya existe ese usario')
            else: 
                baseDatos [clave]= Usuario(clave, nombre, apellido, correo, telefono)
        
        if opcion == 3: #modificar usuario
            clave = int(input('Ingrese su clave: '))
            
            if clave in baseDatos:
                print(baseDatos.getAtributes())
                nombre = input('Nombre: ')
                apellido = input('Apellido: ')
                correo = input('Correo: ')
                telefono = int(input('Telefono: '))

                baseDatos[clave].nombre = nombre #esto es para guardarlo en la base de datos
                baseDatos[clave].apellido = apellido
                baseDatos[clave].correo = correo
                baseDatos[clave].telefono = telefono

            else:
                print('Usuario no encontrado')
        
        if opcion == 4: #eliminar usuario
            clave = int(input('Dijite la clave: '))
            
            if clave in baseDatos:
                print(print(baseDatos[clave].getAtributes()))
                print(f'¿Estas seguro que quieres eliminar este usuario {clave}?\n1. Si\n2. No')
                opcion = int(input('dijite la opcion : '))
                if opcion == 1:
                    del baseDatos[clave]
                    print('Usuario eliminado')
                else:
                    print(f'No se elimino usuario {clave}')
                    #f=nos da la variable
        
        if opcion == 5:
            salir = False
        print(f'\nBase de datos: {baseDatos}\n')