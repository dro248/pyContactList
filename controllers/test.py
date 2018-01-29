import sys

# Add parent directory to the path in order to import models
sys.path.append("..")

from models.Person import Person

p = Person()
p.save(None, None, None, None,None, None)
p.delete()
