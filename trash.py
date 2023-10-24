class Spiller:
    def __init__(self, navn, højde, vægt, våben):
        self.navn = navn
        self.højde = højde
        self.vægt = vægt
        self.våben = våben
        self.score = 0
        self.liv = 100

    def brug_våben(self, fjende):
        fjende.liv -= 10


class Fjende:
    def __init__(self, navn, højde, vægt, våben):
        self.navn = navn
        self.højde = højde
        self.vægt = vægt
        self.våben = våben
        self.score = 0
        self.liv = 200

    def udskriv_liv(self):
        print(self.liv)


spiller = Spiller("Frodo", 1.80, 80, "Sværd")
fjende1 = Fjende("Sauron", 2.50, 200, "Kæmpe Sværd")
fjende2 = Fjende("Saruman", 2.10, 100, "Stav")
fjende3 = Fjende("Gollum", 1.20, 30, "Kløer")
fjende4 = Fjende("Emil", 1.80, 80, "Bog")

spiller.brug_våben(fjende1)
fjende1.udskriv_liv()
