# variabele_5 = 10

#Opdracht 2 en 3 Boodschappenlijst

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

#Opdracht 4

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

# Opdracht 6

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
# g) Slicing is begin en eind aan te geven en daarna de stap
# s = "Dit is een string"
# # # print(s[7:10])
# s = "I'm Ferhan "
# print(s[10:3:-1])

c = [1,2,3,4,5]
c.append(6)
# print(c)
# append voegt nog een getal toe aan de lijst

# d = c
# d.append(7)
# print(c)
# # Je ziet dat c de waarde van d heeft genomen.
d = c[:]
d.append(7)
print(c)
print(d)