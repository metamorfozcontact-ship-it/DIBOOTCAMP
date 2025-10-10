#  Exercice 1
print("Hello world\n" * 4)

#  Exercice 2
resultat = (99 ** 3) * 8
print(resultat)

#  Exercice 3
mon_nom = "Fanta"
nom_utilisateur = input("Comment tu t'appelles ? ")
if nom_utilisateur.lower() == mon_nom.lower():
    print("Wow ! On a le même prénom 😄")
else:
    print(f"Enchanté {nom_utilisateur}, joli prénom ! 🌸")

#  Exercice 4
taille = int(input("Quelle est ta taille en cm ? "))
if taille > 145:
    print("🎢 Tu es assez grand(e) pour faire les montagnes russes !")
else:
    print("😅 Tu dois encore grandir un peu avant de monter.")

#  Exercice 5
my_fav_numbers = {3, 7, 9}
my_fav_numbers.add(11)
my_fav_numbers.add(13)
my_fav_numbers.remove(13)
friend_fav_numbers = {4, 7, 10}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#  Exercice 6
mon_tuple = (2, 4, 6)
try:
    mon_tuple.append(8)
except AttributeError:
    

#  Exercice 7
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
count_apples = basket.count("Apples")
basket.clear()
print(count_apples)
print(basket)

#  Exercice 8
sandwich_orders = [
    "Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
    "Pastrami sandwich", "Egg sandwich", "Chicken sandwich",
    "Pastrami sandwich"
]  print(f"✅ Préparation de : {sandwich}")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"✅ Préparation de : {sandwich}")
    finished_sandwiches.append(sandwich)
print("\n🥪 Sandwichs préparés :")
for s in finished_sandwiches:
    print("-", s)