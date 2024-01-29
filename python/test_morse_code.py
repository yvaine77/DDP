import pytest
import morse_code

def test_morese_code():
    assert morse_code.morse_translator("Hello World") == ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    assert morse_code.morse_translator("Python") == ".--. -.-- - .... --- -."
    assert morse_code.morse_translator("Morse Code") == "-- --- .-. ... . / -.-. --- -.. ."
    