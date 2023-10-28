from adventurelib import *
from csv import *  #import all data from csv file in future

class Place(Room):
    context=''

class Space(Room):
    def __init__(self,description,aliases):
        super().__init__(description)
        self.aliases=aliases   #fix for adding room to a bag.

class Kingdom(Room):
    def __init__(self,description,aliases):
        super().__init__(description)
        self.aliases=aliases   #fix for adding room to a bag.
        self.king=None
        self.citys=Bag()

class City(Room):
    def __init__(self,description,aliases):
        super().__init__(description)
        self.aliases=aliases   #fix for adding room to a bag.
        self.mayor=None
        self.population=-1


Space_Unknown=Space('This is a huge space we know nothing about and no one had been there ever. Too far even your mind cant reach.','Unknown')
Space_Sprit=Space('This is the up to 9-dimentions space where sprites live. Sprits will move the higher dimention world by unknown creteria. There rumor says, sprits can be merged.', 'Sprit Space')
Space_Sea=Space('The beautiful sea, you know. In the middle of land. Only can be accessed by four land ports.','The Sea')
Space_Land=Space('This is where humen and cretures live. Humen rule this space and splited into 7 kingdoms. Wars or peace?','The Land')
Space_UnderGround=Space('Night creatures live under-ground. Most of them are blind and afaid of light. Eager for fresh meat all the time...','The Underground')
Space_GhostSpace=Space('Space up to 2-dimention full ghosts. What kind a place it is!','Ghost Space')
#Universe=Bag([Space_Unknown,Space_Sprit,Space_Sea,Space_Land,Space_UnderGround,Space_GhostSpace])

Kingdom_North=Kingdom('The most wide kingdowm of the seven. Cold. People are very nice and they like to elect someone looks pretty but know nothing as their King.','North Kingdom')
Kingdom_North.king='Treadou'



Ottawa=City('Capital of North Kindom. Two seasons in a year, winter and nwinter. Stay at home and sleeping all the day during winter.','Ottawa')
Ottawa.mayor='Emily'
Ottawa.population=1250000

Kingdom_North.citys.add(Ottawa)