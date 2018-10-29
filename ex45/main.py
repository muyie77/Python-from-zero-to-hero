from textwrap import dedent

class Main(object):

    key = None

    def enter(self):
        print(dedent("""
                You are a patient (Psychopath) on a hospital. You don't want to be
                treated and you want to get out the hospital as soon as possible.

                To get out the hospital you need to disguise as a hospital staff
                and use the staff's elavator.
                """))
        print("Go to the lobby? y/n")

        while True:
            choice = input("> ")

            if choice == 'Y' or choice == 'y':
                Main.key = 'lobby'
                break
            elif choice == 'N' or choice == 'n':
                print("Okay, I'll just stay here.")
                Main.key = 'your room'
                break
            else:
                print("Can't you read the choices?")
