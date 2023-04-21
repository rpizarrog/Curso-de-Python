# Módulo para procesar diccionarios

import random as rn

rn.seed(2023)

# Mostrar un saludo simple
def saludo_simple():
    print("Saludos. Estamos en el módulo procesar_diccionarios. Hola ")

# Mostrar un saludo recibiendo y utilizando un argumento nombre
def saludo_nombre(nombre):
    print("Saludos. Estamos en el módulo procesar_diccionarios: Hola ", nombre)


# Devolver un saludo recibiendo y utilizando un argumento nombre
def saludo_retorno(nombre):
    return "Regresamos. estamos en el módulo procesar_diccionarios. Hola, " + nombre


def ordenar_diccionario(diccionario):
    claves = diccionario.keys()
    claves_ordenadas = sorted(claves)
    diccionario_ordenado = {}
    for clave in claves_ordenadas:
        diccionario_ordenado[clave] = diccionario[clave]
    return diccionario_ordenado

# Devuelve una lista de los que son Femeninos o Masculinos
def filtrar_genero(diccionario, gen):
    # - Extraer del diccionario solo los elementos cuyo elemento género sea 'F' o 'M' y convertir esta extracción a una lista. Iterar
    lista_femeninos = []
    lista_masculinos = []

    for dicc in diccionario:
        if diccionario[dicc]["genero"] == 'M':
            lista_masculinos.append(diccionario[dicc])
        if diccionario[dicc]["genero"] == 'F':
            lista_femeninos.append(diccionario[dicc])

    if gen == 1:
        return lista_masculinos
    if gen == 2:
        return lista_femeninos
    
# Devuelve una lista deacuerdo con la CARRERA
def filtrar_carrera(diccionario, carr):
    # - Extraer del diccionario solo los elementos cuyo segú la carrer 1-SISTEMAS 2-TIC 3-INFORMATICA  
    # esta extracción a una lista. Iterar Y DEVOLVER LA LISTA
    lista_sis = []
    lista_tic = []
    lista_inf = []

    for dicc in diccionario:
        if diccionario[dicc]["carrera"] == 'SISTEMAS':
            lista_sis.append(diccionario[dicc])
        elif diccionario[dicc]["carrera"] == 'TIC':
            lista_tic.append(diccionario[dicc])
        else:  
            lista_inf.append(diccionario[dicc])

    if carr == 1:
        return lista_sis
    if carr == 2:
        return lista_tic
    if carr == 3:
        return lista_inf
    
    
def crear_diccionario_personas(cuantos):
    nombres = ['ROBERTO', 'MIGUEL', 'GUILLERMO', 'DAVID', 'RICARDO', 'JOSÉ', 'CARLOS', "TOMÁS", 'CRISTIAN', 'DANIEL', 
           'MATEO', 'ANTONIO', 'DONALD', 'MARCO', 'PABLO', 'ANDRES', 'JORGE', 'RUBEN', 'KEVIN', 'RANDY', 
           'BRYANT', 'EDUARDO', 'OSCAR', 'LUIS', 'ALFREDO', 
           'MARY', 'PATRICIA', 'JENNY', 'ELIZABETH', 'LINDA', 'BARBARA', 'SUSANA', 'JESSICA', 'MARGARITA', 'SARA', 
           'KAREN', 'NANCY', 'ELISA', 'BETY', 'LUCY', 'GUILLE', 'FATIMA', 'LEO', 'DONNA', 'EMILIA', 
           'CAROLINA', 'MICHELLE', 'AMANDA', 'GLORIA', 'ADRIANA']
    generos = ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M',
           'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M',
           'M', 'M','M', 'M', 'M',
           'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
           'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
           'F', 'F', 'F', 'F', 'F']


    carreras = ["SISTEMAS", "TIC", "INFORMATICA", "ARQUITECTURA", "QUIMICA"]

    clases = ["ALTA", "MEDIA", "BAJA"]
    
    # Crear el diccionario con claves aleatorias y valores aleatorios
    personas = {}
    for i in range(cuantos):
        clave = rn.randint(1000, 2000)
        
        # Nombre y genero aleatorio
        n = rn.randint(0, 49)
        nombre = nombres[n]
        genero = generos[n]
    
        # edad aleatorio
        edad = rn.randint(18, 25)
    
        # carrera
        n = rn.randint(0, 4)
        carrera = carreras[n]
    
        # promedio
        # edad aleatorio
        promedio = rn.randint(70, 100) 
    
        # clase economica
        # carrera
        n = rn.randint(0, 2)
        clase = clases[n]
    
        personas[clave] = {"nombre": nombre, "edad": edad, "carrera": carrera, "promedio": promedio, "clase":clase}

    # Imprimir el diccionario
    # print(personas)
    return(personas)

    
    
    
        
