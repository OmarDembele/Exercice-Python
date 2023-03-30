"""
#EXO1
tps=6.892
dist=79.7
vitesse=dist//tps
#print("la vitesse est:",vitesse)
#FORMAT ARRONDI
print("la vitesse est: {}".format(vitesse))

#EXO2
nom=input("saisain un nom\t")
age=int(input("saisir l'age\t"))
print("votre nom est {} et vous avez {} ans".format(nom,age))

"""
#EXO3
"""
semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
print("les 5 premiers jous",semaine[0:5])
print("les week-enk",semaine[5:7])
#semaine.reverse()
#print(semaine)
for x in list(range(1,11)):
	y=9*x
	print(y)

for x in range(5):
	print(semaine[x])	

"""

#EXO4
"""
som=0	
etudiant=[14,9,6,8,12]
for x in range(len(etudiant)):
	som=som+etudiant[x]

print("la somme est",som)	

moy=som/len(etudiant)
print(f"{moy} est la moyenne")



#EXO5
a=["*","**","***","****","*****","******","*******","********","*********","**********",]
for x in range(len(a)):
	print(a[x])

a.reverse()0
print("l'inverse\n")
for x in range(len(a)):
	print(a[x])

"""

#import django
#print django.get_version()

# CELA PEMET DE SAISIR DES NBRES D4UNE LISTES ET LES AFFICHER

print('remplir la liste\n')
a=[]
for i in range(10):
    a.append(input('Saisir un nbre\t'))	
print(a)        