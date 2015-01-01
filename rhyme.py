#!/usr/bin/env python

import random
from itertools import izip as zip, count

PHONES = ['AA0', 'AA1', 'AA2', 'AE0', 'AE1', 'AE2', 'AH0', 'AH1', 'AH2', 'AO0', 'AO1', 'AO2', 'AW0', 'AW1', 'AW2', 'AY0', 'AY1', 'AY2', 'EH0', 'EH1', 'EH2', 'ER0', 'ER1', 'ER2', 'EY0', 'EY1', 'EY2', 'IH0', 'IH1', 'IH2', 'IY0', 'IY1', 'IY2', 'OW0', 'OW1', 'OW2', 'OY0', 'OY1', 'OY2', 'UH0', 'UH1', 'UH2', 'UW0', 'UW1', 'UW2']

STRESSED = ['AA1', 'AA2', 'AE1', 'AE2', 'AH1', 'AH2', 'AO1', 'AO2', 'AW1', 'AW2', 'AY1', 'AY2',  'EH1', 'EH2', 'ER1', 'ER2', 'EY1', 'EY2', 'IH1', 'IH2', 'IY1', 'IY2', 'OW1', 'OW2', 'OY1', 'OY2', 'UH1', 'UH2', 'UW1', 'UW2']

with open("./cmudict_nocred.txt","r") as f:
    cmu = f.readlines() 

def rhyme():
    seed = raw_input('Seed Word: ').upper()
    seed_entry = [entry for entry in cmu if seed == entry.split()[0]]
    # ^ returns a list with one value
    try:
        seed_entry = seed_entry[0]
    except IndexError:
        print "I encountered a problem with " + seed
        print "I do not know how to pronounce this, and therefore cannot find a rhyme"
        
    # ^ sets seed_entry as a string instead of single item list
    e = seed_entry.split()
    # ^ splits phonemes into a list where [0] is the seed word
    stressed_vowel_positions = [i for i, j in zip(count(), e) if j in STRESSED]
    # ^ list comp that finds the index for each stressed vowel phoneme
    try:
        last_stressed_vowel = stressed_vowel_positions[-1]
    except IndexError:
        last_stressed_vowel = 0
    # ^ determines the index of the last stressed vowel
    # ^ exception for words with no stressed vowels (such as 'A', pronounced 'AH0')
    backward_count_vowel = len(e) - last_stressed_vowel
    # ^ determines the index from the right instead of left so 'greater syllabic'?! words are counted
    candidates = [entry.split()[0] for entry in cmu if entry.split()[-backward_count_vowel:] == e[-backward_count_vowel:]]
    # ^ list comp that matches words that share identical phonemes from the last stressed vowel
    # ^ i.e. it finds true rhymes!
    print candidates

rhyme() 
