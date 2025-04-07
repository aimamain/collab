class AimaMai():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f' Менин баламдын аты {self.name} , жашы болсо {self.age}'
class Malika(AimaMai):
    def __init__(self, name, age):
        super().__init__(name, age)
malika = Malika("Malika",14)

class Abdulmumid(AimaMai):
    def __init__(self, name, age):
        super().__init__(name, age)

abdulmumid = Abdulmumid("Abdulmumid", 16)



class Rashid(AimaMai):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
abdurashid = Rashid("Rashid", 19)

print(malika.info())
print(abdurashid.info())
print(abdulmumid.info())

print("Hello I'm Aiyma and Rashid")

print(h)

