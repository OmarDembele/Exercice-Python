#LES FONCTIONS
"""""
#EXO2
from math import *
def cube(x):
	y=x*x*x
	return y

def volsphere(r):
	b=4*pi*cube(r)/3
	return b


rayon=int(input("saisir le rayon\t"))
v=volsphere(rayon)
print(v)


liste=[1,2,3,4,5,6]
for x in enumerate(liste):
	print(x)	#affiche les valeurs deux à deux	

"""		
#EXO3

def mafonction(x):
	return 2*x**3+x-5
def tabuler(fonction,borninf,bornsup,nbpas):

