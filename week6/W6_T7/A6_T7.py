LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELIMITER = ';'

def readFile(PfileName) -> str:
    content = ''
    fileHandle = open(PfileName, "r")
    row = fileHandle.readline()
    while row != '':
        content += row
        row = fileHandle.readline()
    fileHandle.close()

    return content

def writeFile() -> None:

    return None

def appendToFile() -> None:

    return None

def row() -> str:
    newContent = ''
    return newContent

def getLocation(locationId):
    location = "unknown"
    if locationId == 1:
        location = "Galba's palace"
    elif locationId == 2:
        location = "Otho's palace"
    elif locationId == 3:
        location = "Vitelliu's palace"
    elif locationId == 4:
        location "Vespasian's palace"
    elif locationId == 0:
        location = "Home"
    return location

def main() -> None:
    print("Travel starting.")
    playerProgressFileName = "player_progress.txt"
    progress = readFile(playerProgressFileName)
    lastProgress = progress.strip().split('\n')[-1].split(DELIMITER)
    currentLocationId = int(lastProgress[0])
    currentLocation = getLocation(currentLocationId)
    nextLocasionId = int(lastProgress[1])
    nextLocasion = getLocation(nextLocasionId)
    passPhrase = lastProgress[2]

    print(f"Currently at {currentLocation}.")
    print(f"Traveling to {nextLocasion}.")
    print(f"...Arriving to the {nextLocasion}.")
    print("Passing the guard at the entrance.")
    return None



main()