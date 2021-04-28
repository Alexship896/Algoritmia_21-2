def datos(Nombre, ApellidoPaterno, ApellidoMaterno, clave, salon):
    datos = {}
    print(f"Este es mi nombre completo: {Nombre} {ApellidoPaterno} {ApellidoMaterno}")
    print(f"Esta es mi clave ULSA: {clave}") 
    print(f"Este es mi salón: {salon}")
    return datos
datos("Cristian", "Flores", "Bernal", "200477", "477")