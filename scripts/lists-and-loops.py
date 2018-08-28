#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SCRIPT:    lists-and-loops.py
AUTHOR(S): Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE:   Open educational materials for a seminar on digital culture
COPYRIGHT:  GNU General Public License v2. 
"""

import random

# set the random seed
random.seed()

# line break
print ""

# lists of words
nouns = ["emjoi", "unicorn", "sloth", "robot", "alien", "lolcat", "python", "bug", "flying saucer", "moon", "sorcerors apprentice"]
verbs = ["laughed out loud", "rolled on the floor laughing", "slept", "read", "declaimed", "roared", "glittered"]
adjectives = ["giant", "raucous", "playful", "sparkling", "sleepy", "scornful", "arrogant", "stealthy", "mechanical", "magical", "ancient"]
adverbs = ["loudly", "silently", "playfully", "sneakily", "proudly", "tearfully", "mindfully", "boldly", "gently", "disdainfully", "daintily", "patiently"]

# select random words from lists
noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
adverb = random.choice(adverbs)

# print a sentence with random words from the lists
print "The {adjective} {noun} {adverb} {verb}.".format(adjective=adjective, noun=noun, adverb=adverb, verb=verb)

# line break
print ""

# shuffle the list of adjectives
random.shuffle(adjectives)

# print the shuffled list of adjectives with increasing whitespace
i = 0
print "The "
for adjective in adjectives:
    i = i + 1
    whitespace = " " * i
    print whitespace + adjective
    
# print the rest of the sentence
print "{noun} {verb}.".format(noun=noun, verb=verb)

