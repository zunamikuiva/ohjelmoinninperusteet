# A6_T7  Messages from the Four Emperors


import os
import codecs

def rot13(text):
    return codecs.encode(text, "rot_13")


locations = {
    0: "home",
    1: "Galba's palace",
    2: "Otho's palace",
    3: "Vitellius' palace",
    4: "Vespasian's palace"
}

progress_file = "player_progress.txt"


if not os.path.exists(progress_file):
    with open(progress_file, "w") as f:
        f.write("current_location;next_location;passphrase\n")
        f.write("0;1;qvfpvcyvar\n")

with open(progress_file, "r") as f:
    lines = f.read().strip().split("\n")

last_line = lines[-1].split(";")
current_location = int(last_line[0])
next_location = int(last_line[1])
passphrase = last_line[2]


if next_location not in locations:
    print("All emperors already visited.")
    quit()


print("Travel starting.")
print(f"Currently at {locations[current_location]}.")
print(f"Travelling to {locations[next_location]}...")
print(f"...Arriving to the {locations[next_location]}.")
print("Passing the guard at the entrance.")

plain_pass = rot13(passphrase)
print(f"\"{plain_pass}!\"")

print("Looking for the message in the palace...")


cipher_file = f"{next_location}_{passphrase}.gkg"

if not os.path.exists(cipher_file):
    print("Message file not found:", cipher_file)
    quit()

print("Ah, there it is! Seems cryptic.")


with open(cipher_file, "r") as f:
    first_line = f.readline().rstrip()
    rest = f.read()


with open(progress_file, "a") as f:
    f.write(f"{current_location};{next_location};{passphrase}\n")
    f.write(first_line + "\n")

print("[Game] Progress autosaved!")


decoded_message = rot13(first_line + "\n" + rest)


plain_file = f"{next_location}-{plain_pass}.txt"

with open(plain_file, "w") as f:
    f.write(decoded_message)

print("Deciphering Emperor's message...")
print("Looks like I've got the plain version of the Emperor's message.")
print("Time to leave...")
print("Travel ending.")
