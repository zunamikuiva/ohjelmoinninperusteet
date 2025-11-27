# A7_T7 - Enigma machine

import string

ALPHABET = string.ascii_uppercase

def loadConfig(filename):
    """
    Load rotor and reflector configuration from a file.
    Expecting file format:
    Rotor1:<letters>
    Rotor2:<letters>
    Rotor3:<letters>
    Reflector:<letters>
    """
    rotors = []
    reflector = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Rotor1:"):
                rotors.append(line.split(":")[1])
            elif line.startswith("Rotor2:"):
                rotors.append(line.split(":")[1])
            elif line.startswith("Rotor3:"):
                rotors.append(line.split(":")[1])
            elif line.startswith("Reflector:"):
                reflector = line.split(":")[1]
    return rotors, reflector

def rotateRotors(positions):
    """
    Rotate the rotors: rightmost rotor always moves.
    """
    positions[2] = (positions[2] + 1) % 26
    if positions[2] == 0:
        positions[1] = (positions[1] + 1) % 26
        if positions[1] == 0:
            positions[0] = (positions[0] + 1) % 26

def forwardPass(c, rotors, positions):
    """
    Pass letter forward through the rotors
    """
    index = ALPHABET.index(c)
    for rotor, pos in zip(rotors, positions):
        index = (index + pos) % 26
        c = rotor[index]
        index = ALPHABET.index(c)
    return c

def backwardPass(c, rotors, positions):
    """
    Pass letter backward through the rotors (reverse order)
    """
    index = ALPHABET.index(c)
    for rotor, pos in zip(rotors[::-1], positions[::-1]):
        index = rotor.index(ALPHABET[index])
        index = (index - pos) % 26
        c = ALPHABET[index]
    return c

def reflect(c, reflector):
    """
    Pass letter through reflector
    """
    index = ALPHABET.index(c)
    return reflector[index]

def enigmaEncode(text, rotors, reflector):
    positions = [0,0,0]
    result = ""
    for ch in text:
        if ch not in ALPHABET:
            result += ch
            continue
        rotateRotors(positions)
        c = forwardPass(ch, rotors, positions)
        c = reflect(c, reflector)
        c = backwardPass(c, rotors, positions)
        result += c
        print(f'Character "{ch}" illuminated as "{c}"')
    return result

def main():
    print("Enigma Machine starting.")
    config_file = input("Insert config(filename): ")
    plug = input("Insert plugs (y/n)?: ")
    if plug.lower() == "y":
        print("Plugboard not implemented. Ignoring plugs.")
    else:
        print("No extra plugs inserted.")
    
    rotors, reflector = loadConfig(config_file)
    print("Enigma initialized.\n")

    while True:
        row = input("Insert row (empty stops): ").upper()
        if row == "":
            break
        converted = enigmaEncode(row, rotors, reflector)
        print(f'Converted row - "{converted}".\n')

    print("Enigma closing.")

if __name__ == "__main__":
    main()
