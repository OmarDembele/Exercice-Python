""""
inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
outputlist=[]
index=0
for i in range(len(inputLists[0])):
    outputlist.append([])
    print(outputlist)
    for j in range(len(inputLists)):
        outputlist[index].append(inputLists[j][index])
    index+=1
print(outputlist)  
"""
print("ajout d'un liste")
x=[]
for i in range(3):
   x.append([])
#print(x)
for i in range(6):
    x.append()    
print(x)    
             
       