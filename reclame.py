# Importeer functie mijn_functie_2
from algemene_functies import mijn_functie_2


# Functie 1: aanbieding maken
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)

    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."


# Functie 2: totale inkomsten inclusief btw-berekening
def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag = totaal * btw

    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag:.2f} euro btw betaald dient te worden."


# Functie 3: hoogste en laagste waarde
def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]


# Functie 4: gemiddelde inkomsten
def gemiddelde(mijn_lijst):
    gem = sum(mijn_lijst) / len(mijn_lijst)

    return f"De gemiddelde inkomsten deze week zijn {gem:.2f} euro."


# Functie 5: meervoudig
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)


# Functie 6: combinatie
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)

    return mijn_functie_2(korte_lijst[0], korte_lijst[1])