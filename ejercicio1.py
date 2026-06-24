estudiantes = []

try:
    n = int(input("¿Cuántos estudiantes deseas registrar?\n"))
except ValueError:
    print("Ingresaste un valor invalido, la policia va directo a tu casa malhechor. ")
    n = 0

def registrar_estudiante():
            while True:
                rut = input("Ingrese rut a registrar sin puntos ni guión.\n").strip().upper()
                if len(rut) == 9 or len(rut) == 8:  
                    dv = rut[-1]
                    cuerpo = rut[:-1]
                    if cuerpo.isdigit():
                        rut_limpio = f"{int(cuerpo):,}-{dv}".replace(",",".").rjust(12)
                        break
                    else:
                        print("El rut ingresado fue invalido por favor intente nuevamente")
                        continue
                else:
                    print("El rut ingresado es erroneo, ingrese uno correcto")
                    continue

            nombre = input("Ingrese ambos nombres y apellidos del alumno\n").strip().title()
            
            while True:
                try:
                    edad = int(input("Ingrese la edad del alumno.\n"))
                    break
                except ValueError:
                    print("Ingrese una edad en números enteros por favor.")
            
            carrera = input("Ingrese la carrera que estudia el alumno.\n").strip().title()

            registro = {"rut": rut_limpio,
                        "nombre": nombre,
                        "edad": edad,
                        "carrera": carrera}
            
            estudiantes.append(registro)


for e in range(n):
    print(f"Se registrarán: {n} estudiantes.")
    print(f"Actualmente registrando al estudiante {e+1}")
    registrar_estudiante()

if n > 0:
    print("-----LISTA FINAL DE ESTUDIANTES-----")
    for est in estudiantes:
        print(f"RUT: {est['rut']} | Nombre: {est['nombre']} | Edad: {est['edad']} | Carrera: {est['carrera']}")