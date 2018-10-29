from textwrap import dedent
from random import randint
import os

class Caught(object):

    quips = [
        "Nice one! Being sarcastic is always fun.",
        "Good job! I can't get out of this hospital forever. Psycho!",
        "Can't you do any better?",
        "Thank you very much for imprisoning me here forever. Psycho!",
    ]

    def enter(self):
        print(Caught.quips[randint(1,4)-1])
        exit(0)
