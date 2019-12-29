z=[1,5,2]
f=[1,7,3]
q=[2,1]
j=[1,2,2,5]
#esConjunto: list -> bool
#se verifica si la lista ingresada es un conjunto, si lo es da True
#ejemplo: esConjunto(z) -> True
def esConjunto(a):
    for i in a:
        if a.count(i)>1:
            return False
    return True
assert esConjunto(z)
assert esConjunto(q)
assert esConjunto(f)
assert not esConjunto(j)
#pertenece: objeto list -> bool
#se verifica si el objeto en cuestion pertenece a la lista, si lo es da True
#Ejemplo: pertenece(2,z)->True
def pertenece(n,l):
	for i in l:
		if i==n:
			return True
	return False
#union: list list -> list
#la funcion recibe dos conjuntos y entrega un tercero con los elementos de ambos
#ejemplo: union(z,q)->[1 5 2]
def union(a,b):
    assert esConjunto(a)
    assert esConjunto(b)
    y=a
    for i in b:
        if pertenece(i,y)==False:
            y.append(i)
    return y
assert union([1,2,3],[3,4]) == [1, 2, 3, 4]
assert union([2],[3,5]) == [2,3,5]
assert union([1,2,4],[1,2,4]) == [1,2,4]
#interseccion: list list -> list
#la funcion recibe dos listas/conjuntos y entrega una con los elementos que pertenecen a ambas
#ejemplo:inter(z,q)->[1,2]
def interseccion(a,b):
    assert esConjunto(a)
    assert esConjunto(b)
    h=[]
    for i in b:
        if pertenece(i,a):
            h.append(i)
    return h
assert interseccion([1,2,4],[1,2,4]) == [1,2,4]
assert interseccion([1,2,3],[7,6,8]) == []
assert interseccion([1,3,2,5],[3,5]) == [3,5]
#sub: list list -> bool
#verifica si un conjunto(a) es sub conjunto del otro(b)
#ejemplo:sub(1,z)->True
def sub(a,b):
    assert esConjunto(a)
    assert esConjunto(b)
    for i in a:
        if not pertenece(i,b):
            return False
    return True
assert sub(q,z)
assert not sub(z,q)
assert not sub(q,f)
assert not sub([1,2,3,4],[7])
#comparar: list list -> int
#recibe dos listas/conjuntos 0 si a=b,-1 si a C b,1 si a כ b y False si son conjuntos disjuntos
#ejemplo:comparar(z,q)->False
def comparar(a,b):
    assert esConjunto(a)
    assert esConjunto(b)
    if sub(a,b) and sub(b,a):
        return 0
    elif sub(a,b):
        return -1
    elif sub(b,a):
        return 1
    else:
        return False
assert comparar([1,2,3,4],[7]) == False
assert comparar([1,2,3,4],[7,4]) == False
assert comparar([1,2,3,4],[1,4]) == 1
assert comparar([1],[1,4]) == -1
assert comparar([1,4],[1,4]) == 0
assert comparar(z,q) == 1
#cardinal: list -> int
#cuenta los elementos de un conjunto a
#ejemplo:cardinal(q)-> 2
def cardinal(a):
    assert esConjunto(a)
    return len(a)
assert cardinal([1,2,3,4]) == 4
assert cardinal([1,5]) == 2
assert cardinal([7]) == 1
assert cardinal([1,2,22]) == 3
#resta: list list -> list
# se tienen dos conjuntos y se le quitan al conjunto a los elementos de b que estan en a
#ejemplo:resta(z,q)->[5]
def resta(a,b):
    assert esConjunto(a)
    assert esConjunto(b)
    for i in b:
        y=a
        if pertenece(i,a):
            y.remove(i)
    return y
assert resta([1,5,2],[1,2]) == [5]
assert resta([1,2],[1,5,2]) == []
assert resta([2,3,4],[1,5]) == [2,3,4]
#grabar: list str ->
#escribe en un archivo(str sin el .txt, mas comodo) los elementos de una lista ingresada
def grabar(x,nombreArchivo):
        assert type(x) == list
        assert esConjunto(x)
        assert type(nombreArchivo) == str
        A=open(nombreArchivo + ".txt","w")
        for linea in x:
                A.write(linea+"\n")
        A.close()
#leer:str -> list
#recibe un str(sin el .txt) y escribe las lineas como listas del archivo

def leer(nombreArchivo):
        assert type(nombreArchivo) == str
        A=open(nombreArchivo + ".txt","r")
        L=[]
        for linea in A:
                nuevaLinea = linea[0:-1]
                L.append(nuevaLinea)
        return L
        A.close()

