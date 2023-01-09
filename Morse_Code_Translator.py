import RPi.GPIO as GPIO
import time

output_pin = 14
# Telling the Pi what that the ping is the GPIO pin not the board pin
GPIO.setmode(GPIO.BCM)
# Tell ing the Pi that the pin is outputing
GPIO.setup(output_pin, GPIO.OUT)

print("This turns text into morse code!!")
while True:
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

    # Does a check to see what set of actions the Pi should take for that code
    for element in range(0, len(cipher)):
        if cipher[element] == '.':
            GPIO.output(output_pin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(output_pin, GPIO.LOW)
        elif cipher[element] == '-':
            GPIO.output(output_pin, GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(output_pin, GPIO.LOW)
        elif cipher[element] == ' ':
            time.sleep(1.5)
        else:
            time.sleep(3.5)
