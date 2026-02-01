"""
Simple Caesar cipher implementation.
"""


def caesar_encrypt(text, shift=3):
    """
    Encrypt text using Caesar cipher.

    :param text: Input text (str)
    :param shift: Shift value (int)
    :return: Encrypted text (str)
    """
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result
