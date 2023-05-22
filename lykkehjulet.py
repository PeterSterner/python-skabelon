
tal = 55

while True:
    gæt = int(input("Gæt et tal mellem 1 og 100: "))
    if gæt == tal:
        print("Tillykke, du har gættet rigtigt!")
        break
    elif gæt < tal:
        print("Dit gæt er for lavt!")
    else:
        print("Dit gæt er for højt!")
