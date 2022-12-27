# import RPi.GPIO as GPIO

print("This turns text into morse code!!")
Message = input("Type your message please:  ")

Translation = {}
i = 0
Message = Message.lower()

# Turning the text into Morse Code
for letter in [*Message]:
    if letter == 'a':
        Translation.update({i: [1, 3]})
    elif letter == 'b':
        Translation.update({i: [3, 1, 1, 1]})
    elif letter == 'c':
        Translation.update({i: [3, 1, 3, 1]})
    elif letter == 'd':
        Translation.update({i: [3, 1, 1]})
    elif letter == 'e':
        Translation.update({i: [1]})
    elif letter == 'f':
        Translation.update({i: [1, 1, 3, 1]})
    elif letter == 'g':
        Translation.update({i: [3, 3, 1]})
    elif letter == 'h':
        Translation.update({i: [1, 1, 1, 1]})
    elif letter == 'i':
        Translation.update({i: [1, 1]})
    elif letter == 'j':
        Translation.update({i: [1, 3, 3, 3]})
    elif letter == 'k':
        Translation.update({i: [3, 1, 3]})
    elif letter == 'l':
        Translation.update({i: [1, 3, 1, 1]})
    elif letter == 'm':
        Translation.update({i: [3, 3]})
    elif letter == 'o':
        Translation.update({i: [3, 3, 3]})
    elif letter == 'p':
        Translation.update({i: [1, 3, 3, 1]})
    elif letter == 'q':
        Translation.update({i: [3, 3, 1, 3]})
    elif letter == 'r':
        Translation.update({i: [1, 3, 1]})
    elif letter == 's':
        Translation.update({i: [1, 1, 1]})
    elif letter == 't':
        Translation.update({i: [3]})
    elif letter == 'u':
        Translation.update({i: [1, 1, 3]})
    elif letter == 'v':
        Translation.update({i: [1, 1, 1, 3]})
    elif letter == 'w':
        Translation.update({i: [1, 3, 3]})
    elif letter == 'x':
        Translation.update({i: [3, 1, 1, 3]})
    elif letter == 'y':
        Translation.update({i: [3, 1, 3, 3]})
    elif letter == 'z':
        Translation.update({i: [3, 3, 1, 1]})
    elif letter == ' ':
        Translation.update({i: "space"})
    else:
        print("error")
        exit()
    i += 1
    Translation.update({i: "wait"})
    i += 1

print(Translation)