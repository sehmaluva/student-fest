import base64

def ceasar_decode(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = "A" if char.isupper() else "a"
            result += chr((ord(char) - ord(base)- shift) % 26 + ord(base))
        else:
            result += char
            
    return result

def base64_decode(text):
    return base64.b64decode(text.encode()).decode()
