# Contents
1. [**Lists and loops**](#lists-and-loops)
    1. [Lists](#lists)
    1. [Loops](#loops)
    1. [Towards a poem](#towards-a-poem)

# List and Loops
Today we will use **print statements**, **variables**,
**randomness**, **lists**, and **loops**
to write simple sentences.
Open the container here
https://mybinder.org/v2/gh/baharmon/digital-culture-seminar/master,
then open today's Jupyter notebook `lists-and-loops.ipynb`,
and follow the directions here or there to start programming!

## Lists
First we will write a list of nouns,
a list of verbs, a list of adjectives, and a list of adverbs.
Then we will use a random selection of these words to
computationally compose a sentence.

```python
import random

# set the random seed
random.seed()

# lists of words
nouns = ["emjoi",
    "unicorn",
    "sloth",
    "robot",
    "alien",
    "lolcat",
    "python",
    "bug",
    "flying saucer",
    "moon",
    "sorcerors apprentice"]
verbs = ["laughed out loud",
    "rolled on the floor laughing",
    "slept",
    "read",
    "declaimed",
    "roared",
    "glittered"]
adjectives = ["giant",
    "raucous",
    "playful",
    "sparkling",
    "sleepy",
    "scornful",
    "arrogant",
    "stealthy",
    "mechanical",
    "magical",
    "ancient"]
adverbs = ["loudly",
    "silently",
    "playfully",
    "sneakily",
    "proudly",
    "tearfully",
    "mindfully",
    "boldly",
    "gently",
    "disdainfully",
    "daintily",
    "patiently"]

# select random words from lists
noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)
adverb = random.choice(adverbs)

# print a sentence with random words from the lists
print "The {adjective} {noun} {adverb} {verb}.".format(adjective=adjective,
    noun=noun, adverb=adverb, verb=verb)
```

## Loops
First we will randomly shuffle our adjectives.
Then we will loop through the list of adjectives,
printing each on a new line.
Each new line will be preceded by an extra space
to create an interesting structure of whitespace.
Then we will finish the sentence
with a random selection of a noun and verb.

```python
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
```

## Towards a poem
Now create your own, more poetic lists and sentence structure
to write a generative poem!
Diction, syntax, sentence structure, and whitespace
are the basic building blocks of poetry.
