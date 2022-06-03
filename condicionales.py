calificacion = input("Introduce tu calificaion de la az-900: ")

calificacion = int(calificacion)

if calificacion < 700:
    print("ves por no estudiar")
elif calificacion > 1000:
    print("mentiroso")    
else :
    print("felicidades por pasar")


edad = input("Introduce tu edad: ")
edad = int(edad) 

if edad >= 18 and edad <= 100:
    print("Bienvenido al mamitas")
elif edad > 100:
    print("re ruco bro")
elif edad < 0:
    print("ni que fueras dios")
elif edad < 18:
    print("jaja re gil")