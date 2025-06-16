import random

# Farboptionen
color_options = {
    "schwarz": 30,
    "rot": 31,
    "grün": 32,
    "gelb": 33,
    "blau": 34,
    "magenta": 35,
    "cyan": 36,
    "weiß": 37
}

def generate_sky_full_of_stars(height, width, star_count, star_symbol, star_color_code):
    # Erzeuge den Himmel mit zufällig platzierten Sternen
    for i in range(height):  # Äußere Schleife für jede Zeile
        row = ""  # Zeile leeren, um Platz für die Sterne zu schaffen
        for j in range(width):  # Innere Schleife für jede Spalte
            # Zufällig entscheiden, ob an dieser Stelle ein Stern ist
            if random.random() < star_count / (width * height):
                row += f"\033[{star_color_code}m{star_symbol}\033[0m"  # Stern mit Symbol und Farbe
            else:
                # Leerer Raum für den Hintergrund
                row += " "
        print(row)  # Zeile ausgeben

# Benutzereingaben
width = int(input("Gib die Breite des Sternenhimmels ein (20-60): "))
height = int(input("Gib die Höhe des Sternenhimmels ein (5-25): "))
star_count = int(input("Gib die Anzahl der Sterne an (1-100): "))

# Benutzer wählt ein Symbol für die Sterne
star_symbol = input("Gib das Symbol für die Sterne ein (*, +, o): ")

# Farbwahl
print("Wähle eine Farbe für die Sterne aus den folgenden Optionen:")
for color in color_options:
    print(color)

chosen_star_color = input("Gib deine gewählte Farbe für die Sterne ein: ").lower()


if chosen_star_color in color_options:
    star_color_code = color_options[chosen_star_color]
else:
    print("Ungültige Farbe für die Sterne, Standardfarbe wird verwendet.")
    star_color_code = color_options["weiß"]

# Den Sternenhimmel generieren
generate_sky_full_of_stars(height, width, star_count, star_symbol, star_color_code)