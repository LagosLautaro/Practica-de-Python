lista_nombres = ['Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina']
lista_notas1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
lista_notas2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#punto A)

lista_unica =  list(map(lambda nombre,nota1,nota2: {"Nombre": nombre, "Nota 1": nota1, "Nota 2": nota2},lista_nombres,lista_notas1,lista_notas2))


#punto B)
print()

lista_promedio = list(map(lambda lista : (lista["Nombre"] , (lista["Nota 1"] + lista["Nota 2"])//2),lista_unica))


print ("Lista de promedios: ")
for i in range(len(lista_promedio)):
    print(lista_promedio[i])

#Punto C)
print()

nombres,promedio = list(zip(*lista_promedio))
print(nombres)
print(promedio)
print()
promedio_general = float(sum(promedio)/len(lista_promedio))

print(f" El promedio del curso es {promedio_general}")

#punto D)
print()


nota_maxima = max(promedio)

def  buscar_alumno_lista(nota,lista):
     for i in range(len(lista)):
         if lista[i][1] == nota:
             return lista[i]


nota_mas_alta = buscar_alumno_lista(nota_maxima,lista_promedio)
print(f" El alumno con el promedio mas alto es {nota_mas_alta[0]} con {nota_mas_alta[1]}")

#punto E)
print()


def buscar_alumno_dicc(nota,lista):
    for i in range(len(lista)):
         if lista[i]["Nota 1"] == nota or lista[i]["Nota 2"] == nota:
             alumno = (lista[i]["Nombre"],nota)
             return alumno
        
nota_minima = min(lista_notas1 + lista_notas2)
nota_mas_baja = buscar_alumno_dicc(nota_minima,lista_unica)
print(f" El alumno con la nota mas baja es {nota_mas_baja[0]} con {nota_mas_baja[1]}")