import Tarea1
#convertirBases: --> int
#la funcion va conviertiendo un numero entregado de una base que la persona da en
#una base especifica a otra base requerida y se le entrega el numero en la base nueva
#ejemplo:convertirBases()
#Convertir n° desde base1 a base2
#base1 ? 5
#n° ? 25
#base incorrecta
#otra conversión (si/no)? Si
#Convertir n° desde base1 a base2
#base1 ? 7
#n° ? 453
#base2 ? 4
#n° =  3222
#otra conversión (si/no)? no
def convertirBases():
    print "Convertir n° desde base1 a base2"
    base1 = input("base1 ? ")
    if base1 > 9 or 2 > base1:
        print "base incorrecta"
        x = raw_input("otra conversión (si/no)? ")
        if x == "si" or x == "Si":
            return convertirBases()
        else: return
    num = input("n° ? ")
    if not Tarea1.esCorrecto(num,base1):
        print "numero incorrecto"
        x = raw_input("otra conversión (si/no)? ")
        if x == "si" or x == "Si":
            return convertirBases()
        else: return
    base2 = input("base2 ? ")
    print "n° =  " , Tarea1.base((Tarea1.decimal(num,base1)),base2)
    x = raw_input("otra conversión (si/no)? ")
    if x == "si" or x == "Si":
        return convertirBases()
    else: return
    
    
#Menor: None -> None
#la funcion no recibe ningun parametro, y mediante un input se entrega el numero en decimal 
#y se entrega el menor de todos los ingresados
#ejemplo:Menor()
#n°? 11012
#decimal = 13
#n°? 313
#numero incorrecto
#n°? 541
#base incorrecta
#n°? 1023
#decimal= 11
#n°? 308
#decimal= 
#n°? 0 (fin de datos)
#menor: base= 3 digitos = 102 decimal= 11
def Menor(inicial=True, menor=0, basemenor=10):
  num = input("nº? ")
  base = num%10
  numero = num/10
  if numero == 0:
      print "menor: base=" ,basemenor, "digitos =",Tarea1.base(menor,basemenor), "decimal=" ,menor
      return
  elif (base)<2:
    print "base incorrecta"
    return Menor(inicial,menor,basemenor)
  elif (base)>9:
    print "base incorrecta"
    return Menor(inicial,menor,basemenor)
  elif Tarea1.esCorrecto(numero,base) == False:
    print "numero incorrecto"
    return Menor(inicial,menor,basemenor)
  else:
    base10 = Tarea1.decimal(numero,base)
    print "decimal=" , base10
    if inicial:
      return Menor(False, base10, base)
    elif menor <= base10:
      return Menor(False, menor, basemenor)
    else:
      return Menor(False, base10, base)

