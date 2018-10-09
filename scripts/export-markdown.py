#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SCRIPT:    export-markdown.py
AUTHOR(S): Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE:   Open educational materials for a seminar on digital culture
COPYRIGHT:  GNU General Public License v2. 
"""

# import libraries
import markovify 

"""
Combine text from Lovecraft's Dunwich Horror and Petronius' Satyricon
"""
# get raw text as string
with open("../readings/lovecraft-dunwich-horror.txt") as l:
    lovecraft = l.read()

with open("../readings/satyricon.txt") as s:
    satyricon = s.read()

# build and combine the models
lovecraft_model = markovify.Text(lovecraft)
satyricon_model = markovify.Text(satyricon)
model_synthesis = markovify.combine([lovecraft_model, satyricon_model], 
    [ 1.5, 1 ])

# generate a sentence from the markov model
markov_text = model_synthesis.make_sentence()
  
# get raw text as string with the write (w) or append (a) option
with open("../poems/poem.md", "w") as m:

    # write a header in markdown
    m.write("## The Dunwich Satyricon")

    # write a new line in markdown
    m.write("\n")

    # write the start of a code block in markdown
    m.write("```")

    # write a new line in markdown
    m.write("\n")

    # write the text generated from the markov model
    m.write(markov_text)

    # write a new line in markdown
    m.write("\n")

    # write the end of a code block in markdown
    m.write("```")

"""
preview your markdown document by dragging and dropping it into either
https://jbt.github.io/markdown-editor/
or
https://dillinger.io/
"""