from app.api.models.Client import Client, Country
from app.api.db import Session, Base, engine

#destroy it all..
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)



db = Session()

#----------------------------
#---- Generate some countries
#----------------------------

# Get countries
import json
with open("app/api/assets/countries.json") as f:
    countries_dict = json.load(f)


#print(countries_dict)

# seed the db

for c in countries_dict:
    #print(c.keys())
    db.add(Country(name = c["name"], name_2letter = c["alpha-2"], name_3letter = c["alpha-3"], region = c["region"]))
    db.commit()
db.close()





#--------------------------------
#---- Generate random client data
#--------------------------------

import random

n = 20

prefixes=('Equity','Shale','Dirty','Greedy','Polluting', 'Money')
postfixes=('Energy','Power','Oil','GAS','Benzin','Petroleum','Fuel','JetFuel')



names = []
for x in range(n):
    fullname = random.choice(prefixes)+" "+random.choice(postfixes)
    country = random.randint(1,len(countries_dict))
    address = "NA Temp" 
    db.add_all(
        [Client(name=fullname,country = country, address = address)]
    )
    db.commit()

db.close()       


