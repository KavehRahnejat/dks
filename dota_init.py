from dota_models import *
from dota_items import *
from dota_calculator import *
import json

hero = AntiMage(25)
items = [UltimateOrb(), UltimateOrb(), UltimateOrb(), UltimateOrb(), UltimateOrb(), UltimateOrb(), UltimateOrb()]

x = find_dps(hero, items)
x.update(find_ehp(hero, items))

print json.dumps(x, indent=3)