class Warrior(): # дали название классу
    def __init__(self, name, power, endurance, hair_color): #перечислили атрибуты, характиристики
        self.name = name   #self. — создание конкретной характеристики
        self.power = power
        self.endurance = endurance
        self.hair_cjlor = hair_cjlor
    def eat(self):                   # создаём функции класса( что воин может делать)
        print(f"{self.name} сел кушать")
        self.power = + 1
    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance = + 2
    def hit(self):
        print(f"{self.name} бьет кого - то")
        self.endurance = - 6
    def walk(self):
        print(f"{self.name} гуляет")

    def walk(self):              # пишим характеристики конкретного воина, объекта
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_cjlor}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")

war1 = Warrior(name="Степа", power = 76 , endurance = 54, hair_cjlor = "коричневый")

print(war1.name)
print(war1.power)
print(war1.endurance)
print(war1.hair_cjlor)
