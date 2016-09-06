import random

def consonant_cluster(first_upper):
    sonorant = list(u'lmnr')
    voiced = list(u'bdzvjg')
    unvoiced = list(u'ptsf\u0448k')
    while True:
        form = [random.randint(0, 1), random.randint(0, 2)]
        if form[0]:
            a = random.choice(voiced)
            b = random.choice(voiced)
        else:
            a = random.choice(unvoiced)
            b = random.choice(unvoiced)
        if form[1] == 1:
            a = random.choice(sonorant)
        elif form[1] == 2:
            b = random.choice(sonorant)
        if a != b:
            break
    if first_upper:
        a = a.upper()
    return a + b

def rootword():
    vowels = list(u'aeiou')
    consonants = list(u'lmnrbdzvjgptsf\u0448k')
    form = random.randint(0, 1)
    s = u""
    if form:
        s = s + consonant_cluster(True)
        s = s + random.choice(vowels)
        s = s + random.choice(consonants)
        s = s + random.choice(vowels)
    else:
        s = s + random.choice(consonants).upper()
        s = s + random.choice(vowels)
        s = s + consonant_cluster(False)
        s = s + random.choice(vowels)
    return s

if __name__ == "__main__":
    seed = int(raw_input("Seed? "))
    random.seed(seed)
    print rootword()
