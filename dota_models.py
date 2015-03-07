class BaseHero():
	crit_chance = 0
	crit_bonus = 0

	starting_agi = 0
	starting_stre = 0
	starting_inte = 0
	progression_agi = 0
	progression_stre = 0
	progression_inte = 0

	base_hp = 150
	base_ar = 0

	damage_percentage = 0
	base_damage = 0

	bat = 1.7

	__abstract = True

	def __init__(self, level=25):
		if getattr(self, '_' + self.__class__.__name__+ '__abstract', False) == True:
		# __abstract is a private variable so this will only be True for explicitly stated abstract classes and not the children
			raise Exception('%s is an abstract parent class and cannot be instantiated' % self.__class__.__name__)
		
		if not isinstance(level, int):
			self.level = 25
		else:
			self.level = max(0, min(level, 25))

		self.base_agi = self.starting_agi + self.level * self.progression_agi
		self.base_stre = self.starting_stre + self.level * self.progression_stre
		self.base_inte = self.starting_inte + self.level * self.progression_inte

		if self.level in [15, 16]:
			self.base_agi += 2
			self.base_stre += 2
			self.base_inte += 2

		elif self.level > 16:
			self.base_agi += (2 * self.level - 30)
			self.base_stre += (2 * self.level - 30)
			self.base_inte += (2 * self.level - 30)

class AgilityHero(BaseHero):
	primary_stat = 'agi'
	__abstract = True

class StrengthHero(BaseHero):
	primary_stat = 'stre'
	__abstract = True

class IntelligenceHero(BaseHero):
	primary_stat = 'inte'
	__abstract = True

class Slark(AgilityHero):
	starting_agi = 21
	starting_stre = 21
	starting_inte = 16
	progression_agi = 1.5
	progression_stre = 1.8
	progression_inte = 1.9

class AntiMage(AgilityHero):
	starting_agi = 22
	starting_stre = 22
	starting_inte = 15
	progression_agi = 2.8
	progression_stre = 1.2
	progression_inte = 1.8
	# mana burn

class Bloodseeker(AgilityHero):
	starting_agi = 24
	starting_stre = 23
	starting_inte = 18
	progression_agi = 3
	progression_stre = 2
	progression_inte = 1.7

class BountyHunter(AgilityHero):
	starting_agi = 21
	starting_stre = 17
	starting_inte = 19
	progression_agi = 3
	progression_stre = 1.8
	progression_inte = 1.4
	# jinada

class Broodmother(AgilityHero):
	starting_stre = 17
	progression_stre = 2.5
	starting_agi = 18
	progression_agi = 2.2
	starting_inte = 18
	progression_inte = 2

class Clinkz(AgilityHero):
	starting_stre = 15
	progression_stre = 1.6
	starting_agi = 22
	progression_agi = 3
	starting_inte = 16
	progression_inte = 1.55
	# fire arrows

class DrowRanger(AgilityHero):
	starting_stre = 17
	progression_stre = 1.9
	starting_agi = 26
	progression_agi = 1.9
	starting_inte = 15
	progression_inte = 1.4
	
	damage_percentage = 0.18

	def __init__(self, level=25):
		super(self, DrowRanger).__init__(level)
		if self.level > 6:
			self.base_agi += 40
		if self.level > 11:
			self.base_agi += 20
		if self.level > 15:
			self.base_agi += 20
		if self.level > 2:
			self.crit_chance += 0.06
		if self.level > 4:
			self.crit_chance += 0.06
		if self.level > 7:
			self.crit_chance += 0.06

class EmberSpirit(AgilityHero):
	starting_stre = 19
	progression_stre = 2
	starting_agi = 22
	progression_agi = 1.8
	starting_inte = 20
	progression_inte = 1.8

class FacelessVoid(AgilityHero):
	starting_stre = 23
	progression_stre = 1.6
	starting_agi = 23
	progression_agi = 2.65
	starting_inte = 15
	progression_inte = 1.5
	# time lock

class Gyrocopter(AgilityHero):
	starting_stre = 18
	progression_stre = 1.8
	starting_agi = 24
	progression_agi = 2.8
	starting_inte = 23
	progression_inte = 2.1

class Juggernaut(AgilityHero):
	starting_stre = 20
	progression_stre = 1.9
	starting_agi = 20
	progression_agi = 2.85
	starting_inte = 14
	progression_inte = 1.4

	crit_chance = 0.15
	crit_bonus = 1.0

	def __init__(self, level=25):
		super(self, Juggernaut).__init__(level)
		if self.level > 2:
			self.crit_chance += 0.05
		if self.level > 4:
			self.crit_chance += 0.05
		if self.level > 7:
			self.crit_chance += 0.05

class LoneDruid(AgilityHero):
	starting_stre = 17
	progression_stre = 2.1
	starting_agi = 24
	progression_agi = 2.7
	starting_inte = 13
	progression_inte = 1.4

class Luna(AgilityHero):
	starting_stre = 15
	progression_stre = 1.9
	starting_agi = 18
	progression_agi = 2.8
	starting_inte = 16
	progression_inte = 1.85

	base_damage = 14

	def __init__(self, level=25):
		super(self, Luna).__init__(level)
		if self.level > 2:
			self.base_damage += 8
		if self.level > 4:
			self.base_damage += 8
		if self.level > 7:
			self.base_damage += 8

class Medusa(AgilityHero):
	starting_stre = 15
	progression_stre = 1.65
	starting_agi = 20
	progression_agi = 2.5
	starting_inte = 19
	progression_inte = 1.85

class Meepo(AgilityHero):
	starting_stre = 23
	progression_stre = 1.6
	starting_agi = 23
	progression_agi = 1.9
	starting_inte = 20
	progression_inte = 1.6

	base_damage = 14

	def __init__(self, level=25):
		super(self, DrowRanger).__init__(level)
		if self.level > 2:
			self.base_damage += 14
		if self.level > 4:
			self.base_damage += 14
		if self.level > 7:
			self.base_damage += 14

class Mirana(AgilityHero):
	starting_stre = 17
	progression_stre = 1.85
	starting_agi = 20
	progression_agi = 2.75
	starting_inte = 17
	progression_inte = 1.65

class Morphling(AgilityHero):
	starting_stre = 19
	progression_stre = 2
	starting_agi = 24
	progression_agi = 3
	starting_inte = 17
	progression_inte = 1.5
	# morph

class NagaSiren(AgilityHero):
	starting_stre = 21
	progression_stre = 2.3
	starting_agi = 21
	progression_agi = 2.75
	starting_inte = 18
	progression_inte = 1.95