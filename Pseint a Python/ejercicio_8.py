import os

cantAlumnosCargados = 0;
cantAlumnosMaxima = 10;

alumnos = [""] * 10;
notas1 = [0] * 10;
notas2 = [0] * 10;

continuar = True;

while continuar:
    os.system('cls');
    opcion = int(input("Seleccione la operacion que desea realizar:\n\n\t1. Cargar Alumno.\n\t2. Ver alumnos y sus promedios.\n\t3. Salir.\n\nOperacion: ").strip());

    os.system('cls');
    match opcion:
        case 1:
            if cantAlumnosCargados < cantAlumnosMaxima:
                nombre = input("Ingrese el nombre del alumno: ").strip();
                while nombre == "":
                    nombre = input("Error: El nombre no puede estar vacio.\nIngrese el nombre del alumno: ").strip();
                
                nota1 = float(input("Ingrese la primera nota del alumno: ").strip());
                while nota1 < 0:
                    nota1 = float(input("Error: La nota no puede ser negativa.\nIngrese la primera nota del alumno: ").strip());
                
                nota2 = float(input("Ingrese la segunda nota del alumno: ").strip());
                while nota2 < 0:
                    nota2 = float(input("Error: La nota no puede ser negativa.\nIngrese la segunda nota del alumno: ").strip());
                
                alumnos[cantAlumnosCargados] = nombre;
                notas1[cantAlumnosCargados] = nota1;
                notas2[cantAlumnosCargados] = nota2;

                cantAlumnosCargados += 1;
                print("Alumno cargado exitosamente.");
            else:
                print("Se alcanzo la capacidad maxima de alumnos.");

        case 2:
            if(cantAlumnosCargados == 0):
                print("Aun no hay alumnos cargados.");
            else:
                print("Datos alumnos: \n\n")
                for i in range(cantAlumnosCargados):
                    print(f"\t{i + 1}. {alumnos[i]}. Promedio: {(notas1[i] + notas2[i]) / 2}");

        case 3:
            continuar = False;

    if continuar:
        input("\n\nPresione Enter para continuar...")
