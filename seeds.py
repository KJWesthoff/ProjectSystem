from app.api.models import Client
from app.api.db import Session, Base, engine

#destroy it all..
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


#-------------------------
#---- Generate random data
#-------------------------

import random

n = 20

prefixes=('Equity','Shale','Dirty','Greedy','Polluting', 'Money')
postfixes=('Energy','Power','Oil','GAS','Benzin','Petroleum','Fuel','JetFuel')
names = []
for x in range(n):
    fullname = random.choice(prefixes)+" "+random.choice(postfixes)
    names.append(fullname)
    
print(names)



db = Session()




# insert  clients
#db.add_all(
#    Client()
#)