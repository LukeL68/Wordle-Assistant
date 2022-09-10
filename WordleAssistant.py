# Wordle Assistant

###################################################################################

WordListFile = open("D:\Coding\WordleAssistant\WordListFile.txt","r")
wordList = WordListFile.readlines()

possibleWords = []

# False = unknown character (second dimension serves as blacklist), True = known character (second dimension serves as whitelist)
filter = [[False,""],[False,""],[False,""],[False,""],[False,""]]
knownCharacters = ""
knownCharactersTally = 0

guess = ["","","","","",""]
result = ["","","","","",""]

for i in range(len(wordList)):
    wordList[i] = wordList[i].rstrip('\n')
    print(wordList[i])

for round in range(6):

    guess[round] = input("Enter guess #" + str(round+1) + ": ")
    result[round] = input("Enter results: ")

    for letterIndex in range(5):
        if result[round][letterIndex] == "0":
            for i in range(5):
                # Add this character to all blacklists
                if filter[i][0] == False:
                    filter[i][1] += guess[round][letterIndex]
        elif result[round][letterIndex] == "1":
            # Add this character to blacklist for this index if unknown and add to string of known characters
            if filter[letterIndex][0] == False:
                    filter[letterIndex][1] += guess[round][letterIndex]
            knownCharacters += guess[round][letterIndex]
        elif result[round][letterIndex] == "2":
            #Clear blacklist for this index and add this character to whitelist for this index
            filter[letterIndex][0] = True
            filter[letterIndex][1] = ""
            filter[letterIndex][1] = guess[round][letterIndex]
    
    for i in range(len(wordList)):
        print("Checking: " + wordList[i])
        # run filter
        for letterIndex in range(5):
            # if true (whitelist)
            print("filtering...")
            if filter[letterIndex][0]:
                print("checking if " + wordList[i][letterIndex] + " is in " + filter[letterIndex][1] + " (whitelist for character " + str(letterIndex+1) + ")")
                if wordList[i][letterIndex] in filter[letterIndex][1]:
                    passFilter = True
                    print("pass!")
                else:
                    passFilter = False
                    print("fail!")
            else:
                print("checking if " + wordList[i][letterIndex] + " is in " + filter[letterIndex][1] + " (blacklist for character " + str(letterIndex+1) + ")")
                if wordList[i][letterIndex] in filter[letterIndex][1]:
                    passFilter = False
                    print("fail!")
                else:
                    passFilter = True
                    print("passsed filters for this character!")
            
            if not passFilter:
                print("Word failed!")
                break

        if passFilter:
            print("checking characters...")
            if passFilter:
                for k in range(len(knownCharacters)):
                    print("Checking if " + knownCharacters[k] + " is in the word " + wordList[i])
                    if knownCharacters[k] in wordList[i]:
                        passFilter = True
                        print("passed check for this character!")
                    else:
                        passFilter = False
                        print("fail")
                        break
        else:
            print("Word failed!")
                
        if passFilter:
            print("Word passed!")
            possibleWords.append(wordList[i])

    # update word list with possible words
    wordList.clear()
    for j in range(len(possibleWords)):
        wordList.append(possibleWords[j])
    possibleWords.clear()
    
    print("Number of possible words: " + str(len(wordList)))
    print("Possible words: " + str(wordList))

    
for i in range(5):
        print("Known letter: " + str(filter[i][0]))
        if filter[i][0]:
            print("Whitelist: " + str(filter[i][1]))
        else:
            print("Blacklist: " + str(filter[i][1]))






    
                
    











