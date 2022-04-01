import threading as th


class Pet:
    _name = ""
    type = ""
    __health = 0
    __hunger = 0
    __fun = 0
    time_hatch = 0

    __lost_fun = 0
    __gain_hunger = 0

    def __init__(self, name, typ, hunger, health, fun, lost_fun, gain_hunger, time):
        self._name = name
        self.type = typ
        self.hunger = hunger
        self.health = health
        self.fun = fun
        self.__lost_fun = lost_fun
        self.__gain_hunger = gain_hunger
        self.time_hatch = time

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        elif value > 100:
            self.__health = 100
        else:
            self.__health = value

    @property
    def hunger(self):
        return self.__hunger

    @hunger.setter
    def hunger(self, value):
        if value < 0:
            self.__hunger = 0
        elif value > 100:
            self.__hunger = 100
        else:
            self.__hunger = value

    @property
    def fun(self):
        return self.__fun

    @fun.setter
    def fun(self, value):
        if value < 0:
            self.__fun = 0
        elif value > 100:
            self.__fun = 100
        else:
            self.__fun = value

    @property
    def lost_fun(self):
        return self.__lost_fun

    @lost_fun.setter
    def lost_fun(self, value):
        self.__lost_fun = value

    @property
    def gain_hunger(self):
        return self.__gain_hunger

    @gain_hunger.setter
    def gain_hunger(self, value):
        self.__gain_hunger = value

    def vet(self):
        self.health += (self.health * 1 / 2)
        self.fun -= (self.fun * 1 / 3)

    def feed(self):
        self.hunger -= 5

    def play(self):
        self.fun += 5


class Horse(Pet):
    def __init__(self, name, typ, hunger, health, fun, lost_fun, gain_hunger, time):
        super().__init__(name, typ, hunger, health, fun, lost_fun, gain_hunger, time)
        self.type = "Horse"

    def mk_hungry(self):
        global mk_hungryth
        mk_hungryth = th.Timer(1, self.mk_hungry)
        mk_hungryth.start()
        self.hunger += 1
        self.health -= (self.health - 1 / 8 * self.hunger)
        self.gain_hunger += 1

    def mk_fun(self):
        global mk_funth
        mk_funth = th.Timer(1, self.mk_fun)
        mk_funth.start()
        self.fun -= 1
        self.health -= (1 / 8 * (100 - self.fun))
        self.lost_fun += 1


class Eagle(Pet):
    def __init__(self, name, typ, hunger, health, fun, lost_fun, gain_hunger, time):
        super().__init__(name, typ, hunger, health, fun, lost_fun, gain_hunger, time)
        self.type = "Eagle"

    def mk_hungry(self):
        global mk_hungryth
        mk_hungryth = th.Timer(1, self.mk_hungry)
        mk_hungryth.start()
        self.hunger += 3
        self.health -= (self.health - 1 / 6 * self.hunger)
        self.gain_hunger += 3

    def mk_fun(self):
        global mk_funth
        mk_funth = th.Timer(1, self.mk_fun)
        mk_funth.start()
        self.fun -= 3
        self.health -= (1 / 6 * (100 - self.fun))
        self.lost_fun += 3


class Panther(Pet):
    def __init__(self, name, typ, hunger, health, fun, lost_fun, gain_hunger, time):
        super().__init__(name, typ, hunger, health, fun, lost_fun, gain_hunger, time)
        self.type = "Panther"

    def mk_hungry(self):
        global mk_hungryth
        mk_hungryth = th.Timer(1, self.mk_hungry)
        mk_hungryth.start()
        self.hunger += 5
        self.health -= (self.health - 1 / 4 * self.hunger)
        self.gain_hunger += 5

    def mk_fun(self):
        global mk_funth
        mk_funth = th.Timer(1, self.mk_fun)
        mk_funth.start()
        self.fun -= 5
        self.health -= (1 / 4 * (100 - self.fun))
        self.lost_fun += 5
