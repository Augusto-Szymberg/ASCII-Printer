#            _____  _____ _____ _____   _____      _       _            
#     /\    / ____|/ ____|_   _|_   _| |  __ \    (_)     | |           
#    /  \  | (___ | |      | |   | |   | |__) | __ _ _ __ | |_ ___ _ __ 
#   / /\ \  \___ \| |      | |   | |   |  ___/ '__| | '_ \| __/ _ \ '__|
#  / ____ \ ____) | |____ _| |_ _| |_  | |   | |  | | | | | ||  __/ |   
# /_/    \_\_____/ \_____|_____|_____| |_|   |_|  |_|_| |_|\__\___|_|   
# By A.S.

# The following program is to print a desired text in a fun way.
# It browses through an ASCII array until it get to a desired letter.
# Then it locks it and continues until it has the desired output.
# This demo prints out hello world, you can edit it by changing the toPrint.
# It gets exponentialy slower the longer the toPrint is. 
                                                                     
from threading import Thread
import time

toPrint = "Hello World"

ASCII = ["!", '"', "#", "$" "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", 
         "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
         ":", ";", "<", "+", ">", "?", "@"
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
         "[", "]", "^", "_",
         "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
         "{", "|", "}", "~", " "]
prePrint = []

class first(Thread):
    def run(self):
       print("Run Program alt.HelloWorld ")
       HelloWorld = []
       for i in toPrint:
           HelloWorld.append(self.getLetterChain(i))

       x = 0
       for i in HelloWorld:
            for z in HelloWorld[x]:
                time.sleep(0.002)
                print(z, end = "")
            if x < (len(HelloWorld)-1):
                x = x + 1

    def getLetterChain(self, letter):
        letterChain = []
        letterPrinted = False
        for i in ASCII:
            if letterPrinted == False :
                if len(prePrint) != 0:
                    for x in prePrint:
                        letterChain.append(x)
                letterChain.append(i)
                letterChain.append("\n")
                if(i == letter):
                    letterPrinted = True
                    prePrint.append(i)
                    return(letterChain)

first().start()
