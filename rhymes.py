#!/usr/bin/env python

import random
from itertools import izip as zip, count

PHONES = ['AA0', 'AA1', 'AA2', 'AE0', 'AE1', 'AE2', 'AH0', 'AH1', 'AH2', 'AO0', 'AO1', 'AO2', 'AW0', 'AW1', 'AW2', 'AY0', 'AY1', 'AY2', 'EH0', 'EH1', 'EH2', 'ER0', 'ER1', 'ER2', 'EY0', 'EY1', 'EY2', 'IH0', 'IH1', 'IH2', 'IY0', 'IY1', 'IY2', 'OW0', 'OW1', 'OW2', 'OY0', 'OY1', 'OY2', 'UH0', 'UH1', 'UH2', 'UW0', 'UW1', 'UW2']

STRESSED = ['AA1', 'AA2', 'AE1', 'AE2', 'AH1', 'AH2', 'AO1', 'AO2', 'AW1', 'AW2', 'AY1', 'AY2',  'EH1', 'EH2', 'ER1', 'ER2', 'EY1', 'EY2', 'IH1', 'IH2', 'IY1', 'IY2', 'OW1', 'OW2', 'OY1', 'OY2', 'UH1', 'UH2', 'UW1', 'UW2']

with open("./cmudict_nocred.txt","r") as f:
    cmu = f.readlines() 

def ret_rhyme(seed):
    seed_entry = [entry for entry in cmu if seed == entry.split()[0]] #returns a list with one value
    seed_entry = seed_entry[0]
    e = seed_entry.split()
    svp = [i for i, j in zip(count(), e) if j in STRESSED]
    try:
        lsv = svp[-1]
    except IndexError:
        lsv = 0
    bcv = len(e) - lsv
    candidates = [entry.split()[0] for entry in cmu if entry.split()[-bcv:] == e[-bcv:]]
    return random.choice(candidates)

def rhymes():
    phrase = raw_input("Write phrase: ")
    nonsense = []
    phrase_split = phrase.upper().split()
    for word in phrase_split:
        nonsense.append(ret_rhyme(word))
    for word in nonsense:
        print word.lower(),
    print
    
rhymes()   
