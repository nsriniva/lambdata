from random import randint


class Product():

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        val = self.price/self.weight

        if val < 0.5:
            ret = "Not so stealable..."
        elif 0.5 <= val < 1.0:
            ret = "Kinda stealable."
        else:
            ret = "Very stealable!"

        return ret

    def explode(self):
        val = self.flammability * self.weight

        if val < 10:
            ret = "...fizzle."
        elif 10 <= val < 50:
            ret = "...boom!"
        else:
            ret = "...BABOOM!!"

        return ret


class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        val = self.weight

        if val < 5:
            ret = "That tickles."
        elif 5 <= val < 15:
            ret = "Hey that hurt!"
        else:
            ret = "OUCH!"

        return ret
