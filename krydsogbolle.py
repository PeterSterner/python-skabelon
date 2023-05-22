def tegn_braet():
    # Tegn bræt
    print(" ", end="")
    for i in range(1, 4):
        print(i, end=" ")
    print()
    for i in range(1, 4):
        print(i, end=" ")
        for j in range(1, 4):
            print(braet[i][j], end=" ")
        print()


def spiller_tur(spiller):
    # Spiller tur
    print("Spiller", spiller)
    while True:
        x = int(input("Indtast x-koordinat: "))
        y = int(input("Indtast y-koordinat: "))
        if braet[y][x] == " ":
            braet[y][x] = spiller
            break
        else:
            print("Ugyldigt træk!")


def tjek_vinder(spiller):
    # Tjek om spiller har vundet
    for i in range(1, 4):
        if braet[i][1] == spiller and braet[i][2] == spiller and braet[i][3] == spiller:
            return True
        if braet[1][i] == spiller and braet[2][i] == spiller and braet[3][i] == spiller:
            return True
    if braet[1][1] == spiller and braet[2][2] == spiller and braet[3][3] == spiller:
        return True
    if braet[1][3] == spiller and braet[2][2] == spiller and braet[3][1] == spiller:
        return True
    return False


def spil():
    tegn_braet()
    while True:
        spiller_tur("X")
        tegn_braet()
        if tjek_vinder("X"):
            print("Spiller X har vundet!")
            break
        spiller_tur("O")
        tegn_braet()
        if tjek_vinder("O"):
            print("Spiller O har vundet!")
            break


# Hovedprogram
braet = [[" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " "]]

spil()
