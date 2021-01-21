import pgzrun
from pgzero.actor import Actor


class Poziom_zycia(Actor):
    def __init__(self):
        self.first=30
        self.second=30
        self.zycia = []
        self.ilosc_zyc = 3
        self.blokada = False

        for i in range(self.ilosc_zyc):
            self.zycia.append(Actor("heart",(self.first+i*53,self.second)))

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
    def __init__(self):
        self.first=400
        self.second=484
        super(Gracz, self).__init__("p1_stand",(self.first,self.second))
        self.klatka = 0
        self.szybkosc = 6
        self.punkty = 0

    # def draw(self):
    #     pass

    def update(self):
        for i in range(1, 10):
            if self.klatka == 0:
                self.image = "p1_walk01"
            elif self.klatka == i:
                self.image = f"p1_walk0{i}"
            elif self.klatka == 9:
                self.image = "p1_walk10"
            elif self.klatka == 10:
                self.image = "p1_walk11"

        self.klatka += 1
        if self.klatka == 11:
            self.klatka = 0


class Napisy():
    def __init__(self):
        self.start = "Wcisnij ENTER aby rozpoczac gre"
        self.koniec = "Przegrales :( Koniec Gry\nWcisnij ENTER aby zagrac jeszcze raz"

    def draw(self,arg):
        screen.draw.text(arg, center=(screen.width / 2, screen.height / 2),
                         color="orange", fontsize=60)


class Tlo_Podloze(Actor):
    def __init__(self):
        self.x_podloze=0
        self.y_podloze=0
        self.grafika_podloze = "castle"
        self.grafika_tlo = "#ebe591"

    def draw(self):
        screen.fill(self.grafika_tlo)

        for i in range((screen.width // 70) + 1):
            screen.blit(self.grafika_podloze, (i * 70, screen.height - 70))


class Plansza():
    def __init__(self):
        self.poziom_zycia = Poziom_zycia()
        self.gracz = Gracz()
        self.przeszkody = Przeszkody()
        self.tlo_podloze = Tlo_Podloze()
        self.napisy = Napisy()
        self.punkty=0
        self.stan_gry=0

    def detektor_kolizji():
        pass

    def draw(self):
        self.tlo_podloze.draw()
        self.poziom_zycia.draw()
        self.gracz.draw()

        if self.stan_gry==0:
            self.napisy.draw(self.napisy.start)

        if self.poziom_zycia.ilosc_zyc==0:
            self.stan_gry="q"
            self.napisy.draw(self.napisy.koniec)

    def update(self):
        if keyboard.RETURN:
            if self.stan_gry==0:
                self.stan_gry=1


        if self.stan_gry==1:
            if keyboard.right or keyboard.left:
                if keyboard.RIGHT:
                    self.gracz.left += self.gracz.szybkosc

                if keyboard.LEFT:
                    self.gracz.left -= self.gracz.szybkosc

                if keyboard.SPACE and keyboard.LEFT:
                    self.gracz.left -= 2 * self.gracz.szybkosc

                if keyboard.SPACE and keyboard.RIGHT:
                    self.gracz.left += 2 * self.gracz.szybkosc

                self.gracz.update()

            if self.gracz.right < 0:
                self.gracz.left = screen.width

            if self.gracz.left > screen.width:
                self.gracz.right = 0

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

def update():
    gra.update()


pgzrun.go()
