"""

def calculator(y, m, d):
    import datetime
    today=datetime.datetime.now().date()
    #year_born=int(input("Enter your age: "))
    year_born=datetime.date(y, m, d)
    age=today.year - year_born.year
    #age=int((today-year_born).days /365.25)
    print(today)
    print(age)
calculator(1998, 1, 31)    
"""
from datetime import date  
now=date.today()
born=int(input("Enter your birth date")) 
def calculator(x):
    x=now.year-born
    print(x)
calculator(now) 
   
    