eng_alphabet = [chr(i) for i in range(97, 123)]

def take_sentence():
    sentence = input('Enter your sentence: ')
    return sentence

def validate_key(key):
    return key.isdigit() and 1 <= int(key) <= 26

def take_key():
    key = input('Enter your key: ')
    if validate_key(key):
        return int(key)
    else:
        while not validate_key(key):
            key = input('key must be an integer between 1 and 26: ')
    return int(key)

