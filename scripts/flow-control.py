#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SCRIPT:    flow-control.py
AUTHOR(S): Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE:   Open educational materials for a seminar on digital culture
COPYRIGHT:  GNU General Public License v2. 
"""

# import libraries
import random

# set the random seed
random.seed()

# assign variables
i = 0
names = ["Cloudy", "Echo", "Action"]
name = random.choice(names)
pronouns = ["he", "she"]
pronoun = random.choice(pronouns)

# print line breaks
print ""
print ""
print ""

# print the opening lines of the story
print "One summer evening over cold beer and roasted peanuts \
my young friend {name} told me story. \
{pronoun} had gone to a fortune teller in the old town, \
paid with a fistful of crumpled old bills, \
and was handed a single die.\
".format(name=name, pronoun=pronoun.capitalize())

def whitespace(i):
    i = i + 1
    indent = "   " * i
    return i, indent

def dice_roll(i, name):
    """Simulate the roll of a dice"""
    roll = random.randint(1,6)
    i, indent = whitespace(i)
    print "{indent}{name} shook the die \
and rolled a {roll}.".format(indent=indent, name=name, roll=roll)
    return i, roll

def fortune(i, name, pronoun):
    """A recursive story in which a fortune is told"""
    print ""
    i, roll = dice_roll(i, name)
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
        fortune(i, name, pronoun)

fortune(i, name, pronoun)