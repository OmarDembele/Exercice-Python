# la saisit d'une liste

a=[]
print('Remplir la liste des nombres')
d=int(input('saisir un nbre compris entre 5 et 15: '))
for i in range(0, d):
    x=a.append(i)
print(a)
#Calcul de la moyenne
b=[12,16,20,20,12,30,25,23,24,20]
#b.sort()
print(b)
som=0
for x in range(len(b)):
    som=som+b[x]  
moy=som/len(b)
print("la moyenne est: ",moy)

# Calcul de la valeur mediane
print(len(b))
if len(b)%2==0:
    m1=b[len(b)//2]
    m2=b[len(b)//2-1]
    m=(m1+m2)/2 
else:
    m=b[len(b)//2]    
print('la mediane est:', m)  


# CALCUL DE LA MODE
ba=[12,16,20,20,12,30,25,23,24,20]
ab={}
for i in ba:
   #ab.setdefault(i, 0)
    ab[i]=ab.get(i, 0) + 1
    #ab[i]+=1
frequent=max(ab.values())
for i, j in ab.items():
    if j==frequent:
        mode=i
print("la mode est:",mode)            

    

