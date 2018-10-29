from textwrap import dedent
from cr import *

class Doctors_Office(object):

    key = None
    id = 0

    def enter(self):
        if Comfort_Room.ready == 0: # Used directly the other class' variable because of an error
            print(dedent('''
                    "Hey! What are you doing here?!? Shouldn't you be on
                    your room resting?"said the doctor as he saw you enter
                    the office. The doctor called a nurse and escort you to
                    your room.
            '''))
            Doctors_Office.key = 'caught'
        else:
            print(dedent('''
                    You talked to the doctor for a while. The doctor's ID is on
                    the table. You picked it up and the doctor didn't notice it.
                    "Hey doc, I have to go. I have patient to take care of."
                    '''))
            Doctors_Office.id = 1
            Doctors_Office.key = 'lobby'
