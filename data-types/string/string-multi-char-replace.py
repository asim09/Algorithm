# Replace all occurence of ['s','l', 'a'] with 'AA' in a string

def replacement(mainSring, toBeReplaced, newString):
    for elem in toBeReplaced:
        if elem in mainSring:
            mainSring = mainSring.replace(elem, newString)
    return mainSring

lol = 'String with replaced Content :  Hello, ThiX iX a Xample Xtring'
print(replacement(lol, ['s','l', 'a'], 'AA'))
