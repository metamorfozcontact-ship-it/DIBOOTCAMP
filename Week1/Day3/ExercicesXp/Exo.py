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

else:
    print(f"{davids_dog.name} est plus grand.")

    







