import base64

def ceasar_encode(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char

    return result

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()