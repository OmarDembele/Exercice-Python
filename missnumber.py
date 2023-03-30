
""""

a=[0,12,2,3,3,4,6,7,9,10,12,13,14,15]
b=set(a)
#print(b)
c=[]
for i in range(0, len(b)):
    if i not in b:
        c.append(i)

print('les donnees manquant: ', c)    
"""
a=[]
for i in range(15):
    a.append(int(input('Enter a number: ')))
print("the list values",a)
update=set(a)
b=[]
def missing(n):
    for j in range(15):
        if j not in update:
            b.append(j)
            
    print('the missing number',b)  

missing(a)          
    