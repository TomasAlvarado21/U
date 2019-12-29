#largo: int -> int
#la funcion un numero entero y esta devuelve la cantidad de digitos que posee
#ejemplo: largo(123) -> 3 y largo(31) ->2
def largo(x):
	assert type(x) == int
	return len(str(x))  
#decimal: int int -> int
#convierte a decimal numero expresado en una base
#ej: decimal(215,8) -> 141
#ej: decimal(1,2) -> 1
#ej: decimal(313,5)-> 83
#ej: decimal(2022,4)->138
def decimal(x,y): 
  assert x>=0
  assert y>=2 and 10 >= y
  assert type(x)==int and type(y)==int
  if largo(x) == 1:
    return x
  else:
   return (x/(10**(largo(x) - 1)))*(y**(largo(x)-1)) + decimal((x - (x/(10**(largo(x)-1)))*(10**(largo(x)-1))) , y)
assert decimal(313,5) == 83
assert decimal(2022,4) == 138
assert decimal(1,2) == 1
#esCorrecto: int int -> bool
#la funcion recibe dos numeros e indica True si el primero corresponde a la base
#del segundo, sino da False
#ejemplo:esCorrecto(234,5)-> True y esCorrecto(237,4)->False
def esCorrecto(x,y):
  assert x >= 0
  assert y>=2 and 10 >= y
  assert type(x)==int and type(y)==int
  if x == 0:
    return True
  elif x/(10**(largo(x)-1)) >= y:
    return False
  else:
    return esCorrecto(x - (x/(10**(largo(x)-1)))*(10**(largo(x)-1)), y)
assert esCorrecto(234,5) == True
assert esCorrecto(237,4) == False
#base: int int -> int
#la funcion recibe un numero en formato de base decimal y devuelve en base dada (y)
#ejemplo:base(314,7)->626 y base(525,9)->643
def base(x,y):
  assert x>=0
  assert type(x)==int and type(y)==int
  if x/y ==0:
    return x%y
  else:
    return 10*(base(x/y,y)) + x%y
assert base(314,7) == 626
assert base(525,9) == 643
