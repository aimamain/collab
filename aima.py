class AimaMai():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f' Менин баламдын аты {self.name} , жашы болсо{self.age}'
class Malika(AimaMai):
    def __init__(self, name, age):
        super().__init__(name, age)
malika = Malika("Malika",14)

class Abdulmumid(AimaMai):
    def __init__(self, name, age):
        super().__init__(name, age)

abdulmumid = Abdulmumid("Abdulmumid", 16)

