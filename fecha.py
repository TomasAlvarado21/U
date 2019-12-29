import estructura
def bisiesto(x):
   assert type(x)==int and x>=0 #precondicion
   return (x%4==0 and x%100!=0) or (x%400==0)
assert bisiesto(2020)     #prueba     
assert not bisiesto(2019) #prueba

estructura.crear("Fecha", "dia mes ano")
#validar: int -> bool
#funcion que verifica si la fecha es correcta
#ej: validar(03092000) -> True
#ej: validar(29022001) -> False
def validar(Fecha):
  if Fecha.mes == 4 or Fecha.mes == 6 or Fecha.mes == 9 or Fecha.mes == 11:
      if 1<= Fecha.dia <= 30:
        return True
      else: 
        return False
  if Fecha.mes == 1 or Fecha.mes == 3 or Fecha.mes == 5 or Fecha.mes == 7 or Fecha.mes ==8 or Fecha.mes == 10 or Fecha.mes == 12:
      if 1<= Fecha.dia <= 31:
        return True
      else: return False
  if Fecha.mes == 2:   
    if bisiesto(Fecha.ano):
      if 1<= Fecha.dia <= 29:
        return True
      else: return False
    else:
      if 1<= Fecha.dia <= 28:
        return True
      else: return False
  else: return False
#Test
assert validar(Fecha(29,02,2004))     #ano bisiesto
assert not validar(Fecha(29,02,2003))
assert validar(Fecha(9,03,2000))
assert not validar(Fecha(31,04,1867))

#efe: int -> Fecha
#funcion que recibe un entero ddmmaaaa y entrega una fecha
#ej: efe(9032000) -> Fecha(dia=9, mes=3, ano=2000)
#ej: efe(31122019) -> Fecha(dia=31, mes=12, ano=2019)
def efe(F):
  eFe = Fecha(F/(10**6),F%(10**6)/(10**4),F%(10**4))
  assert validar(eFe) #precondicion
  return eFe
#Test
assert efe(3092000) == Fecha(dia=3, mes=9, ano=2000)
assert efe(31122019) == Fecha(dia=31, mes=12, ano=2019)
assert efe(7081815) == Fecha(dia=7, mes=8, ano=1815)

#entero: Fecha -> int 
#funcion que recibe una fecha y entrega un entero ddmmaaaa
#ej: entero(Fecha(dia=9, mes=3, ano=2000)) -> 9032000
#ej: entero(Fecha(dia=31, mes=12, ano=2019)) -> 31122019
def entero(F):
  return F.dia*10**6 + F.mes*10**4 + F.ano
#Test
assert entero(Fecha(dia=9, mes=3, ano=2000)) == 9032000
assert entero(Fecha(dia=31, mes=12, ano=2019)) == 31122019
assert entero(Fecha(dia=7, mes=8, ano=1815)) == 7081815

#siguente: Fecha -> int 
#funcion que recibe una fecha y entrega el dia siguente
#ej: siguente(Fecha(dia=9, mes=3, ano=2000)) -> 10032000
#ej: siguente(Fecha(dia=31, mes=12, ano=2019)) -> 1012020
def siguiente(Fe):
   if Fe.mes ==12:
      if Fe.dia == 31:
         return 1*10**6 + 1*10**4 + (Fe.ano+1)
   if Fe.mes == 4 or Fe.mes == 6 or Fe.mes == 9 or Fe.mes == 11:
      if Fe.dia == 30:
         return 1*10**6 + (Fe.mes+1)*10**4 + Fe.ano
      else:
         return (Fe.dia+1)*10**6 + Fe.mes*10**4 + Fe.ano
   if Fe.mes == 1 or Fe.mes == 3 or Fe.mes == 5 or Fe.mes == 7 or Fe.mes ==8 or Fe.mes == 10:
      if Fe.dia == 31:
         return 1*10**6 + (Fe.mes+1)*10**4 + Fe.ano
      else:
         return (Fe.dia+1)*10**6 + Fe.mes*10**4 + Fe.ano
   if Fe.mes == 2: 
    if bisiesto(Fe.ano):
      if Fe.dia == 29:
        return 1*10**6 + (Fe.mes+1)*10**4 + Fe.ano
      else:
         return (Fe.dia+1)*10**6 + Fe.mes*10**4 + Fe.ano
    else:
      if Fe.dia== 28:
        return 1*10**6 + (Fe.mes+1)*10**4 + Fe.ano
      else:
         return (Fe.dia+1)*10**6 + Fe.mes*10**4 + Fe.ano
#Test
assert siguiente(Fecha(dia=31, mes=12, ano=2019)) == 1012020
assert siguiente(Fecha(dia=9, mes=03, ano=2000)) == 10032000
assert siguiente(Fecha(dia=28, mes=02, ano=1996)) == 29021996

#aString: Fecha -> str
#funcion que entrega la fecha de la forma DD/MM/AAAA
#ej: aString(Fecha(dia=9, mes=3, ano=2000)) -> 9/3/2000
#ej: aString((Fecha(dia=31, mes=12, ano=2019)) -> 31/12/2019
def aString(F):
  return str(F.dia)+"/"+str(F.mes)+"/"+str(F.ano)
#Test
assert aString(Fecha(dia=9, mes=3, ano=2000)) == "9/3/2000"
assert aString(Fecha(dia=31, mes=12, ano=2019)) == "31/12/2019"
assert aString(Fecha(dia=7, mes=8, ano=1815)) == "7/8/1815"

#comparar: Fecha(1) Fecha(2) -> int
#funcion que compara dos fechas y devuelve -1 si F1 es mayor, 0 si son iguales o 1 si F2 es mayor.
#ej:comparar(Fecha(dia=29, mes=2, ano=2000),Fecha(dia=9, mes=3, ano=2001)) -> 1
#ej:comparar(Fecha(dia=29, mes=12, ano=2000),Fecha(dia=9, mes=3, ano=2000)) -> -1
#ej:comparar(Fecha(dia=9, mes=8, ano=1969),Fecha(dia=9, mes=8, ano=1969)) -> 0
def comparar(F1,F2):
    assert validar(F1) #precondicion
    assert validar(F2) #precondicion
    if F1.dia==F2.dia and F1.mes==F2.mes and F1.ano==F2.ano:
        return 0
    if F1.mes==F2.mes and F1.ano==F2.ano:
        if F1.dia>F2.dia:
            return -1
        else:
            return 1
    if F1.ano==F2.ano:
        if F1.mes>F2.mes:
            return -1
        else:
            return 1
    if F1.ano>F2.ano:
        return -1
    if F1.ano<F2.ano:
        return 1
#Test
assert comparar(Fecha(dia=9, mes=3, ano=2000),Fecha(dia=9, mes=12, ano=2019)) == 1
assert comparar(Fecha(dia=9, mes=3, ano=2000),Fecha(dia=1, mes=3, ano=2000)) == -1
assert comparar(Fecha(dia=9, mes=3, ano=2000),Fecha(dia=9, mes=3, ano=2000)) == 0

#diferencia: Fecha Fecha -> int 
#funcion que calcula la diferencias en anos entre dos fechas
#ej:diferencia(Fecha(dia=9, mes=8, ano=1969),Fecha(dia=9, mes=7, ano=1969)) -> 0
#ej:diferencia(Fecha(dia=9, mes=8, ano=1969),Fecha(dia=9, mes=7, ano=969)) -> 999
def diferencia(F1,F2):
   if comparar(F1,F2) == 0:
      return 0
   elif comparar(F1,F2) == -1:
      if F1.ano == F2.ano:
         return F1.ano - F2.ano
      else:
         if F1.mes == F2.mes:
            if F1.dia < F2.dia:
               return F1.ano - F2.ano -1
            else:
               return F1.ano - F2.ano
         elif F1.mes > F2.mes:
            return F1.ano - F2.ano
         else:
            return F1.ano - F2.ano -1
   else:
      if F2.ano == F1.ano:
         if F2.mes == F1.mes:
            return F2.ano - F1.ano
         else:
            return F2.ano - F1.ano
      else:
         if F2.mes == F1.mes:
            if F2.dia < F1.dia:
               return F2.ano - F1.ano - 1
            elif F2.dia == F1.dia:
               return F2.ano - F1.ano
            else:
               return F2.ano - F1.ano
         elif F2.mes > F1.mes:
            return F2.ano - F1.ano
         else:
            return F2.ano - F1.ano - 1
assert diferencia(Fecha(dia=9, mes=8, ano=1969),Fecha(dia=9, mes=8, ano=969)) == 1000
assert diferencia(Fecha(dia=9, mes=8, ano=1969),Fecha(dia=9, mes=7, ano=1969)) == 0
assert diferencia(Fecha(dia=9, mes=8, ano=1969),Fecha(dia=9, mes=7, ano=2019)) == 49
assert diferencia(Fecha(dia=9, mes=8, ano=1969),Fecha(dia=9, mes=7, ano=969)) == 1000
assert diferencia(Fecha(dia=20, mes=8, ano=1999),Fecha(dia=10, mes=9, ano=2019)) == 20
assert diferencia(Fecha(dia=10, mes=9, ano=2019),Fecha(dia=20, mes=8, ano=1999)) == 20
