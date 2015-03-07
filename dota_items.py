class BaseItem():
	agi = 0
	stre = 0
	inte = 0

	ias = 0

	crit_chance = 0
	crit_bonus = 0

	damage_percentage = 0
	base_damage = 0

	hp = 0
	ar = 0

	__abstract = True

	def __init__(self):
		if getattr(self, '_' + self.__class__.__name__+ '__abstract', False) == True:
		# __abstract is a private variable so this will only be True for explicitly stated abstract classes and not the children
			raise Exception('%s is an abstract parent class and cannot be instantiated' % self.__class__.__name__)

class BladeOfAlacrity(BaseItem):
	agi = 10

class OgreClub(BaseItem):
	stre = 10

class StaffOfWizardry(BaseItem):
	inte = 10

class UltimateOrb(BaseItem):
	agi = 10
	stre = 10
	inte = 10

class RobeOfTheMagi(BaseItem):
	inte = 6

class BandOfElvenskin(BaseItem):
	agi = 6

class BeltOfStrength(BaseItem):
	stre = 6