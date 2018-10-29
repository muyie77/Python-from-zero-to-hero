from textwrap import dedent
import os

class Exit(object):

    key = None
    won = 0

    def enter(self):
        print(dedent('''
                You are walking on the ground floor when the guard whistles at
                you. "Prrrrrt! Who are you? I know all the nurses here, and
                you don't look familiar. May I see your ID?"

                What will you do?
                1. Show the ID that is on your pocket
                2. Reason out
                3. Run off
                '''))

        action = input("> ")
        while True:
            if action == '1':
                print(dedent('''
                        "This isn't your ID! Your a nurse and this is a doctor's ID"
                        I'm right! Your not a staff here.'''))
                Exit.key = 'caught'
                break
            elif action == '2':
                print(dedent('''
                        "Okay."
                        You look for your wallet and...
                        "My ID is missing. Maybe I dropped it somewhere. Could you
                        help me?"
                        The guard walks into the elevator. You run off and exited
                        the hospital

                        You Won! Congratulations!'''))
                Exit.won = 1
                exit(0)
            elif action == '3':
                print(dedent('''
                        You run off quickly. The guard did not catch up.
                        While your running, you slipped of your foot and your head
                        hit the wall so bad. The guard called some nurse and take
                        you back to your room.'''))
                Exit.key = 'caught'
                break
            else:
                print("Can't you read the choices?")
