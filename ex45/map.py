from main import *
from lobby import *
from nurses import *
from cr import *
from doctors import *
from elevator import *
from exit import *
from caught import *

class Map(object):
    scene = {
        'your room': Main(),
        'lobby': Lobby(),
        'cr': Comfort_Room(),
        'doctors': Doctors_Office(),
        'nurses': Nurses_Room(),
        'elevator': Elevator(),
        'exit': Exit(),
        'caught': Caught()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene # assigning 'your room' to the constructor

    # gets the class from the scene lists
    def select_scene(self, scene_name):
        start = Map.scene.get(scene_name)
        return start

    # getting the 'Main()' class by using the constructor
    def first_scene(self):
        return self.select_scene(self.start_scene)
