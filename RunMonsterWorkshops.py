# Run all the code in this file
# import needed classes
from WorkshopClass import *


# Create some workshops
Scare = Workshop('Scare 101')
Magic = Workshop('Magic for beginners')
Maths = Workshop('Advanced Mathematics')

# Create some monsters
Sully = Monster('Sully')
Mike = Monster('Mike')
Patricia = Monster('Patricia')
Patch = Monster('Patch')

# Adding Monsters to workshops
Scare.set_teacher(Sully)
Scare.add_attendee(Patch)
Scare.add_attendee(Mike)

print(Scare.name, Scare.get_teacher().name, Scare.get_attendees_names())

Maths.set_teacher(Patricia)
Maths.add_attendee(Patch)
Maths.add_attendee(Sully)
print(Maths.name, Maths.get_teacher().name, Maths.get_attendees_names())

# Make monsters do some stuff
print(Sully.name, Sully.sleep(), Sully.eat(), Sully.scare_attack())
Sully.add_skill('Cooking')
Sully.add_skill('Comedy')
Sully.add_skill('Scaring')
print(Sully.get_skills())
