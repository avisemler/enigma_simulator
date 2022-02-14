from config import Config
from rotor import Rotor
from enigma import Enigma
from reflector import Reflector
from plugboard import Plugboard

settings = Config("abcdefghijklmnopqrstuvwxyz")

rotor1 = Rotor(links="EKMFLGDQVZNTOWYHXUSPAIBRCJ", rotation=0, move_next="r", config=settings)
rotor2 = Rotor(links="AJDKSIRUXBLHWTMCQGZNPYFVOE", rotation=0, move_next="f", config=settings)
rotor3 = Rotor(links="BDFHJLCPRTXVZNYEIWGAKMUSQO", rotation=0, move_next="w", config=settings)

reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT", settings)

enigma = Enigma([rotor1, rotor2, rotor3], Plugboard(""), reflector)

#Demostrate the self-inverse nature
string = input("Enter a string to encode: ")
print("After one encoding ", out := enigma.encode(string))
enigma.reset()
print("After resetting the enigma and reapplying  ", enigma.encode(out))