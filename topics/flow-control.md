# Contents
1. [**Flow control**](#flow-control)
    1. [Conditional statements](#conditional-statements)
    1. [Functions](#functions)

# Flow control
Today we will use **conditional statements** and **functions**
to write a recursive story with an element of chance.
Open the container here
https://mybinder.org/v2/gh/baharmon/digital-culture-seminar/master,
then open today's Jupyter notebook `flow-control.ipynb`
and follow the directions here or there to start programming!
Or you can write your own Python script
in an integrated development environment (IDE) like Spyder
using [flow-control.py](/scripts/flow-control.py) as a guide.

## Conditional statements
Let's start by writing a the opening lines of our story.
We will assign a random gender and a random name
for our hero or heroine
from a list of genders and a list of names.


```python
# import libraries
import random
random.seed()

# assign variables
names = ["Cloudy", "Echo", "Action"]
name = random.choice(names)
pronouns = ["he", "she"]
pronoun = random.choice(pronouns)

# print the opening lines of the story
print "One summer evening over cold beer and roasted peanuts \
my young friend {name} told me story. \
{pronoun} had gone to a fortune teller in the old town, \
paid with a fistful of crumpled old bills, \
and was handed a single die.\
".format(name=name, pronoun=pronoun.capitalize())
```

Okay, now let's write an **IF THEN** statement.
First we use the **randomint** function to generate
random integer between 1 and 6 to simulate the roll of a dice.


Now set different conditions for the results of the dice roll.
Check **IF** the dice roll was 1, then write a bad ending to the story.
Check **ELSE IF** the dice roll was 6, then write a good ending.
Check **ELSE IF** the dice roll was less than or equal to three
and the hero's name was Action, then print an ending to the story
Check **ELSE**, then continue the story...

```python
# simulate the roll of a dice
roll = random.randint(1,6)
print "{name} shook the die \
and rolled a {roll}.".format(name=name, roll=roll)

# if the dice roll was one then print a bad ending to the story
if roll == 1:
    print "The fortune teller wrinkled her nose \
and stared into {name}'s eyes. \
You will marry a flight attendant \
and live happily, until you discover \
that your partner has also married a pilot \
in a distant city.".format(roll=roll, name=name)
# else if the dice roll was six then print a good ending to the story
elif roll == 6:
    print "The fortune teller gasped. \
You will live long and make lots of money. \
Now fork over some cash.".format(roll=roll)
# else if both conditions are true then print an ending to the story
elif roll <= 3 and name == "Action":
    print "The fortune teller told me that to have good luck \
I should be true to my inner nature, \
so I choose the name {name} \
to always remind myself to seize the moment!".format(name=name)
# else continue the story
else:
    print "The fortune teller scraped the die off the table with \
a shake of the head, handed over scrap of red paper with a charm \
drawn in ink and told my young friend to come back in a years time \
when luck changed. And so {pronoun} did. \
The next year...".format(roll=roll, pronoun=pronoun)
```

## Functions
To continue the story we will write a function
that will repeat the same story with different luck!
This will make the story recursive -
it will repeat itself with variations.

First let's write a function for rolling the dice.
We already wrote the code to roll the dice.
Now we will wrap it in a function
so that we can easily reuse that code.

```python
def dice_roll(name):
    """Simulate the roll of a dice"""
    roll = random.randint(1,6)
    print "{indent}{name} shook the die \
and rolled a {roll}.".format(indent=indent, name=name, roll=roll)
    return roll
```

Now try the function!

```python
roll = dice_roll(name)
print roll
```

To tell a recursive story, you will repeat the same story
within the story (but with different luck).
So wrap all of the conditional statements in a function.
To start tell this part of the story run the `fortune()` function.
You can nest this function recursively within itself.
For example in the final **ELSE** statement,
add the `fortune()` function again.

```python
# import libraries
import random
random.seed()

# assign variables
names = ["Cloudy", "Echo", "Action"]
name = random.choice(names)
pronouns = ["he", "she"]
pronoun = random.choice(pronouns)

# print the opening lines of the story
print "One summer evening over cold beer and roasted peanuts \
my young friend {name} told me story. \
{pronoun} had gone to a fortune teller in the old town, \
paid with a fistful of crumpled old bills, \
and was handed a single die.\
".format(name=name, pronoun=pronoun.capitalize())

def dice_roll(name):
    """Simulate the roll of a dice"""
    roll = random.randint(1,6)
    print "{name} shook the die \
and rolled a {roll}.".format(name=name, roll=roll)
    return roll

def fortune(name, pronoun):
    """A recursive story in which a fortune is told"""
    print ""
    roll = dice_roll(name)
    # if the dice roll was one then print a bad ending to the story
    if roll == 1:
        print "The fortune teller wrinkled her nose \
and stared into {name}'s eyes. \
You will marry a flight attendant \
and live happily, until you discover \
that your partner has also married a pilot \
in a distant city.".format(roll=roll, name=name)
    # else if the dice roll was six then print a good ending to the story
    elif roll == 6:
        print "The fortune teller gasped. \
You will live long and make lots of money. \
Now fork over some cash.".format(roll=roll)
#    elif all([roll <= 3, name == "Action"]):
    # else if both conditions are true then print an ending to the story
    elif roll <= 3 and name == "Action":
        print "The fortune teller told me that to have good luck \
I should be true to my inner nature, \
so I choose the name {name} \
to always remind myself to seize the moment!".format(name=name)
    # else continue the story
    else:
        print "The fortune teller scraped the die off the table with \
a shake of the head, handed over scrap of red paper with a charm \
drawn in ink and told my young friend to come back in a years time \
when luck changed. And so {pronoun} did. \
The next year...".format(roll=roll, pronoun=pronoun)
        fortune(name, pronoun)

fortune(name, pronoun)
```
