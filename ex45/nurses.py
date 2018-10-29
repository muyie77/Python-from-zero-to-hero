from textwrap import dedent

class Nurses_Room(object):

    key = None
    uniform = 0

    def enter(self):
        print(dedent('''
                You entered the nurses room and hid behind the cabinet.
                You saw a nurse's uniform on the floor. "Oh! Maybe this
                fits me. But I can't find an ID here to access the
                elavator. Maybe I can get one at the doctor's office."
                You picked it up and headed to the lobby.
                '''))
        Nurses_Room.uniform += 1
        Nurses_Room.key = 'lobby'
