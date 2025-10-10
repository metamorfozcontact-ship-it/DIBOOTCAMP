class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Bengal(Cat):
    def sing(self, sounds):
        return f"{self.name} sings {sounds}"


class Chartreux(Cat):
    def sing(self, sounds):
        return f"{self.name} sings {sounds}"


class Siamese(Cat):
    def sing(self, sounds):
        return f"{self.name} sings {sounds}"


# Étape 2 : Créer des instances
bengal_cat = Bengal("Tigrou", 3)
chartreux_cat = Chartreux("Grisou", 5)
siamese_cat = Siamese("Luna", 2)

# Étape 3 : Créer la liste de chats et promener
all_cats = [bengal_cat, chartreux_cat, siamese_cat]
sara_pets = Pets(all_cats)
print("\n=== EXERCICE 1 : ANIMAUX DE COMPAGNIE ===")
sara_pets.walk()

# ===============================================================
# 🌟 EXERCICE 2 — CHIENS 🐶
# Méthodes, attributs, comparaisons
# ===============================================================

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} barks woof!"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight!"
        elif my_power < other_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a draw!"


# Étape 2 : Créer 3 chiens
dog1 = Dog("Rex", 4, 20)
dog2 = Dog("Teacup", 2, 5)
dog3 = Dog("Max", 5, 15)

# Étape 3 : Tester
print("\n=== EXERCICE 2 : CHIENS ===")
print(dog1.bark())
print(f"{dog1.name}'s run speed: {dog1.run_speed()}")
print(dog1.fight(dog2))
print(dog2.fight(dog3))

# ===============================================================
# 🌟 EXERCICE 3 — CHIENS DOMESTIQUÉS 🏡🐕
# Héritage + random + *args
# ===============================================================

import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        all_dogs = ", ".join(args)
        print(f"{self.name} and {all_dogs} are playing together!")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} isn't trained yet!")


# Test complet
print("\n=== EXERCICE 3 : CHIENS DOMESTIQUÉS ===")
my_dog = PetDog("Fido", 3, 12)
my_dog.train()
my_dog.play("Buddy", "Max", "Rocky")
my_dog.do_a_trick()

# ===============================================================
# 🌟 EXERCICE 4 — FAMILLE 👨‍👩‍👧
# Classes, interactions et conditions
# ===============================================================

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)
        print(f"{first_name} {self.last_name} est né(e) dans la famille !")

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends.")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("Person not found in family.")

    def family_presentation(self):
        print(f"Famille : {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, {member.age} ans")


# Test complet
print("\n=== EXERCICE 4 : FAMILLE ===")
bamba_family = Family("Bamba")
bamba_family.born("Fanta", 35)
bamba_family.born("Adam", 18)
bamba_family.born("Sali", 12)

bamba_family.family_presentation()


bamba_family.check_majority("Adam")
bamba_family.check_majority("Sali")




{}

