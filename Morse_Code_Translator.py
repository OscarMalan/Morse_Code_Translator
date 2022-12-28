import RPi.GPIO as GPIO
import time
import numpy as np

output_pin = 14

print("This turns text into morse code!!")
Message = input("Type your message please:  ")

Translation = {}
x = 0
Message = Message.lower()

# Turning the text into Morse Code
for letter in [*Message]:
    if letter == 'a':
        Translation.update({x: [1, 3]})
    elif letter == 'b':
        Translation.update({x: [3, 1, 1, 1]})
    elif letter == 'c':
        Translation.update({x: [3, 1, 3, 1]})
    elif letter == 'd':
        Translation.update({x: [3, 1, 1]})
    elif letter == 'e':
        Translation.update({x: [1]})
    elif letter == 'f':
        Translation.update({x: [1, 1, 3, 1]})
    elif letter == 'g':
        Translation.update({x: [3, 3, 1]})
    elif letter == 'h':
        Translation.update({x: [1, 1, 1, 1]})
    elif letter == 'i':
        Translation.update({x: [1, 1]})
    elif letter == 'j':
        Translation.update({x: [1, 3, 3, 3]})
    elif letter == 'k':
        Translation.update({x: [3, 1, 3]})
    elif letter == 'l':
        Translation.update({x: [1, 3, 1, 1]})
    elif letter == 'm':
        Translation.update({x: [3, 3]})
    elif letter == 'o':
        Translation.update({x: [3, 3, 3]})
    elif letter == 'p':
        Translation.update({x: [1, 3, 3, 1]})
    elif letter == 'q':
        Translation.update({x: [3, 3, 1, 3]})
    elif letter == 'r':
        Translation.update({x: [1, 3, 1]})
    elif letter == 's':
        Translation.update({x: [1, 1, 1]})
    elif letter == 't':
        Translation.update({x: [3]})
    elif letter == 'u':
        Translation.update({x: [1, 1, 3]})
    elif letter == 'v':
        Translation.update({x: [1, 1, 1, 3]})
    elif letter == 'w':
        Translation.update({x: [1, 3, 3]})
    elif letter == 'x':
        Translation.update({x: [3, 1, 1, 3]})
    elif letter == 'y':
        Translation.update({x: [3, 1, 3, 3]})
    elif letter == 'z':
        Translation.update({x: [3, 3, 1, 1]})
    elif letter == ' ':
        Translation.update({x: "space"})
    else:
        print("error")
        exit()
    x += 1
    Translation.update({x: "wait"})
    x += 1

x -= 1
del Translation[x]

print(len(Translation[4]))


#for i in Translation:
#    if np.searchsorted(Translation[i], 1):
#        print("Dot")
#    elif np.searchsorted(Translation[i], 3):
#        print("Dash")
#    else:
#        print(Translation[i])


