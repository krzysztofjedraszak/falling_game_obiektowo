import pgzrun
from pgzero.actor import Actor


class Poziom_zycia(Actor):
    def __init__(self):
        self.zycia = []
        self.ilosc_zyc = 3
        self.blokada = False

        for i in range(self.ilosc_zyc):
            self.zycia.append(Actor("heart",(30+i*53,28)))

    def zdejmij_blokade(self):
        self.blokada = False

    def zaloz_blokade(self):
        self.blokada = True

    def zmniejsz(self):
        if self.ilosc_zyc > 0 and self.blokada == False:
            self.ilosc_zyc -= 1
            self.zaloz_blokade()
            self.zycia.pop()
            self.zdejmij_blokade()

    def draw(self):
        for i in self.zycia:
            i.draw()


class Gracz(Actor):
    def __init__(self, x, y):
        # super
        self.klatka = 0
        self.szybkosc = 0
        self.punkty = 0

    def draw(self):
        pass

    def update(self):
        pass


class Napisy():
    def __init__(self):
        self.start = ""
        self.koniec = ""

    def draw(self):
        pass


class Tlo_Podloze(Actor):
    def __init__(self, x_podloze, y_podloze):
        # super
        grafika_podloze = ""
        grafika_tlo = ""

    def draw(self):
        pass


class Plansza():
    def __init__(self):
        self.zycia = Poziom_zycia()
        self.gracz = Gracz(0, 0)
        self.przeszkody = Przeszkody()
        self.tlo_podloze = Tlo_Podloze(0, 0)
        self.napisy = Napisy()

    def draw(self):
        self.zycia.draw()

    def update(self):
        pass


class Fireball(Actor):
    def __init__(self):
        self.y_min = 0
        self.y_max = 0
        self.fireballs = []
        self.pred_spadania = 0

    def draw(self):
        pass


class Anvil(Actor):
    def __init__(self):
        self.y_min = 0
        self.y_max = 0
        self.anvils = []
        self.pred_spadania = 0

    def draw(self):
        pass


class Star(Actor):
    def __init__(self):
        self.y_min = 0
        self.y_max = 0
        self.stars = []
        self.pred_spadania = 0

    def draw(self):
        pass


class Przeszkody():
    def __init__(self):
        self.fireball = Fireball()
        self.anvil = Anvil()
        self.star = Star()

    def draw(self):
        pass

    def update(self):
        pass


gra = Plansza()


def draw():
    screen.clear()

    gra.draw()
    pass


def update():
    pass


pgzrun.go()
