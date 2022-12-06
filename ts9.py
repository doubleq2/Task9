from ts8_1 import baselist2
from models import *

with db:
    Drivers.insert_many(baselist2).execute()
print("DONE")