"""
Write a Python function named morse_translator that translates a given string into Morse code.

Each alphabetic character in the string should be translated to its corresponding Morse code equivalent.
The Morse code for each character should be separated by a space.
Each word in the string should be separated by a forward slash (/).
The function should handle both uppercase and lowercase alphabetic characters.
The function should be case-insensitive, meaning it treats uppercase and lowercase letters the same.
Non-alphabetic characters (like numbers or symbols) should not be translated.

https://en.wikipedia.org/wiki/Morse_code
"""


def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }
    #Convert the text into uppercase for case-insensitivity:
    text= text.upper()
    
    #Translate each character to Morse code:
    morse_translated = [] #Create an empty list to store the translated Morse code
    for char in text:
        if char in morse_code_dict:
            morse_translated.append(morse_code_dict[char])
        elif char == " ":
            morse_translated.append("/") 
        
    #Join the Morse code symbols into a string
    return " ".join(morse_translated)

# Test cases
print(morse_translator("HELLO WORLD"))  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -."
print(morse_translator("Morse Code"))  # Expected output: "-- --- .-. ... . / -.-. --- -.. ."