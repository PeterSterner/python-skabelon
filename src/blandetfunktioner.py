def find_min(liste):
    min = liste[0]
    for i in range(1, len(liste)):
        if liste[i] < min:
            min = liste[i]
    return min


def find_gennemsnit(liste):
    sum = 0
    for tal in liste:
        sum += tal
    return sum / len(liste)


def udskriv_liste(n):
    import random
    liste = []
    for i in range(n):
        liste.append(random.randint(1, 100))
    print(liste)
    return liste


def udskriv_min_gennemsnit(liste):
    print("Mindste tal:", find_min(liste))
    print("Gennemsnit:", find_gennemsnit(liste))


# Test af funktionerne
liste = udskriv_liste(10)
udskriv_min_gennemsnit(liste)
