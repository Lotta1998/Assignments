import time

print("Es ist Abends und dein Magen knurrt...")
time.sleep(2)
print("Du musst dich entscheiden:")
time.sleep(2)
print("Was soll es heute zum Abendessen geben?")

# 1. Eingabe: Hunger
time.sleep(2)
while True:
    try:
        hunger = int(input("Auf einer Skala von 1 bis 5: Wie hungrig bist du gerade? "))
        if 1 <= hunger <= 5:
            break
        else:
            print("Bitte gib eine Zahl zwischen 1 und 5 ein.")
    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")

if hunger == 1:
    print("Für dich wäre ein Snack geeignet!")
elif hunger == 2:
    print("Das klingt nach größerem Appetit!")
elif hunger == 3:
    print("Du brauchst eine Zwischenmahlzeit")
elif hunger == 4:
    print("Ab in die Küche mit dir!")
elif hunger == 5:
    print("Das klingt, als hättest du einen riesigen Hunger!")

# 2. Eingabe: Essensart (vegan, vegetarisch, fleisch)
time.sleep(2)
while True:  # Schleife für gültige Essensauswahl
    Essenstyp = input("Bist du vegan, vegetarisch oder isst du Fleisch? ").lower()
    if Essenstyp in ["vegan", "vegetarisch", "fleisch"]:
        break
    else:
        print("Ungültige Eingabe! Bitte wähle 'vegan', 'vegetarisch' oder 'fleisch'.")

# 3. Eingabe: Essensart (warm oder kalt)
if Essenstyp == "vegetarisch":
    while True:  # Schleife für gültige Essensart
        Essensart = input("Möchtest du lieber etwas warmes oder kaltes? ").lower()
        if Essensart == "warmes":
            print("Wie wäre es mit einer Linsenbolognese?")
            break
        elif Essensart == "kaltes":
            print("Wie wäre es mit einem sommerlichen Nudelsalat?")
            break
        else:
            print("Ungültige Wahl! Bitte wähle 'warmes' oder 'kaltes'.")

elif Essenstyp == "fleisch":
    while True:  # Schleife für gültige Essensart
        Essensart = input("Möchtest du lieber etwas warmes oder kaltes? ").lower()
        if Essensart == "warmes":
            print("Wie wäre es mit Spaghetti Bolognese?")
            break
        elif Essensart == "kaltes":
            print("Wie wäre es mit einem bunten Salat mit Hähnchenbrust?")
            break
        else:
            print("Ungültige Wahl! Bitte wähle 'warmes' oder 'kaltes'.")

elif Essenstyp == "vegan":
    while True:  # Schleife für gültige Essensart
        Essensart = input("Möchtest du lieber etwas warmes oder kaltes? ").lower()
        if Essensart == "warmes":
            print("Wie wäre es mit Linsencurry?")
            break
        elif Essensart == "kaltes":
            print("Wie wäre es mit Gurken-Maki?")
            break
        else:
            print("Ungültige Wahl! Bitte wähle 'warmes' oder 'kaltes'.")

# 4. Eingabe: Zusätzliche Frage basierend auf dem Essenswunsch
time.sleep(2)
if hunger >= 4:  # Wenn der Hunger groß ist
    while True:  # Schleife für gültige Antwort auf Dessert
        extra = input("Hast du noch Platz für ein Dessert? (ja/nein) ").lower()
        if extra == "ja":
            print("Wie wäre es mit einem leckeren Schokoladenkuchen?")
            break
        elif extra == "nein":
            print("Okay, dann lassen wir das Dessert für heute!")
            break
        else:
            print("Ungültige Eingabe! Bitte antworte mit 'ja' oder 'nein'.")
else:
    print("Kein Dessert nötig, du hast genug gegessen!")

# Abschluss
time.sleep(2)
print("Guten Appetit!")

