class Werknemer:
    def __init__(self, registratienummer):
        self.registratienummer = registratienummer

class Freelancer(Werknemer):
    def __init__(self, registratienummer, uurloon):
        super().__init__(registratienummer)
        self.uurloon = uurloon
        self.uren_gewerkt = 0

    def werkuren(self, uren):
        self.uren_gewerkt = uren

    def printverdiend(self):
        verdiend = self.uurloon * self.uren_gewerkt
        print(f"Werknemer: {self.registratienummer} verdient: {verdiend:.2f} Euro.")


class VasteKracht(Werknemer):
    def __init__(self, registratienummer, maandloon):
        super().__init__(registratienummer)
        self.maandloon = maandloon

    def printverdiend(self):
        print(f"Werknemer: {self.registratienummer} verdient: {self.maandloon:.2f} Euro.")


class Stukwerker(Werknemer):
    def __init__(self, registratienummer, stukprijs):
        super().__init__(registratienummer)
        self.stukprijs = stukprijs
        self.aantal_stukken = 0

    def produceerstuks(self, stuks):
        self.aantal_stukken = stuks

    def printverdiend(self):
        verdiend = self.stukprijs * self.aantal_stukken
        print(f"Werknemer: {self.registratienummer} verdient: {verdiend:.2f} Euro.")


# Testprogramma voor Opdracht 1a en 1b
f = Freelancer(1, 25.75)         # werknemer 1 verdient 25.75 per uur
v = VasteKracht(2, 1873.53)      # werknemer 2 verdient 1873.53 per maand
s = Stukwerker(3, 1.05)          # werknemer 3 verdient 1.05 per stuk

f.werkuren(84)                   # werknemer 1 werkt (deze maand) 84 uren
s.produceerstuks(1687)           # werknemer 3 produceert (deze maand) 1687 stuks

print('Maand 1:')
f.printverdiend()
v.printverdiend()
s.printverdiend()

f.werkuren(13.5)                 # werknemer 1 werkt (deze maand) 13.5 uren
s.produceerstuks(0)              # werknemer 3 produceert (deze maand) 0 stuks

print('Maand 2:')
f.printverdiend()
v.printverdiend()
s.printverdiend()
