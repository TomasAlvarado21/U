from fecha import*
import estructura
#Parte B
#Se crea la estructura Personaje

estructura.crear("personaje", "nombre nacimiento fallecimiento")

#validarFechas personaje -> bool
#funcion que verifica si las fechas de nacimiento y defuncion de un personaje esten correctas
#ej:validarPersonaje(personaje("Tomas",Fecha(dia=9, mes=3, ano=2000),Fecha(dia=9, mes=12, ano=2019))) -> True
#ej:validarPersonaje(personaje("Jaime",Fecha(dia=18, mes=8, ano=1983),Fecha(dia=31, mes=5, ano=2001))) -> True
#ej:validarPersonaje(personaje("Jaime",Fecha(dia=15, mes=6, ano=1996),Fecha(dia=26, mes=2, ano=1970))) -> False
def validarPersonaje(P):
    assert type(P.nombre) == str
    if comparar(P.nacimiento,P.fallecimiento) == 1:
        return True
    else: return False
#test
assert validarPersonaje(personaje("Tomas",Fecha(dia=9, mes=3, ano=2000),Fecha(dia=9, mes=12, ano=2019))) == True
assert validarPersonaje(personaje("Jaime",Fecha(dia=18, mes=8, ano=1983),Fecha(dia=31, mes=5, ano=2001))) == True
assert validarPersonaje(personaje("Juan",Fecha(dia=15, mes=6, ano=1996),Fecha(dia=26, mes=2, ano=1970))) == False

#nombre personaje -> str
#funcion que entrega el nombre de un personaje
#ej:nombre(personaje("Tomas",Fecha(dia=9, mes=3, ano=2000),Fecha(dia=9, mes=12, ano=2019))) -> 'Tomas'
#ej:nombre(personaje("Jaime",Fecha(dia=18, mes=8, ano=1983),Fecha(dia=31, mes=5, ano=2001))) -> 'Jaime'
def nombre(P):
    assert validarPersonaje(P) #precondicion
    return P.nombre
#test
assert nombre(personaje("Tomas",Fecha(dia=9, mes=3, ano=2000),Fecha(dia=9, mes=12, ano=2019))) == "Tomas"
assert nombre(personaje("Jaime",Fecha(dia=18, mes=8, ano=1983),Fecha(dia=31, mes=5, ano=2001))) == "Jaime"
assert nombre(personaje("Jose",Fecha(dia=15, mes=6, ano=1996),Fecha(dia=26, mes=2, ano=2000))) == "Jose"

#nacimiento personaje -> Fecha
#funcion que entrega la fecha de nacimiento de un personaje
#ej:nacimiento(personaje("Tomas",Fecha(dia=9, mes=3, ano=2000),Fecha(dia=9, mes=12, ano=2019))) -> Fecha(dia=9, mes=3, ano=2000)
#ej:nacimiento(personaje("Jaime",Fecha(dia=18, mes=8, ano=1983),Fecha(dia=31, mes=5, ano=2001))) -> Fecha(dia=18, mes=8, ano=1983)
def nacimiento(P):
    assert validarPersonaje(P) #precondicion 
    return P.nacimiento
#test
assert nacimiento(personaje("Tomas",Fecha(dia=9, mes=3, ano=2000),Fecha(dia=9, mes=12, ano=2019))) == Fecha(dia=9, mes=3, ano=2000)
assert nacimiento(personaje("Jaime",Fecha(dia=18, mes=8, ano=1983),Fecha(dia=31, mes=5, ano=2001))) == Fecha(dia=18, mes=8, ano=1983)
assert nacimiento(personaje("Jose",Fecha(dia=15, mes=6, ano=1996),Fecha(dia=26, mes=2, ano=2000))) == Fecha(dia=15, mes=6, ano=1996)

#fallecimiento personaje -> Fecha
#funcion que entrega la fecha de fallecimiento de un personaje
#ej:fallecimiento(personaje("Tomas",Fecha(dia=9, mes=3, ano=2000),Fecha(dia=9, mes=12, ano=2019))) -> Fecha(dia=9, mes=12, ano=2019)
#ej:fallecimiento(personaje("Jaime",Fecha(dia=18, mes=8, ano=1983),Fecha(dia=31, mes=5, ano=2001))) -> Fecha(dia=31, mes=5, ano=2001)
def fallecimiento(P):
    assert validarPersonaje(P) #precondicion
    return P.fallecimiento
#test
assert fallecimiento(personaje("Tomas",Fecha(dia=9, mes=3, ano=2000),Fecha(dia=9, mes=12, ano=2019))) == Fecha(dia=9, mes=12, ano=2019)
assert fallecimiento(personaje("Jaime",Fecha(dia=18, mes=8, ano=1983),Fecha(dia=31, mes=5, ano=2001))) == Fecha(dia=31, mes=5, ano=2001)
assert fallecimiento(personaje("Jose",Fecha(dia=15, mes=6, ano=1996),Fecha(dia=26, mes=2, ano=2000))) == Fecha(dia=26, mes=2, ano=2000)

#info personaje -> str
#funcion que entrega la fecha de nacimiento, defuncion y nombre de un personaje
#ej:info(personaje("Tomas",Fecha(dia=9, mes=3, ano=2000),Fecha(dia=9, mes=12, ano=2019))) -> '9/3/2000-9/12/2019 Tomas'
#ej:info(personaje("Jaime",Fecha(dia=18, mes=8, ano=1983),Fecha(dia=31, mes=5, ano=2001))) -> '18/8/1983-31/5/2001 Jaime'
def info(P):
    assert validarPersonaje(P) #precondicion
    return aString(P.nacimiento)+"-"+aString(P.fallecimiento)+" "+P.nombre
#test
assert info(personaje("Tomas",Fecha(dia=9, mes=3, ano=2000),Fecha(dia=9, mes=12, ano=2019))) == '9/3/2000-9/12/2019 Tomas'
assert info(personaje("Jaime",Fecha(dia=18, mes=8, ano=1983),Fecha(dia=31, mes=5, ano=2001))) == '18/8/1983-31/5/2001 Jaime'
assert info(personaje("Jose",Fecha(dia=15, mes=6, ano=1996),Fecha(dia=26, mes=2, ano=2000))) == '15/6/1996-26/2/2000 Jose'

#edad personaje -> int
#funcion que entrega la edad de un personaje 
#ej:edad(personaje("Tomas",Fecha(dia=20, mes=8, ano=1999),Fecha(dia=7, mes=9, ano=2019))) -> 20
#ej:edad(personaje("Jaime",Fecha(dia=18, mes=8, ano=1983),Fecha(dia=31, mes=5, ano=2001))) -> 17
def edad(P):
    assert validarPersonaje(P) #precondicion 
    return diferencia(P.nacimiento,P.fallecimiento)
#test
assert edad(personaje("Tomas",Fecha(dia=20, mes=8, ano=1999),Fecha(dia=7, mes=9, ano=2019))) == 20
assert edad(personaje("Jaime",Fecha(dia=18, mes=8, ano=1983),Fecha(dia=31, mes=5, ano=2001))) == 17
assert edad(personaje("Jose",Fecha(dia=15, mes=6, ano=1996),Fecha(dia=26, mes=2, ano=2000))) == 3
