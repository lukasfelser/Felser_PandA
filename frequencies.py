
def frequencies(t: str) -> dict:

    freqs = {}
    english_alphabet = "abcdefghijklmnopqrstuvwxy"        # defining all "letter" characters

    for line in t:                                        # eliminating all non letter characters
        for char in line:
            if char not in english_alphabet:
                t = t.replace(char, "")

    for line in t:                                        # iterating through cleaned file
        for char in line:                                 # iterating over each character
            if char in freqs:
                freqs[char] += 1                          # adding 1 to each instance of the character
            else:
                freqs[char] = 1                           # setting value to 1 if character not in freqs (yet)

    return freqs
