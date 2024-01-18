import random


class Cat:
    print("Meow hi")

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_eat(self):
        print("Meow time to eat!")
        self.progress -= 0.12
        self.gladness += 3

    def to_sleep(self):
        print("Meow i'll sleep!")
        self.gladness += 3

    def to_chill(self):
        print("Meow time to rest")
        self.gladness += 5
        self.progress -= 0.1

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def is_alive(self):
        if self.progress < -0.5:
            print("Meow... (cat dead)")
            self.alive = False
        elif self.gladness <= 0:
            print("Meow depression")
            self.alive = False
        elif self.progress > 5:
            print("Meow passed externally...")
            self.alive = False

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life."
        print(f"{day:=^50}")
        choose = random.randint(1, 3)
        if choose == 1:
            self.to_eat()
        elif choose == 2:
            self.to_sleep()
        elif choose == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


nick = Cat("Sharik")

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)