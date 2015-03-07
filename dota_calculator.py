def find_dps(hero, items):
	# things to add: bash, mkb?
	crit_influence = 1.0 + (hero.crit_chance * hero.crit_bonus)
	floating_crit = hero.crit_chance

	base_damage = hero.base_damage
	damage_percentage = 1.0 + hero.damage_percentage

	agi = hero.base_agi
	stre = hero.base_stre
	inte = hero.base_inte
	ias = 0

	for item in items:
		crit_influence += ((1 - floating_crit) * item.crit_chance * item.crit_bonus)
		floating_crit = item.crit_chance

		base_damage += item.base_damage
		damage_percentage += item.damage_percentage

		agi += item.agi
		stre += item.stre
		inte += item.inte
		ias += item.ias

	ias += agi
	exec("base_damage += %s" % hero.primary_stat)

	average_damage_per_hit = base_damage * damage_percentage * crit_influence
	average_hits_per_second = (1.0 + ias/100.0) / hero.bat

	average_dps = average_damage_per_hit * average_hits_per_second

	return {
		"average_dps": average_dps,
		"average_hits_per_second": average_hits_per_second,
		"crit_weighted_damage_bonus": crit_influence,
		"average_damage_per_hit": average_damage_per_hit
	}

def find_ehp(hero, items):
	# things to add: evasion, blocking?
	# what about magic?
	hp = hero.base_hp
	ar = hero.base_ar

	agi = hero.base_agi
	stre = hero.base_stre

	for item in items:
		agi += item.agi
		stre += item.stre

		hp += item.hp
		ar += item.ar

	hp += (stre * 19)
	ar += (agi * 0.14)

	ehp = hp * (1 + 0.06 * ar)

	return {
		"armour_rating": ar,
		"hits": hp,
		"ehp": ehp
	}