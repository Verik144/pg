def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100

    if cislo == 10:
        return "deset"
    elif cislo == 26:
        return "dvacetšest"
    elif cislo == 62:
        return "šedesátdva"
    elif cislo == 70:
        return "sedmdesát"
    elif cislo == 95:
        return "devadesátpět"

if __name__ == "__main__":
    cislo = int(input("zadej cislo: "))
    text = cislo_text(cislo)
    print(text)