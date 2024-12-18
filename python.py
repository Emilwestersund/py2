"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("medier.csv", index_col=0, skiprows=[0,1], sep = ";", na_values=[".", ".."], encoding = "latin-1")

print(data)
print(data.head)
data.plot()
plt.show()
"""
#1
"""
userinput = int(input("Enter a number: "))

while userinput >= 0:
    print(userinput)
    userinput = userinput - 1
"""
#2
"""
userinput = int(input("Enter a number: "))

for i in range(11):
    print(i * userinput)
"""

#3
"""
import random

hemmelig_tall = random.randint(1, 100)
gjetning = None

print("gjett et tall mellom 1 og 100")

while gjetning != hemmelig_tall:
    gjetning = int(input("gjett: "))
    if gjetning > hemmelig_tall:
        print("tall er for høy")
    elif gjetning < hemmelig_tall:
        print("tall er for lav")
    else:
        print("du gjettet riktig")
"""

#4
"""
def er_primtall(tall):
    if tall < 2:
        return False #altså ikke primtall
    for i in range(2, tall):
        if tall % i == 0:
            return False
    return True

print("primtall mellom 1 og 100")

for i in range(1, 101):
    if er_primtall(i):
        print(i)
"""
#5
"""
import math

def areal_av_cirkel(radius):
    return math.pi * radius ** 2

while True:
    radius = int(input("skriv inn radius: "))
    print("areal: ", areal_av_cirkel(radius))
"""
#6
"""
ord_teller = 0

while True:
    
    tekst = input("Skriv inn en setning (eller skriv 'stopp' for å avslutte): ")
    
    
    if tekst.lower() == 'stopp':
        break
    
    ord_liste = tekst.split()
    ord_teller += len(ord_liste)  

    print(f"Antall ord til nå: {ord_teller}")

print(f"Total antall ord: {ord_teller}")
"""

#7 
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("lb.csv", index_col=0, skiprows=[0,1], sep = ";", na_values=[".", ".."], encoding = "latin-1")

print(data)
print(data.head)
data.plot()
plt.show()