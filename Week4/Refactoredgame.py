import time

# Konstanten
HUNGER_MIN = 1
HUNGER_MAX = 5
ESSENSTYPEN = ["vegan", "vegetarisch", "fleisch"]
ESSENSARTEN = ["warmes", "kaltes"]

# Funktionen

def begruessung():
    print("Es ist Abends und dein Magen knurrt...")
    time.sleep(2)
    print("Du musst dich entscheiden:")
    time.sleep(2)
    print("Was soll es heute zum Abendessen geben?")
    time.sleep(2)

def frage_hunger() -> int:
    """Fragt den Hungerlevel des Nutzers ab und gibt eine Zahl zwischen 1-5 zurück."""
    while True:
        try:
            hunger = int(input("Auf einer Skala von 1 bis 5: Wie hungrig bist du gerade? "))
            if HUNGER_MIN <= hunger <= HUNGER_MAX:
                return hunger
            else:
                print(f"Bitte gib eine Zahl zwischen {HUNGER_MIN} und {HUNGER_MAX} ein.")
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")

def reagiere_auf_hunger(hunger: int):
    reaktionen = {
        1: "Für dich wäre ein Snack geeignet!",
        2: "Das klingt nach größerem Appetit!",
        3: "Du brauchst eine Zwischenmahlzeit",
        4: "Ab in die Küche mit dir!",
        5: "Das klingt, als hättest du einen riesigen Hunger!"
    }
    print(reaktionen.get(hunger))

def frage_essens_typ() -> str:
    while True:
        typ = input("Bist du vegan, vegetarisch oder isst du Fleisch? ").lower()
        if typ in ESSENSTYPEN:
            return typ
        else:
            print("Ungültige Eingabe! Bitte wähle 'vegan', 'vegetarisch' oder 'fleisch'.")

def frage_essens_art() -> str:
    while True:
        art = input("Möchtest du lieber etwas warmes oder kaltes? ").lower()
        if art in ESSENSARTEN:
            return art
        else:
            print("Ungültige Wahl! Bitte wähle 'warmes' oder 'kaltes'.")

def empfehlung_essen(typ: str, art: str):
    vorschlaege = {
        ("vegan", "warmes"): "Wie wäre es mit Linsencurry?",
        ("vegan", "kaltes"): "Wie wäre es mit Gurken-Maki?",
        ("vegetarisch", "warmes"): "Wie wäre es mit einer Linsenbolognese?",
        ("vegetarisch", "kaltes"): "Wie wäre es mit einem sommerlichen Nudelsalat?",
        ("fleisch", "warmes"): "Wie wäre es mit Spaghetti Bolognese?",
        ("fleisch", "kaltes"): "Wie wäre es mit einem bunten Salat mit Hähnchenbrust?",
    }
    print(vorschlaege.get((typ, art)))

def frage_dessert(hunger: int):
    if hunger >= 4:
        while True:
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

def main():
    begruessung()
    hunger = frage_hunger()
    reagiere_auf_hunger(hunger)
    essenstyp = frage_essens_typ()
    essensart = frage_essens_art()
    empfehlung_essen(essenstyp, essensart)
    time.sleep(2)
    frage_dessert(hunger)
    time.sleep(2)
    print("Guten Appetit! ")

if __name__ == "__main__":
    main()
