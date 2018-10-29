from textwrap import dedent
from nurses import *

class Comfort_Room(object):

    key = None
    ready = 0

    def enter(self):
        if Nurses_Room.uniform == 0: # Used directly the other class' variable because of an error
            print(dedent('''
                    "Uggggh, stinky!!! Do you think I have time peeing and
                    pooping? Disgusting!"
                    '''))
            Comfort_Room.key = 'lobby'
        else:
            print(dedent('''
                "I'll just wear this nurse uniform here."
                Wearing...
                "Now I'm ready to go to the Doctors office."
                '''))
            Comfort_Room.ready += 1
            Comfort_Room.key = 'lobby'
