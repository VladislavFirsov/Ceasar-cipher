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

def cipher_sentence(sentence, key):
    ciphered_sentence = ""
    for i in sentence:
        if i.isupper():
            i = i.lower()
            ciphered_sentence += eng_alphabet[(eng_alphabet.index(i) + key) %
                                          len(eng_alphabet)].upper()
        elif i in eng_alphabet:
            ciphered_sentence += eng_alphabet[(eng_alphabet.index(i) + key) %
                                          len(eng_alphabet)]
        else:
            ciphered_sentence += i
    return ciphered_sentence


def decipher_sentence(sentence, key):
    ciphered_sentence = ""
    for i in sentence:
        if i.isupper():
            i = i.lower()
            ciphered_sentence += eng_alphabet[(eng_alphabet.index(i) - key) %
                                              len(eng_alphabet)].upper()
        elif i in eng_alphabet:
            ciphered_sentence += eng_alphabet[(eng_alphabet.index(i) - key) %
                                              len(eng_alphabet)]
        else:
            ciphered_sentence += i
    return ciphered_sentence


def main():
    what_to_do = input('Please, enter a command: cipher or decipher?: ')
    while what_to_do not in ('cipher, decipher'):
        what_to_do = input('I don\'t understand, please, ender a command: cipher or decipher?: ')
    sentence = take_sentence()
    key = take_key()
    if what_to_do == 'cipher':
        print(cipher_sentence(sentence, key))
    else:
        print(decipher_sentence(sentence, key))

if __name__ == '__main__':
    main()




