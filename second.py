def cislo_text(cislo):
    cislo = int(cislo)
    specialni = {
        0:"nula",
        10:"deset",
        11:"jedenact",
        12:"dvanact",
        13:"trinact",
        14:"ctyrnact",
        15:"patnact",
        16:"sestnact",
        17:"sedmnact",
        18:"osmnact",
        19:"devatenact",
        100:"sto"}
    if cislo in specialni:
        return specialni[cislo]
    else:
        desitka = (cislo//10)*10
        jednotka = cislo%10
        jednotky = {0:"",1:"jedna",2:"dva",3:"tri",4:"ctyri",5:"pet",6:"sest",7:"sedm",8:"osm",9:"devet"}
        desitky = {0:"",20:"dvacet",30:"tricet",40:"ctyricet",50:"padesat",60:"sedesat",70:"sedmdesat",80:"osmdesat",90:"devadesat"}
        return f"{desitky[desitka]} {jednotky[jednotka]}".strip()

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)