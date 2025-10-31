tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."




def count_vowels_and_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    rijecnik= {"vowels": 0, "consonants": 0}
    for letter in tekst:
        if letter in consonants:
            rijecnik["consonants"]+= 1
        elif letter in vowels: rijecnik["vowels"]+= 1
    return rijecnik

print(count_vowels_and_consonants(tekst))


