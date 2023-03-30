""""
import getpass
  
pwd = getpass.getpass(prompt = 'Enter the password')
if pwd == 'Admin':
    print('Unlock!')
else:
    print('You entered wrong password')

import getpass
  
pwd = getpass.getpass()
print("You entered: ", pwd)
"""

# AUTHENTIFICATION
import getpass
database={'omar123':'12356', 'bems01':'456789','djigabs':'1478963'}
b=list(database.keys())
print(b)
name=input("Entrer votre nom d'utilisateur: ")
while name not in b:
    name=input("Entrer votre nom d'utilisateur: ")
pwd=getpass.getpass("Entrer votre password: ")   
for i in database.keys():
    if name==i:
        while pwd!=database.get(i):
            pwd=getpass.getpass("Entrer encore votre mot de passe: ")
        break
for x, y in database.items():
    if name==x and pwd==y:
        print('verified')        
            