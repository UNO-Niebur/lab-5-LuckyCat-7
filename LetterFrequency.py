#LetterFrequency.py
#Name:Tori Gregory
#Date:2/22/26
#Assignment:Lab 5

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for letters in message:
        if letters == "A":
            spot = 0
        elif letters == "B":
            spot = 1
        elif letters == "C":
            spot = 2
        elif letters == "D":
            spot = 3
        elif letters == "E":
            spot = 4
        elif letters == "F":
            spot = 5
        elif letters == "G":
            spot = 6
        elif letters == "H":
            spot = 7
        elif letters == "I":
            spot = 8
        elif letters == "J": 
            spot = 9
        elif letters == "K": 
            spot = 10   
        elif letters == "L": 
            spot = 11   
        elif letters == "M": 
            spot = 12   
        elif letters == "N": 
            spot = 13
        elif letters == "O": 
            spot = 14
        elif letters == "P": 
            spot = 15
        elif letters == "Q": 
            spot = 16
        elif letters == "R": 
            spot = 17
        elif letters == "S": 
            spot = 19
        elif letters == "T": 
            spot = 20
        elif letters == "U": 
            spot = 21
        elif letters == "V": 
            spot = 22
        elif letters == "W": 
            spot = 22
        elif letters == "X": 
            spot = 23
        elif letters == "Y": 
            spot = 24
        elif letters == "Z": 
            spot = 25
        freq[spot] = freq[spot] + 1 

    #loop through each letter
    #Find the position in the alphabet
    #Increase the frequency at that position. If position was 5, then frequencies[5] = frequencies[5] + 1




    #Create the output text in the format A,5\n if there were 5 letter A in the message.
    #Remember that the \n is the symbol for a new lin
    output = ""
    for i in range(26):
        print (alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output = output + line

    writeToFile(output)


def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    freqFile = open("frq.csv", 'w')
    freqFile.write(fileText)

    freqFile.close()


def main():
    msg = input("Enter a message: ")
    countLetters(msg)



if __name__ == '__main__':
  main()
