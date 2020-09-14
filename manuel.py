"""lalo = input("dame la edad")
lalo2 = input("dame edad 2")

if(lalo<lalo2):
	print("rafa se ka come")
elif(lalo2<lalo):
	print("rafa es gay")
else:
	print("jajaja")
"""
"""base = int(input("dame un numero"))
altura = int(input("dame un segundo numero"))

area = base*altura/2
print(area)"""
import math
from datetime import date
from datetime import datetime
import time
today = date.today()
print(today)
now = str(datetime.now())
print(now)
no = "no"
si = "si"
realizar_otra_vez = "si"
while si == realizar_otra_vez:
	operacion = input("que lado deceas obtener")
	respuesta_a = "cateto_a"
	respuesta_b = "cateto_b"
	respuesta_c = "hipotenusa"
	if(operacion == respuesta_a):
		cateto_b = int(input("dame el valor de cateto_b"))
		hipotenusa = int(input("dame valor de hipotenusa"))
		resultado_1 = math.sqrt(hipotenusa**2 - cateto_b**2)
		print(resultado_1)
		
	elif(operacion == respuesta_b):	
		cateto_a = int(input("dame el valor de cateto_a"))
		hipotenusa = int(input("dame el valor de hipotenusa"))
		resultado_2 = math.sqrt(hipotenusa**2 - cateto_a**2)
		print(resultado_2)
		
	elif(operacion == respuesta_c):
		cateto_a = int(input("dame el valor de cateto_a"))
		cateto_b = int(input("dame el valor de cateto_b"))
		resultado_3 = math.sqrt(cateto_a**2 + cateto_b**2)
		print(resultado_3)

	realizar_otra_vez = input("desea realizar otra operacion")
	if(realizar_otra_vez == no):
		print("adios" +" "+ now)
		#manuel
		#lalo
		#jajjaja 