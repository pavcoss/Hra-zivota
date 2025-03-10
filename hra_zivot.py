# Funkce pro odstranění háčků a čárek
def odstran_hacky_carky(text):
    diakritika = {
        'á': 'a', 'ä': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'å': 'a',
        'č': 'c', 'ć': 'c',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'ö': 'o', 'ő': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u', 'ű': 'u',
        'ý': 'y', 'ÿ': 'y',
        'ž': 'z', 'ź': 'z', 'ż': 'z',
        'ň': 'n', 'ń': 'n',
        'š': 's', 'ś': 's',
        'ď': 'd', 'đ': 'd',
        'ľ': 'l', 'ĺ': 'l',
        'ř': 'r', 'ť': 't'
    }
    for key, value in diakritika.items():
        text = text.replace(key, value)
    return text

# Inicializace oblíbenosti
oblibenost = {
    "kluci": 0,
    "holky": 0,
    "rodice": 10,
    "dospeli": 0
}

# Zahájení hry
start = odstran_hacky_carky(input("Chceš si zahrát? ano či ne?: ").lower())
if start in ["ano", "a"]:
    
    pohlavi = odstran_hacky_carky(input("Jaký jsi pohlaví? Muž či žena?: ").lower())
    
    if pohlavi not in ["muz", "zena"]:
        print("Jsou jen dvě pohlaví.")
    else:
        print("Nacházíme se v roce 2009 a právě ses narodil")       
        cele_jmeno = input("Zadej své jméno: ") + " " + input("Zadej své příjmení: ")
        print("Přeskočím 3 roky a jsi momentálně ve školce.")
        
        # Výběr hraček
        hracky = {"auticka": "Autíčka", "panenky": "Panenky", "lego": "Lego"}
        print("Máš na výběr ze 3 hraček:", list(hracky.values()))
        
        while True:
            vyber_hracky = odstran_hacky_carky(input("Jakou hračku si vybereš?: ").lower())
            if vyber_hracky in hracky:
                print(f"Vybral jsi si {hracky[vyber_hracky]}.")
                break
            else:
                print("Neplatná volba, zkus to znovu.")

        # Nastavení oblíbenosti
        if vyber_hracky == "auticka":
            oblibenost["kluci"] += 6 if pohlavi == "zena" else 3
            oblibenost["holky"] -= 4 if pohlavi == "zena" else 0
            print("Máš náklonost k autům a kamarádíš se s kluky.")


        elif vyber_hracky == "panenky":
            oblibenost["holky"] += 3 if pohlavi == "zena" else 6
            oblibenost["kluci"] -= 5 if pohlavi == "muz" else 0
            print("Máš náklonost k holkám a jsi slay queen/material gworl.")


        elif vyber_hracky == "lego":
            oblibenost["holky"] += 2
            oblibenost["kluci"] += 2
            print("Budeš velmi kreativní a inteligentní.")











else:
    print("Nevadzi")
