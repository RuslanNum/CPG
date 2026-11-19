def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    radek, sloupec = cilova_pozice
    
    if 1>radek or 1>sloupec or 8<radek or 8<sloupec:
        return False
        
    if cilova_pozice in obsazene_pozice:
        return False
        
    aktualni_pozice = figurka["pozice"]
    aktualni_radek, aktualni_sloupec = aktualni_pozice
    typ = figurka["typ"]
    cil_radek = abs(radek - aktualni_radek)
    cil_sloupec = abs(sloupec - aktualni_sloupec)
    
    if cilova_pozice == aktualni_pozice: 
        return False
    
    if typ == "král":
        if cil_radek <= 1 and cil_sloupec <= 1:
            return True
        return False
        
    elif typ == "jezdec":
        if cil_radek == 1 and cil_sloupec == 2:
            return True
        if cil_radek == 2 and cil_sloupec == 1:
            return True
        return False
        
    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))  # True (o 1 pole dolů)
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))  # False (příliš daleko - o 2 pole)
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))  # False (mimo šachovnici)

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # True (tvar L: 2 nahoru, 1 doprava)
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))  # False (neni tvar L)
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice)) # False (mimo šachovnici)
