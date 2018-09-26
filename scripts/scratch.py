# import libraries
import random
random.seed()

# assign variables
names = ["Cloudy", "Echo", "Action"]
name = random.choice(names)
pronouns = ["he", "she"]
pronoun = random.choice(pronouns)

roll = random.randint(1,6)
print "{name} rolled a {roll}".format(name=name, roll=roll)

if roll == 1:
    print "Bad luck!"

elif roll == 6 or name == "Action":
    print "Good luck!"

else:
    print "Not so bad luck..."
