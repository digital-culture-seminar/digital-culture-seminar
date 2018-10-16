#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SCRIPT:  markovify-to-speech.py
AUTHOR:  Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE: Open educational materials for a seminar on digital culture
LICENSE: GNU General Public License v2
DEPENDENCIES: markovify, playsound, and gTTs
"""

# import libraries
from playsound import playsound
from gtts import gTTS
import markovify

# get raw text as string
with open("../readings/mallarme-a-roll-of-the-dice.txt") as f:
    text = f.read()

# build the markov model
text_model = markovify.NewlineText(text)

# print a randomly-generated sentence of no more than 140 characters
markov_poem = text_model.make_short_sentence(140)

# text to speech
tts = gTTS(text=markov_poem, lang='en')

# write audio file
tts.save("../poems/markovified-poem.mp3")

# play audio file
playsound("../poems/markovified-poem.mp3")
