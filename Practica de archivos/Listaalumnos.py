#Crear un programa que dados una lista de alumnos y sus notas separados por comas y | (pipe), guarde en un archivo de
#texto el promedio de las notas de cada estudiantes python practica.py Juan,98,87,89,90|Jose,90,43,20,40|Pedro,70,80,89,90
"""
Juan=90
Jose=69
Pedro=60
"""

NombresDeAlumnos = ("Juan,98,87,89,90|Jose,90,43,20,40|Pedro,70,80,89,90")


listaDealumnos= NombresDeAlumnos.split("|")
archivo= open("promedios.txt","w")

#print (Lista de alumnos)
for estudiante in listaDealumnos:

   # prin (Estudiantes)
    listaDeDatos = estudiante.split(",")
    #Datos de entrada
    Nombre = listaDeDatos[0]
    nota1 = int(listaDeDatos[1])
    nota2 = int(listaDeDatos[2])
    nota3 = int(listaDeDatos[3])
    nota4 = int(listaDeDatos[4])

    promedio =(nota1 + nota2 + nota3 + nota4 ) / 4
    print(Nombre,  "=" , promedio)
    
    archivo.write(Nombre+ "="+str(promedio)+"\n")
    