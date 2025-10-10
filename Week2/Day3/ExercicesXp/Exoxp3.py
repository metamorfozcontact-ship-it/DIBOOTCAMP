class Cat:
    def __init__(self, name, age):
        self.name = name # Attribut "nom"
        self.age = age # Attribut "âge"

    
    
def get_oldest_cat(cat1, cat2, cat3):
# on compare les âges 
    if cat1.age >= cat2.age and cat1.age >= cat3.age:
        return cat1.name

    elif cat2.age >= cat3.age: 
        return cat2.name

    else : 
        return cat3.name

chat1 = Cat("Mimi", 3)
chat2 = Cat("Nala", 7)
chat3 = Cat("Simba", 5)
print(get_oldest_cat(chat1,chat2,chat3))



class Dog:
    def __init__(self, name, height):        
        self.name = name
        self.height = height   

    def bark(self):
        print(f"{self.name} goes woof!") 

   
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high")   

        # Création des chiens


davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# Appels de méthodes


for dog in [davids_dog, sarahs_dog]:   
    print(f"{dog.name} mesure {dog.height} cm")
    dog.bark()
    dog.jump()

# Comparaison

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} est plus grand.")

else:_

class Song:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
            for line in self.lyrics : 
                print(line)

# Création d’une chanson
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"]) 

stairway = Song ([
    "There's a lady who's sure"
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
    ])

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animaux dans le zoo :", self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

# Appel de la méthode
stairway.sing_me_a_song()


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Création d’une chanson
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

# Appel de la méthode
stairway.sing_me_a_song()

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animaux dans le zoo :", self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped = {}

        for animal in sorted_animals:
            key = animal[0].upper()
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(animal)

        self.grouped_animals = grouped  # on garde ça pour get_groups()

    def get_groups(self):
        for letter, group in self.grouped_animals.items():
            print(f"{letter}: {group}")

# Création du zoo
brooklyn_safari = Zoo("Brooklyn Safari")

# Ajout d’animaux
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.add_animal("Lion")

# Affichage
brooklyn_safari.get_animals()

# Vente
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()

# Tri & affichage des groupes
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()




