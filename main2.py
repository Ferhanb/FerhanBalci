# Opdracht 14

# In deze code zie je dat ik if, elif en else statements kan gebruiken.

# getal = 2

# if getal > 0:
#   print("Dit getal is positief.")
# elif getal < 0;
#   print("Dit getal is kleiner dan 0.")
# elif getal == 0:
#   print("Dit getal is gelijk aan 0.")
# else:
#   print("Dit is misschien geen getal?")

# Opdracht 15

# # Vraag gebruiker waar hij/zij vandaan komt
# land = input("Where do you come from? ").strip().capitalize()
# # Maak een lijst met landen waar ze vandaan kunnen komen

# # Begroet de gebruiker
# if "Nederland" in land:
#   print("Hoi!")
# elif "Frankrijk" in land:
#   print("Bonjour!")
# elif "Duitsland" in land:
#   print("Hallo!")
# elif "Spanje" in land:
#   print("Ola!")
# else:
#   print("Probeer opnieuw")

# # In dit voorbeeld zie je dat het antwoord hoofdlettergevoelig is. En als de gebruiker hetzelfde land in een andere taal invoert, herkent het programma dit woord niet. Gebruik .capitalize(), zodat het programma de eerste letter Hoofdletter maakt en alle andere letters kleine letters worden.

# # Opdracht 16
# # Vraag de gebruiker welke operation hij wil uitvoeren
# vraag = input("Wat wil je doen? ")
# # Vraag twee getallen

# x = int(input("Kies eerste getal: "))
# y = int(input("Kies tweede getal: "))

# # Doe de berekening
# if "Optellen" in vraag or "+" in vraag or "plus" in vraag:
#   z = x + y
# elif "Aftrekken" in vraag or "min" in vraag or "-" in vraag:
#   z = x - y
# elif "Vermenigvuldigen" in vraag or "keer" in vraag or "*" in vraag:
#   z = x * y
# elif "Delen" in vraag or ":" in vraag or "/" in vraag:
#   z = x / y
# else:
#   print("Verkeerd")

# # Print het antwoord in een zin.
# print(f"Het antwoord van de berekening is: {z}")

## Dictionary versie voor opdracht 16

antwoord = input("Wat wil  je doen? ")
berekening = {"plus": ["Optellen", "+"], "min": ["-", "min", "aftrekken"]}
