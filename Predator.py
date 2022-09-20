class Mixin_eat_berries:
    def eat_berries(self):
        print("Я любилю есть ягоды и мед")

class Predator:
    def eat_flesh(self):
        print("Я люблю есть мясо!")


class Wolf(Predator):
    pass

class Bear(Predator, Mixin_eat_berries):
    pass

wolf = Wolf()
wolf.eat_flesh()
bear = Bear()
bear.eat_flesh()
bear.eat_berries()