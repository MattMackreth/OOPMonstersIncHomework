# Here I will create and abstract my workshop class
#       Add the attributes in the __init__ method
#       Add behaviours as individual methods
from MonsterClass import *

class Workshop:
    def __init__(self, workshop_name):
        self.name = workshop_name
        self.monster_attendees_list = []
        self.teacher = Monster()

    def set_teacher(self, teacher_input):
        self.teacher = teacher_input

    def get_attendees(self):

        return self.monster_attendees_list

    def add_attendee(self, new_attendee):
        self.monster_attendees_list.append(new_attendee.name)
