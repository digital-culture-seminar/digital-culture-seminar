#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SCRIPT:    markov-chains.py
AUTHOR(S): Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE:   Open educational materials for a seminar on digital culture
COPYRIGHT:  GNU General Public License v2. 
"""

# import libraries
import markovify 

"""
Generate text from Mallarme's A Roll of the Dice
"""
# get raw text as string
with open("../readings/mallarme-a-roll-of-the-dice.txt") as f:
    text = f.read()

# build the model
text_model = markovify.NewlineText(text) #text_model = markovify.Text(text)

# print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print text_model.make_short_sentence(140)

"""
Generate text from Lovecraft's Dunwich Horror
"""
# get raw text as string
with open("../readings/lovecraft-dunwich-horror.txt") as f:
    text = f.read()

# build the model
text_model = markovify.Text(text)

# print five randomly-generated sentences
for i in range(5):
    print text_model.make_sentence()

"""
Generate text from Petronius' Satyricon
"""
# get raw text as string
with open("../readings/satyricon.txt") as f:
    text = f.read()

# build the model
text_model = markovify.Text(text)

# print five randomly-generated sentences
for i in range(5):
    print text_model.make_sentence()

"""
Combine text from Lovecraft's Dunwich Horror and Petronius' Satyricon
"""
# get raw text as string
with open("../readings/lovecraft-dunwich-horror.txt") as f:
    lovecraft = f.read()

with open("../readings/satyricon.txt") as f:
    satyricon = f.read()

# build and combine the models
lovecraft_model = markovify.Text(lovecraft)
satyricon_model = markovify.Text(satyricon)
model_synthesis = markovify.combine([lovecraft_model, satyricon_model], 
    [ 1.5, 1 ])

# print five randomly-generated sentences
for i in range(5):
    print model_synthesis.make_sentence()