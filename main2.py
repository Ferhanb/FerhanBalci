# # Opdracht 14

# # In deze code zie je dat ik if, elif en else statements kan gebruiken.

# getal = 2

# if getal > 0:
#   print("Dit getal is positief.")

# elif getal == 0:
#   print("Dit getal is gelijk aan 0.")

# else:
#   print("Dit getal is kleiner dan 0.")

# # Opdracht 15

# # Vraag gebruiker waar hij/zij vandaan komt
# land = input("Where do you come from? ") .strip().capitalize()
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

# # In dit voorbeeld zie je dat het antwoord hoofdlettergevoelig is. En als de gebruiker hetzelfde land in een andere taal invoert, herkent het programma dit woord niet.


# Opdracht 16
# Vraag de gebruiker welke operation hij wil uitvoeren
vraag = input("Wat wil je doen? ")
# Vraag twee getallen

x = int(input("Kies eerste getal: "))
y = int(input("Kies tweede getal: "))

# Doe de berekening
if "Optellen" or "+" or "plus" in vraag:
  z = x + y
elif "Aftrekken" or "min" or "-" in vraag:
  z = x - y
elif "Vermenigvuldigen" or "keer" or "*" in vraag:
  z = x * y
elif "Delen" or ":" or "/" in vraag:
  z = x / y

# Print het antwoord in een zin.
print(f"Het antwoord van de berekening is: {z}")


