import random

def rootword():
    vowels = list(u'aeiou')
    consonants = list(u'lmnrbdzvjgptsf\u0448k')
    form = random.randint(0, 1)
    s = u""
    if form:
        s = s + random.choice(consonants).upper()
        s = s + random.choice(consonants)
        s = s + random.choice(vowels)
        s = s + random.choice(consonants)
        s = s + random.choice(vowels)
    else:
        s = s + random.choice(consonants).upper()
        s = s + random.choice(vowels)
        s = s + random.choice(consonants)
        s = s + random.choice(consonants)
        s = s + random.choice(vowels)
    return s

if __name__ == "__main__":
    seed = int(raw_input("Seed? "))
    random.seed(seed)
    print rootword()
