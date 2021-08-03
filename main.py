# item = {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True, "weightInKilos": 0.5}
# item["price"] = 929
# print("Název položky je " + str(item["title"]))
# print("Cena je " + str(item["price"]))
# print("a","b","c",sep=",")
# print("Nadpis,")
# print(f"Cena položky je {item['price']}.")
# if "weightInKilos" in item:
#     print(item["weightInKilos"])
# else:
# #     print("neexistuje")
#
# předmět = {"Český jazyk": 2,"Dějepis": 1,"Matematika": 3}
# print(předmět)

# sausages.pop("Lucka")

# print(sausages.values())
# print(sausages)
# print(sum(sausages.values()))


# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }
# sales["Noc, která mě zabila"]=0
# sales["Zločinný steh"]=sales["Zločinný steh"]+100
# print(sales)

# tombola = {
#     7: "Láhev kvalitního vína Château Headache",
#     15: "Pytel brambor z místního družstva",
#     23: "Čokoládový dort",
#     47: "Kniha o historii města",
#     55: "Šiška salámu",
#     67: "Vyhlídkový let balónem",
#     79: "Moderní televizor",
#     91: "Roční předplatné městského zpravodaje",
#     93: "Společenská hra Sázky a dostihy",
# }
#
# ticketNumber = int(input("Jaké je číslo Vašeho lístku? "))
# if ticketNumber in tombola:
#     print(tombola[ticketNumber])
#     tombola.pop(ticketNumber)
# else:
#     print("Nic nevyhráváte.")
# print(tombola)

# passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
# jmeno = str(input("Jaké je vase jmeno? "))
# password = str(input("Jaké je číslo Vašeho heslo? "))
# if jmeno in passwords:
#     if passwords[jmeno]== password:
#         print("Můžeš vstoupit")


#BALÍKY


# baliky = {
#     "B541X": True,
#     "B547X": False,
#     "B251X": False,
#     "B501X": True,
#     "B947X": False,
# }
# balik = str(input("Jaký je kod Vašeho balíku? "))
# if balik in baliky:
#     if baliky[balik]== True:
#         print("balík byl předán kurýrovi")
#     else:
#         print("balik nebyl predán kuryrovi")
# else:
#     print("balík neexistuje")

#SKLADNÍK
# sklad = {
#   "1N4148": 250,
#   "BAV21": 54,
#   "KC147": 147,
#   "2N7002": 97,
#   "BC547C": 10
# }
#
# zbozi = str(input("Jaký je kod zboží?"))
# pocetKusu = int(input("Kolik kusů chcete koupit?"))
#
# if zbozi in sklad:
#     if sklad[zbozi] >= pocetKusu:
#         print("zboží je skladem")
#     else:
#         print(f"Skladem je pouze {sklad[zbozi]}")
#        sklad.pop(zbozi)

#
# else:
#     print("zboží není skladem")
#       sklad[zbozi]-=pocetKusu

#ZASEDACKY

# volnePokoje = {
#   9: ["Amadeus", "Goya", "Vlasy"],
#   10: ["Forman", "Goya"],
#   11: [],
#   12: ["Amadeus", "Vlasy"]
# }
#
# cas = int(input("Na kterou hodinu chcete zamluvit zasedačku?"))
# if cas in volnePokoje:
#     print(len(volnePokoje[cas]))
# else:
#     print("V tuto hodinu již není k dispozici žádná zasedací místnost")

#MORSEOVAABECEDA
# morseCode = {
#     "0": "-----",
#     "1": ".----",
#     "2": "..---",
#     "3": "...--",
#     "4": "....-",
#     "5": ".....",
#     "6": "-....",
#     "7": "--...",
#     "8": "---..",
#     "9": "----.",
#     "a": ".-",
#     "b": "-...",
#     "c": "-.-.",
#     "d": "-..",
#     "e": ".",
#     "f": "..-.",
#     "g": "--.",
#     "h": "....",
#     "i": "..",
#     "j": ".---",
#     "k": "-.-",
#     "l": ".-..",
#     "m": "--",
#     "n": "-.",
#     "o": "---",
#     "p": ".--.",
#     "q": "--.-",
#     "r": ".-.",
#     "s": "...",
#     "t": "-",
#     "u": "..-",
#     "v": "...-",
#     "w": ".--",
#     "x": "-..-",
#     "y": "-.--",
#     "z": "--..",
#     ".": ".-.-.-",
#     ",": "--..--",
#     "?": "..--..",
#     "!": "-.-.--",
#     "-": "-....-",
#     "/": "-..-.",
#     "@": ".--.-.",
#     "(": "-.--.",
#     ")": "-.--.-"
# }
#
# text = input("co chcete zapsat?")
# for i in text:
#     print(morseCode[i], end=" ")

#
# PRODEJE
# prodeje2019 = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }
#
# prodeje2020 = {
#     "Zkus mě chytit": 3157,
#     "Vrah zavolá v deset": 3541,
#     "Vražda podle knihy": 2510,
#     "Past": 2364,
#     "Zločinný steh": 5412,
# }
#
# kniha = input("Jaká kniha Vás zajímá?")
# soucet = 0
# if kniha in prodeje2019:
#     soucet = soucet + prodeje2019[kniha]
#
# soucet = soucet + prodeje2020[kniha]
# print(f"celkem se prodalo{soucet}")

# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }
# soucet = 0
# for nazev, prodano in sales.items():
#     print(f"Knihy {nazev} bylo prodáno {prodano} výtisků.")
#     soucet = soucet + prodano
# print("Bylo prodáno", soucet, "počet kusů.")
#
#
# sales = [
#     {"název":"Zkus mě chytit", "prodano":4165,"cena":347, "rok":2019},
#     {"název":"Vražda volá deset", "prodano":5681,"cena":299, "rok":2019},
#     {"název":"Zločinný steh", "prodano":2565,"cena":369,"rok":2020}
#
# ]
# trzbyzarok = 0
# for polozka in sales:
#     if polozka["rok"]==2020:
#         trzbyzarok = trzbyzarok + polozka["prodano"] * polozka["cena"]
# print(trzbyzarok)

#CTENÁŘSKÝDENÍK
#
# books = [
#     {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
#     {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
#     {"title": "Past", "pages": 390, "rating": 4},
#     {"title": "Popel popelu", "pages": 411, "rating": 10},
#     {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
#     {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
#     {"title": "Zločinný steh", "pages": 542, "rating": 8},
#     {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
#     {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
# ]
# soucet=0

# for polozka in books:
#     soucet = soucet + polozka["pages"]
#
# soucet2=0
# for polozka in books:
#     if polozka["rating"]>9:
#         soucet2 = soucet2 + polozka["pages"]
#
# print(soucet2)



schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělesná výchova": 3,
  "Chemie": 4,
}

# soucet = 0
# for predmet, znamka in schoolReport.items():
#     soucet = soucet + znamka
# print(soucet)
#
# print(len(schoolReport))
# prumer = soucet/(len(schoolReport))
# print(prumer)
#
# plates = {"4A2 3000": "František Novák",
#   "6P5 4747": "Jana Pilná",
#   "3B7 3652": "Jaroslav Sečkár",
#   "1P5 5269": "Marta Nováková",
#   "37E 1252": "Martina Matušková",
#   "2A5 2241": "Jan Král"
#           }
#
#
# for znacka, jmeno in plates.items():
#     if znacka[1]=="P":
#         print(jmeno)
#
#

{"person": "Petr", "item": "Prací prášek", "value": 399}

purchaseList = [
  {"person": "Petr", "item": "Prací prášek", "value": 399},
  {"person": "Ondra", "item": "Savo", "value": 80},
  {"person": "Petr", "item": "Toaletní papír", "value": 65},
  {"person": "Libor", "item": "Pivo", "value": 124},
  {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
  {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
  {"person": "Ondra", "item": "Toaletní papír", "value": 120},
  {"person": "Míša", "item": "Pečící papír", "value": 30},
  {"person": "Zuzka", "item": "Savo", "value": 80},
  {"person": "Pavla", "item": "Máslo", "value": 50},
  {"person": "Ondra", "item": "Káva", "value": 300}
]
sumPerPerson = {}
total = 0
for item in purchaseList:
    person = item["person"]
    total = total + item["value"]
    if person in sumPerPerson:
        sumPerPerson[person] = sumPerPerson[person]+item["value"]
    else:
        sumPerPerson[person] = item["value"]
    average_value = total/len(sumPerPerson)
    for person, value in sumPerPerson.items():
        if value>average_value:
            print(f"{person} dostane {value - average_value} Kč.")
        else:
            print(f"{person} doplatí {value - average_value} Kč.")


