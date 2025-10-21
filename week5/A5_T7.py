#A5_T7 Word in a string 

DELIMITER = ","

def analyseWords(words):
    if words == "":
        print("No words entered.")
        return
    
    wordList = words.split(DELIMITER)
    wordCount = len(wordList)
    charCount = 0
    for word in wordList:
        charCount += len(word)
    avg = charCount / wordCount

    print(f"- {wordCount} Words")
    print(f"- {charCount} Characters")
    print("- {:.2f} Average word length".format(avg))


def collectWords():
    words = ""
    while True:
        word = input("Insert word (empty stops): ")
        if word == "":
            break
        if words != "":
            words += DELIMITER
        words += word  
    return words

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")

main ()