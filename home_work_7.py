class Human:
    def eat_spaghetti(self):
        print("Я могу есть спагетти")


class Robot:
    def drink_oi(self):
        print("Я могу  потреблять машинное масло")

class Cyborg(Human, Robot):
    pass
    

cyborg = Cyborg()
cyborg.drink_oi()
cyborg.eat_spaghetti()