# 🌟 Défi 1 : Multiples d’un nombre
number = int(input("Entrez un nombre : "))
length = int(input("Entrez la longueur souhaitée : "))

multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

print(f"Résultat : {multiples}")

# 🌟 Défi 2 : Supprimer les lettres doublées consécutives
texte = input("Entrez une phrase ou un mot : ")

nouveau_texte = ""
for i in range(len(texte)):
    if i == 0 or texte[i] != texte[i - 1]:
        nouveau_texte += texte[i]

print(f"Texte nettoyé : {nouveau_texte}")
