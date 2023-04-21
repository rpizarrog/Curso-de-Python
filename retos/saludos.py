def saludo():
    print ("Hola desde saludo")
           
def saludo_arg(nombre):
    print("Hola desde saludo arg", "Hola ", nombre)
    
def saludo_devuelve(nombre):
    return "Regresa un valor desde saludo_devuelve"+"Hola:"+nombre


def crear_diccionario():
    personas = {"1000": {"nombre":"RUBEN", "edad":25, "estado":"DURANGO", "genero": 'M'},
            "1002": {"nombre":"JORGE", "edad":26, "estado":"CHIHUAHUA", "genero": 'M'},
            "1020": {"nombre":"MARY", "edad":20, "estado":"DURANGO", "genero": 'F'}, 
            "1010": {"nombre":"MAYELA", "edad":22, "estado":"CHIHUAHUA", "genero": 'F'}, 
            "1012": {"nombre":"MAYRA", "edad":22, "estado":"DURANGO", "genero": 'F'} }

    return personas
    
