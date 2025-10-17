# 🧩 Exo 1 : Dictionnaire à partir de 2 listes

keys = ['Ten','Twenty','Thirty']

values = [10,20,30]

print(dict(zip(keys,values)))

# ➡️ Résultat : {'Ten':10,'Twenty':20,'Thirty':30}





# 🎬 Exo 2 : Cinéma

fam = {"rick":43,'beth':13,'morty':5,'summer':8}

total=0

for n,a in fam.items():

  if a<3:p=0

  elif a<=12:p=10

  else:p=15

  print(n,p)

  total+=p

print("Total:",total)





# 👜 Exo 3 : Zara

brand={"name":"Zara","creation_date":1975,"creator":"Amancio",

"type":["men","women","children","home"],

"competitors":["Gap","H&M","Benetton"],

"stores":7000,

"color":{"FR":"blue","SP":"red","US":["pink","green"]}}



brand["stores"]=2

brand["country_creation"]="Spain"

brand["competitors"].append("Desigual")

del brand["creation_date"]



print(brand["competitors"][-1],brand["color"]["US"])





# 🌍 Exo 4 : Ville & Pays

def describe_city(city,country="Unknown"):

  print(f"{city} is in {country}")



describe_city("Paris")

describe_city("Reykjavik","Iceland")





# 🎲 Exo 5 : Random Compare

import random

def compare(num):

  r=random.randint(1,100)

  print("Success!" if num==r else f"Fail {num}/{r}")



compare(50)





# 👕 Exo 6 : T-shirt perso

def make_shirt(size="large",txt="I love Python"):

  print(f"Size:{size}, Msg:{txt}")



make_shirt()

make_shirt("medium")

make_shirt("small","Meta Morfoz 💡")





# 🌡️ Exo 7 : Température & conseil

import random

def get_temp():return random.uniform(-10,40)

def main():

  t=get_temp()

  print(f"T°:{t:.1f}°C")

  if t<0:print("🥶 Gèle!")

  elif t<16:print("🧥 Froid")

  elif t<23:print("😊 Doux")

  elif t<32:print("🌤 Chaud")

  else:print("🔥 Trop chaud!")

main()





# 🍕 Exo 8 : Pizza

tops=[];base=10;add=2.5

while True:

  t=input("Topping: ")

  if t=="quit":break

  tops.append(t)

  print(f"Add {t}")

print("Toppings:",tops)

print("Total:",base+add*len(tops))



mon_dico = {"Ten":10, "Twenty":20, "Thirty":30} 
print ("mon_dico")

def upper_string(s):
    return s.upper

fruit = ["Apple","Banana", "Pear", "Abricot", Orange]


def start_with_A(s): 
    return s[0] =="A"

fruit = []