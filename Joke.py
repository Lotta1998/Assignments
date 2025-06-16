import pyjokes
import cowsay

# Hole einen zufälligen Witz
witz = pyjokes.get_joke()

# Lass die Kuh den Witz erzählen
cowsay.cow(witz)
