"""
#EXO1

from math import *
nbre=float(input("saisir un nombre\t"))
if nbre>=0 :
	y=sqrt(nbre)	
	print("la racine carre est:{}".format(y))
else:	
	print("vous avez saisi un nombre negatif")


#EXO2

mot1=input("saisir un premier mot\t")
mot2=input("saisir un deuxieme mot\t")
if mot1<mot2:
	print("plus petit est:",mot1)
else:
	print("plus petit:",mot2)	


#Exo3
pseuil=2.3
vseuil=7.41
pres=float(input("saisir la pression\t"))
vol=float(input("saisir le volume\t"))
if pres>pseuil and vol>vseuil:
	print("la pressionet le volume sont eleve, Stoppez")
elif pres>pseuil:
	print("augmenter le volume de l'enceinte")
elif vol>vseuil:
	print("diminuer le volume de l'enceinte")
else:
	print("tout va bien")



#EXO4
a=0
b=10
while a<b:
	print("a=",a)
	a=a+1


print("autre methode")


while b:
	b=b-1
	if b%2!=0:
		print("b=",b)


#EXO5
nb=int(input("saisir un nombre compris entre 1 et 10\t"))
if 0<=nb<=10:
	print("valeur du nombre saisit:",nb)
else:	
	print("le nombre n'appartient pas à l'intervalle")


	

#EXO6

nom=input("saisir un nom\t")
for lettre in nom :
	print("",lettre)
nom1=["bemba","omzo"]
for x in nom1 :
	print(x)


#EXO7
for i in range(0,10,3):
	print(i)


#EXO8
for i in range(1,10):
	if i==5:
		#break #cela veut dire que l'instruction qui suit et la boucle vont s'arreter 
		continue #cela veut dire que l'instruction qui suit ne se deroulera pas mais la boucle va continuer
	print(i)	

"""

#EXO9
# import
from math import sin
# programme principal -----------------------------------------------
for x in range(-3, 4): # -3 -2 -1 0 1 2 3
	try:
		print("{}".format(sin(x)/x), end=" ")
	except:
		print("{}".format(float(1)), end=" ")

print()		