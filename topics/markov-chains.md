# Contents
1. [**Markov chains**](#markov-chains)
    1. [Generate short sentences from a poem](#generate-short-sentences-from-a-poem)
    2. [Generate sentences from a book](#generate-sentences-from-a-book)
    3. [Combining texts](#combining-texts)
    4. [Other texts](#other-texts)

# Markov chains
Install [Markovify](https://github.com/jsvine/markovify).
Start your script by importing the markovify library.

```python
# import libraries
import markovify
```

## Generate short sentences from a poem
Generate short sentences based on text from  Mallarme's A Roll of the Dice.

```python
# get raw text as string
with open("../readings/mallarme-a-roll-of-the-dice.txt") as f:
    text = f.read()

# build the model
text_model = markovify.NewlineText(text) #text_model = markovify.Text(text)

# print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print text_model.make_short_sentence(140)
```

## Generate sentences from a book
Generate text from Lovecraft's
[Dunwich Horror](https://www.gutenberg.org/ebooks/50133).

```python
# get raw text as string
with open("../readings/lovecraft-dunwich-horror.txt") as f:
    text = f.read()

# build the model
text_model = markovify.Text(text)

# print five randomly-generated sentences
for i in range(5):
    print text_model.make_sentence()
```

## Combining texts
Combine text from
Lovecraft's [Dunwich Horror](https://www.gutenberg.org/ebooks/50133)
and Petronius' [Satyricon](http://www.gutenberg.org/ebooks/5225).

```python
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
```

## Other texts
Download other Public Domain texts from the [Gutenberg Project](https://www.gutenberg.org/)
and experiment!
