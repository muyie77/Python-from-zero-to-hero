from textwrap import dedent
from nurses import *

class Lobby(object):

    key = None

    def enter(self):
        print(dedent("""
                You walked into the lobby. There's a lot of people here.
                There's four doors here.

                Which do you choose?
                """))
        print(dedent("""
                1. Doctors office
                2. Comfort room
                3. Nurses room
                4. Elavator
                """))
        while True:
            choice = input("> ")

            if choice == '1':
                print("Maybe I'll find something here.")
                Lobby.key = 'doctors'
                break

            elif choice == '2':
                Lobby.key = 'cr'
                break

            elif choice == '3':
                print(dedent('''
                        "That's a good idea. Maybe I can find a uniform here for
                        disguise"
                        '''))
                Lobby.key = 'nurses'
                break

            elif choice == '4':
                print("Let me try this.")
                Lobby.key = 'elevator'
                break

            else:
                print("Can't you read the choices?")
