# variabele_5 = 10

# #Opdracht 2 en 3 Boodschappenlijst

# kaas_kilogram = 3
# eieren = 2
# melk_liter = 1
# vlees_kilogram = 5

# kaas_prijs = 2
# ei_prijs = 0.3
# vlees_prijs = 3
# melk_prijs = 1

# totaal_prijs = kaas_kilogram*kaas_prijs + eieren*ei_prijs + melk_liter*melk_prijs + vlees_kilogram*vlees_prijs

# print(totaal_prijs)

# #Opdracht 4

# naam = "Ferhan"
# print(naam)

# rente = 0.03
# saldo = 1500
# print(saldo*(1+rente))

# getallenreeks = [12, 13, 14, 15, 16]
# namenreeks = ["Amber", "Simone", "Katerina"]
# dictionary = {"Straat" : "Roerdomp", "Stad" : "Mijdrecht", "Land" : "Amerika"}

# print(dictionary["Straat"] + " " + dictionary["Land"])

# print(55/4)
# print(55//4) # Hoe vaak past 4 in zijn geheel in 55

# print(55%4) # Wat niet in zn geheel in 55 past. Het aantal van 0.75
# print(13*4)
# print(2**3)

# # Opdracht 6

# print(212 / 24.0)
# print(212//24)
# print(212%24)
# #Het is op dat moment 20:00

# print(75//8)
# # 9 gehele bakken kan je vullen


# a = 5
# b = 5
# print(a**2+b**2)

# c = a**2+b**2
# c = c**0.5
# print(c)


# # 100% = 1.0
# # # 10% = 0.1
# # 1% = 0.01
# # 0.1% = 0.001

# rente = 0.002
# saldo = 1000
# maanden = 48

# print(saldo * ((1+rente) ** 48))

# naam = input("Wat is je naam? ")
# print("Hallo " + naam + ". Leuk, om je te ontmoeten.")
# print(f"Hey {naam}. Leuk om je te ontmoeten.")


# naam = input("Wat is je naam? ")
# leeftijd = input("Wat is je leeftijd? ")
# # print(f"Hallo {naam}, u bent {leeftijd} jaar oud.")

# leeftijd = int(input("Wat is je leeftijd? "))
# jaren_tot_pensioen = 67 - leeftijd
# print(f"U kan met {jaren_tot_pensioen} jaar met pensioen")

# a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(a[-1])
# print(a[0])
# print(a[1:9:2]) # begin:eind-1:stappen van 2
# print(a[:]) # Hele lijst
# print(a[-1]) # Laatste cijfer van lijst
# print(a[8:4:-1]) # Schrijft de lijst andersom
# aa = [[1,2,3],[4,5,6],[7,8,9]] 
# print(aa[0])# Print eerste lijst uit
# print(aa[0][0]) # Print eerste getal van eerste lijst uit.
# print(aa[0][1]) # Tweede getal van eerste lijst
# #g) Slicing is begin en eind aan te geven en daarna de stap
# # s = "Dit is een string"
# #  print(s[7:10])

# s = "Ferhan"
# print(s[-1::-1]) ##-1 is het laatste element -1:0 -> betekent tot 0. Dus je moet gewoon de 0 weglaten [-1::] 

# c = [1,2,3,4,5]
# c.append(6)
# print(c)
# # append voegt nog een getal toe aan de lijst

# ## Opdracht 9 en 10
# # d = c
# # d.append(7)
# # # Je ziet dat c de waarde van d heeft genomen.
# d = c[:]
# d.append(7)
# print(d)
# print(c)

# #Opdracht 11
# #e = [40, 50, 60, 70, 80, 80, 80]
# e = [100, 30, 50, 70, 30, 40, 60]
# print(len(e))
# print(max(e)) # max zoekt het hoogste cijfer in de lijst
# print(min(e)) # min zoekt het laagste cijfer in de lijst
# print(set(e)) #Alle cijfers 1x opnoemen in een lijst
# print(sum(e))

# Opdracht 12

f = [38, 20, 49, 75, 8, 9, 8]
# f is de functienaam
# [ 38, ..] Dit is een lijst van f

f.sort()
print(f) # Deze functie sorteert de list

f.pop(-1)
print(f) # -1 is het laatste getal in de list. pop laat een bepaalde slice uit de list weg bij het printen

f.remove(49)
print(f) # 49 is het getal uit de list. Deze is dankzij de functie remove verwijderd uit de list. De nieuwe f functie wordt geprint zonder het getal 49 in de list.


# Opdracht 13
tekst = "hey, ik ben Ferhan"
x = tekst.capitalize()
print(x)

y = tekst.isupper()
print(y) # Controleren of de tekst in hoofdletters is geschreven.

z = tekst.upper()
print(z) # Alles hoofdletters maken

a = tekst.lower()
print(a) # Alles kleine letters maken

b = tekst.center(20)
print(b)



# if "Optellen" or "+" or "plus" in vraag:
#   z = x + y
# elif "Aftrekken" or "min" or "-" in vraag:
#   z = x - y
# elif "Vermenigvuldigen" or "keer" or "*" in vraag:
#   z = x * y
# elif "Delen" or ":" or "/" in vraag:
#   z = x / y