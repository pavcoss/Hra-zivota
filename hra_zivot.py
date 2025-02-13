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
        'ř': 'r', 'ť': 't',
        'ď': 'd', 'ť': 't', 'ľ': 'l',
        'ž': 'z'
    }

    for key, value in diakritika.items():
        text = text.replace(key, value)

    return text

start = input("Chceš si zahrát? ano či ne?: ")
oblibensot_kluci = 0
oblibenost_holky = 0
oblinost_rodice = 10
oblibentst_dospeli = 0


# Odstranění diakritiky (háčků a čárek)
start = odstran_hacky_carky(start)

# Odstranění diakritiky pro pohlaví
pohlavi = input("Jaký jsi pohlaví? Muž či žena?: ")
pohlavi = odstran_hacky_carky(pohlavi)

if pohlavi.lower() not in ["muz", "zena"]:
    print("Jsou jen dvě pohlaví.")
else:
    if start.lower() in ["ano", "a"]:
        print("Nacházíme se v roce 2009 a právě ses narodil")
        jmeno = input("Zadej své jméno: ")
        prijmeni = input("Zadej své příjmení: ")
        cele_jmeno = jmeno + " " + prijmeni

        print("Přeskočím 3 roky a jsi momentálně ve školce.")
        print("Máš na výběr ze 3 hraček")
        
        hracky = ["autíčka", "panenky", "lego"]
        print(hracky)
        
        vyber_hracky = input("Jakou hračku si vybereš?: ")
        vyber_hracky = odstran_hacky_carky(vyber_hracky)

      
      
        if vyber_hracky.lower() == "auticka":
            print("Vybral jsi si autíčka.")

            if pohlavi.lower() == "zena":
                print("Jelikož sis vybrala autíčka tak se budeš spíše bavit s klukama a budeš mít náklonost k autům ") 
                oblibensot_kluci += 6
                oblibenost_holky -= 4

                
            if pohlavi.lower() == "muz":
                print("našel sis kámoše a teď spolu děláte závody , budeš mít náklonost k autům ")   

                oblibensot_kluci += 3
                   

        if vyber_hracky.lower() == "panenky":
            print("Vybral jsi si panenky.")


            if pohlavi.lower() == "zena":
              print("Jelikož sis vybrala panenky tak se budeš spíše bavit s holkama a budeš slay queen")
            oblibenost_holky += 3
            
            

            if pohlavi.lower() == "muz":
                print("Vybral sis panenky, takže se budeš bavit s holkama a budeš material gworl")
                oblibenost_holky += 6
                oblibensot_kluci -= 5

        
        if vyber_hracky.lower() == "lego":
            print("Vybral jsi si lego.")
        
            if pohlavi.lower() == "zena":
                print("Jelikož sis vybrala lego tak budeš velmi kreativní a inteligentní")
                oblibenost_holky += 2
                oblibensot_kluci += 2
            
            if pohlavi.lower() == "muz":
                print("Vybral sis lego, takže budeš velmi kreativní a tvoje oblíbené lego bude ninjago")
                oblibenost_holky += 2
                oblibensot_kluci += 2

    else:
        print("Škoda, možná jindy.")
