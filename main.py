import pgzrun
from pgzero.actor import Actor


class Poziom_zycia(Actor):
    def __init__(self,x,y):
        # super
        self.zycia=[]
        self.ilosc_zyc=0
        self.blokada=False

    def zdejmij_blokade(self):
        pass

    def zaloz_blokade(self):
        pass

    def zmniejsz(self):
        pass

    def draw(self):
        pass


class Gracz(Actor):
    def __init__(self,x,y):
        # super
        self.klatka=0
        self.szybkosc=0
        self.punkty=0

    def draw(self):
        pass

    def update(self):
        pass


class Napisy():
    def __init__(self):
        self.start=""
        self.koniec=""

    def draw(self):
        pass


class Tlo_Podloze(Actor):
    def __init__(self,x_podloze,y_podloze):
        # super
        grafika_podloze=""
        grafika_tlo=""

    def draw(self):
        pass


class Plansza():
    def __init__(self):
        self.zycia=Poziom_zycia(0,0)
        self.gracz=Gracz(0,0)
        self.przeszkody=Przeszkody()
        self.tlo_podloze=Tlo_Podloze(0,0)
        self.napisy=Napisy()

    def draw(self):
        pass

    def update(self):
        pass


class Fireball(Actor):
    def __init__(self):
        self.y_min=0
        self.y_max=0
        self.fireballs=[]
        self.pred_spadania=0

    def draw(self):
        pass


class Anvil(Actor):
    def __init__(self):
        self.y_min=0
        self.y_max=0
        self.anvils=[]
        self.pred_spadania=0

    def draw(self):
        pass


class Star(Actor):
    def __init__(self):
        self.y_min=0
        self.y_max=0
        self.stars=[]
        self.pred_spadania=0

    def draw(self):
        pass


class Przeszkody():
    def __init__(self):
        self.fireball=Fireball()
        self.anvil=Anvil()
        self.star=Star()

    def draw(self):
        pass

    def update(self):
        pass


def draw():
    pass

def update():
    pass



pgzrun.go()