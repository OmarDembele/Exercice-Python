
from time import time
start= float(time())

# Python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a+(i[0]).upper()
print(a)
end= time()
execution_time = end - start
print("Execution time: ", float(execution_time))