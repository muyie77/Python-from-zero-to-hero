from map import *

class Engine(object):
    def __init__(self, room):
        self.room = room

    def play(self):
        current_scene = self.room.first_scene() # has the value 'Main()' class

        while last_scene.won == 0:
            current_scene.enter() # executing the class method 'enter()'
            next_scene_name = current_scene.key # every scene has a variable 'key' with a scene keyword in it
            current_scene = self.room.select_scene(next_scene_name) # getting the class by its keyword

game_map = Map('your room')
game_play = Engine(game_map)
game_play.play()
