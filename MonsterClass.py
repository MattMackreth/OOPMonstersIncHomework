# Here I will create and abstract my monster class
#       Add the attributes in the __init__ method
#       Add behaviours as individual methods


class Monster:
    def __init__(self, mon_name=""):
        self.name = mon_name
        self.skills = []

    def sleep(self):
        return "ZZZzzzz..."

    def eat(self):
        return 'nom nom'

    def scare_attack(self):
        return 'RAAAHHH'

    def add_skill(self, skill):
        self.skills.append(skill)
        return self.skills

    def get_skills(self):
        return self.skills
