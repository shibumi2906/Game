class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2

    def hit(self):
        print(f"{self.name} бьет кого - то")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет")
    def describe(self):
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")


war1 = Warrior(name="Степа", power=76, endurance=54, hair_color="коричневый")

war2 = Warrior(name="Егор", power=45, endurance=49, hair_color="блондин")


war1.describe()

war1.sleep()
war1.eat()
war1.hit()
war1.walk()

war1.describe()
