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
Generate short sentences based on text from  Mallarme's A Roll of the Dice.
"""
# get raw text as string
with open("../readings/mallarme-a-roll-of-the-dice.txt") as f:
    text = f.read()

# build the model
text_model = markovify.NewlineText(text) #text_model = markovify.Text(text)

# randomly generate a sentence of no more than 140 characters
poem = text_model.make_short_sentence(140)


# get raw text as string with the write (w) or append (a) option
with open("../poems/markov_poem.md", "w") as m:

    # write a header in markdown
    m.write("## A Roll of the Dice")

    # write a new line in markdown
    m.write("\n")

    # write the start of a code block in markdown
    m.write("```")

    # write a new line in markdown
    m.write("\n")

    # write the text generated from the markov model
    m.write(poem)

    # write a new line in markdown
    m.write("\n")

    # write the end of a code block in markdown
    m.write("```")

    # write a new line in markdown
    m.write("\n")

    code_block = """
## Python Code
```python
# get raw text as string /n
with open("../readings/mallarme-a-roll-of-the-dice.txt") as f:
    text = f.read()

# build the model
text_model = markovify.NewlineText(text) #text_model = markovify.Text(text)

# randomly generate a sentence of no more than 140 characters
poem = text_model.make_short_sentence(140)
```
"""

    # write the python code to generate this text in markdown
    m.write(code_block)

"""
preview your markdown document by dragging and dropping it into either
https://jbt.github.io/markdown-editor/
or
https://dillinger.io/
"""
