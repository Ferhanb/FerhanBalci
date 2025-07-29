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

# Opdracht 16
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

# # # Print het antwoord in een zin.
# print(f"Het antwoord van de berekening is: {z}")

# Opdracht 17 Een while loop met een teller totdat het een getal bereikt

# x = 1
# while x <= 64:
#   print(x)
#   x = x * 2

# x * = 2 Korte code

# # Lijst met range functie laten tellen
# lijst = list(range(10, 100, 10)) #Begin, eind, stappen
# print(lijst)

# #For loop
# for cijfer in range(1,11):
#   print(cijfer)


# # For loop met een nieuwe lijst, waaraan telkens gekwadrateerd getal wordt toegevoegd met append.
# lijst = []
# for loop in range(0, 10):
#   lijst.append(loop**2)
# print(lijst)
  

# for loop
# Append methode
# Kwadraat van getallen

for getal in range(0,50):
  # print(getal)
  if getal%3 and getal%5:
    print("Fizzbuzz")
  elif getal%5:
    print("Buzz")
  elif getal%3:
    print("Fizz")
  else:
    print(getal)
