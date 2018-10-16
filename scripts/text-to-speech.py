#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SCRIPT:  text-to-audio.py
AUTHOR:  Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE: Open educational materials for a seminar on digital culture
LICENSE: GNU General Public License v2
DEPENDENCIES: playsound and gTTs
"""

# import libraries
from playsound import playsound
from gtts import gTTS
tts = gTTS(text='Hello world', lang='en')
tts.save("hello-world.mp3")
playsound('hello-world.mp3')
