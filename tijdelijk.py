# Dictionary met ijsprijzen
prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}

# Bereken de aanbiedingsprijs
aanbieding = prijzen["aardbei"] * 0.8

# Maak de reclametekst met een f-string
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"

# Maak een nieuwe tekst zonder decimalen
reclame_tekst2 = reclame_tekst[:reclame_tekst.index("0")]

# Zet de reclametekst om naar hoofdletters
reclame_tekst3 = reclame_tekst2.upper()

# Maak een list van alle woorden
reclame_tekst4 = reclame_tekst3.split()

# Print de woorden onder elkaar
for el in reclame_tekst4:
    # Controleer de lengte van het woord
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())