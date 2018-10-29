from textwrap import dedent
from doctors import *

class Elevator(object):

    key = None

    def enter(self):
        if Doctors_Office.id == 0: # Used directly the other class' variable because of an error
            print(dedent('''
                    "This is staff's elavator. I can't use this yet. I need
                    to have staff's ID first."
                    '''))
            Elevator.key = 'lobby'
        else:
            print(dedent('''
                    "Yohoo! Down we go! Let me put this ID inside my pocket.
                    Someone might see it."'''))
            Elevator.key = 'exit'
