# Escape vom alten Pferdehof

inventory = []
inventory_limit = 5

rooms = {
    "Stall": [
        {"name": "Halfter", "type": "tool"},
        {"name": "Hufeisen", "type": "clue"},
    ],
    "Scheune": [
        {"name": "Schlüssel", "type": "key"},
        {"name": "Sattel", "type": "tool"}
    ],
    "Wohnhaus": [
        {"name": "Notiz", "type": "info"},
        {"name": "Apfel", "type": "food"},
    ]
}

current_room = "Stall"


def show_room_items():
    print(f"\n Du bist im {current_room}. Hier findest du:")
    for item in rooms[current_room]:
        print(f"- {item['name']}")


def show_inventory():
    print("\n Dein Inventar:")
    if not inventory:
        print("  (leer)")
    for item in inventory:
        print(f"- {item['name']} ({item['type']})")


def pick_up(item_name):
    global inventory
    for item in rooms[current_room]:
        if item['name'].lower() == item_name.lower():
            if len(inventory) >= inventory_limit:
                print("Dein Inventar ist voll!")
                return
            inventory.append(item)
            rooms[current_room].remove(item)
            print(f" Du hast {item['name']} aufgehoben.")
            return
    print("Dieses Item ist hier nicht.")


def drop(item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            inventory.remove(item)
            rooms[current_room].append(item)
            print(f" Du hast {item['name']} abgelegt.")
            return
    print("Du hast dieses Item nicht bei dir.")


def use(item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            if item['name'].lower() == "schlüssel" and current_room == "Stall":
                print("🔓 Du hast das Tor zum Pferdehof aufgeschlossen und bist entkommen!")
                print("🎉 GLÜCKWUNSCH – DU HAST GEWONNEN!")
                exit()
            else:
                print(f"Du benutzt {item['name']}, aber es passiert nichts.")
            return
    print("Du hast dieses Item nicht bei dir.")


def examine(item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            print(f"🔍 Du untersuchst {item['name']}. Es ist ein {item['type']}.")
            if item['name'].lower() == "notiz":
                print("📜 Auf der Notiz steht: 'Der Schlüssel ist gut versteckt in der Scheune.'")
            return
    print("Du hast dieses Item nicht bei dir.")


def change_room(new_room):
    global current_room
    new_room = new_room.capitalize()
    if new_room in rooms:
        current_room = new_room
        print(f"\n Du gehst in den {new_room}.")
        show_room_items()
    else:
        print("Diesen Raum gibt es nicht.")


def help_menu():
    print("""
Verfügbare Befehle:
- inventory                  → Zeige dein Inventar
- pickup [item]             → Hebe einen Gegenstand auf
- drop [item]               → Lege einen Gegenstand ab
- use [item]                → Benutze einen Gegenstand
- examine [item]            → Untersuche einen Gegenstand
- go [raumname]             → Wechsle den Raum (Stall, Scheune, Wohnhaus)
- help                      → Zeige diese Hilfe erneut
""")


def main():
    print("🐴 WILLKOMMEN auf dem alten Pferdehof.")
    print("🔒 Du bist eingeschlossen. Finde den Schlüssel und entkomme!")
    help_menu()
    show_room_items()

    while True:
        command = input("\n> ").strip().lower()

        if command == "inventory":
            show_inventory()
        elif command.startswith("pickup "):
            pick_up(command[7:].strip())
        elif command.startswith("drop "):
            drop(command[5:].strip())
        elif command.startswith("use "):
            use(command[4:].strip())
        elif command.startswith("examine "):
            examine(command[8:].strip())
        elif command.startswith("go "):
            change_room(command[3:].strip())
        elif command == "help":
            help_menu()
        else:
            print(" Unbekannter Befehl. Gib 'help' ein für eine Liste.")


main()

