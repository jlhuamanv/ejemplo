def tupla():
tupla = []
for i in range(1,26):
tupla.append(i)
print tupla

def tupla_impares():
tupla = []
for i in range(1,26):
if i % 2 == 0:
tupla.append(i)
print tupla

def tupla_incremento():
tupla = []
for i in range(48,121,4):
tupla.append(i)
print tupla

def tupla_suma():
tupla = []
for i in range(1,51):
tupla.append(i)
print "TUPLA DE SUMA: "
print tupla
count = 0
for i in tupla:
count = count + i
print "METODO 1: "
print count
print "METODO 2: "
print sum(tupla)

def tupla_mult():
tupla = []
for i in range(1,21):
tupla.append(i)
print "TUPLA DE SUMA: "
print tupla
count = 1
for i in tupla:
count = count * i
print "METODO 1: "
print count

def tupla_suma_negativo():
tupla = []
for i in range(50,18,-2):
tupla.append(i)
print tupla
print sum(tupla)

def es_par():
import random
num = random.randint(0,1000)
print "NUMERO: ", num
if num % 2 == 0:
print "Es par"
else:
print "No es par"

def suma_tupla_pares_impares():
tupla = []
for i in range(0,101):
tupla.append(i)
print "TUPLA ORIGINAL: "
print tupla
tupla_pares = []
tupla_impares = []
for i in tupla:
if i % 2 == 0:
tupla_pares.append(i)
else:
tupla_impares.append(i)
print "TUPLA DE LOS PARES\n"
print tupla_pares
print "SUMA: "
print sum(tupla_pares)
print "TUPLA DE LOS IMPARES\n"
print tupla_impares
print "SUMA: "
print sum(tupla_impares)

def tupla_numeros():
import random
num1= random.randint(1,10)
num2= random.randint(10,20)
print "NUMERO 1: ", num1
print "NUMERO 2: ", num2
tupla=[]
for i in range(num1,num2+1):
tupla.append(i)
print tupla
print "Longitud de la tupla: "
print len(tupla)
tupla_pares=[]
for i in tupla:
if i % 2 == 0:
tupla_pares.append(i)
print tupla_pares
print "LONGITUD DE LA TUPLA DE PARES: "
print len(tupla_pares)
print "SUMA DE LA TUPLA DE PARES: "
print sum(tupla_pares)

def multiplos_3():
tupla=[]
for i in range(1,101):
if i % 3 == 0:
tupla.append(i)
print "TUPLA DE DIVISORES DE 3" 
print tupla
print "NUMERO DE DIVISORES DE 3: "
print len(tupla)

def multiplos_3_2():
import random
tupla = []
num = random.randint(1,101)
for i in range(1,num):
tupla.append(i)
print "TUPLA DE JUEGO: "
print tupla
tupla_multiple = []
for i in tupla:
if i % 3 == 0 and i % 2 == 0:
tupla_multiple.append(i)
print "TUPLA MULTIPLE DE DOS Y TRES: "
print tupla_multiple
print "LONGITUD DE LA CADENA: "
print len(tupla_multiple)
print "SUMA DE LA CADENA: "
print sum(tupla_multiple)

def condiciones():
import random
num1= random.randint(1,101)
num2= random.randint(1,101)
print "NUMERO 1: " , num1
print "NUMERO 2: " , num2
tupla = []
if num1 < num2: 
for i in range(num1,num2):
tupla.append(i)
print "TUPLA DE JUEGO: "
print tupla
print "SUMA DE LA TUPLA: "
print sum(tupla)
else:
print num1**2 + num2**2

#################################################################
#####################FUNCION PRINCIPAL###########################
#################################################################
def main():
print tupla()
print tupla_impares()
print tupla_incremento()
print tupla_suma()
print tupla_mult()
print tupla_suma_negativo()
print es_par()
print suma_tupla_pares_impares()
print tupla_numeros()
print multiplos_3()
print multiplos_3_2()
print condiciones()

print main()
----er0KamZ
