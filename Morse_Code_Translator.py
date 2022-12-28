# import RPi.GPIO as GPIO
import time
import numpy as np

output_pin = 14

print("This turns text into morse code!!")
message = input("Type your message please:  ")

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}

# Function to encrypt the string
# according to the morse code chart
cipher = ''
message = message.upper()
for letter in message:
    if letter != ' ':

        # Looks up the dictionary and adds the
        # corresponding morse code
        # along with a space to separate
        # morse codes for different characters
        cipher += MORSE_CODE_DICT[letter] + ' '
    else:
        # 1 space indicates different characters
        # and 2 indicates different words
        cipher += ' '

for element in range(0, len(cipher)):
    if cipher[element] == '.':
        print("dot")
    elif cipher[element] == '-':
        print("dash")
    elif cipher[element] == ' ':
        print('gap')
    else:
        print("space")