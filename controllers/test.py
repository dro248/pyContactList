import sys

# Add parent directory to the path in order to import models
sys.path.append("..")

from models.Person import Person

print("start")
p = Person()
# p.create( {username}, {password}, {full name}, {email} )
p.create("hpotter", "magic123", "POTTER, Harry", "the.boy@lived.com")
print("finished")

