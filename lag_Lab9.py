def encode(password):
    encoded = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded

def decode(password):
    decoded = ''.join(str((int(char) - 3) % 10) for char in password)
    return decoded