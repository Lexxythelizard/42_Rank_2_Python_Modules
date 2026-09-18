#!/usr/bin/python3

# TODO:
"""
It is now time to define the test scenario. The capacitor.py script, located at the root
of the Git repository, will proceed as follows:
	• Create a healing Creature factory.
	• Create the base, then the evolved Creature and make them:
		1) be described;
		2) attack;
		3) heal.
	• Create a transforming Creature factory.
	• Create the base, then the evolved Creature and make them:
		1) be described;
		2) attack;
		3) transform;
		4) attack again;
		5) revert.
"""

# Example output:
"""
$> python3 capacitor.py
Testing Creature with healing capability
base:
Sproutling is a Grass type Creature
Sproutling uses Vine Whip!
Sproutling heals itself for a small amount
evolved:
Bloomelle is a Grass/Fairy type Creature
Bloomelle uses Petal Dance!
Bloomelle heals itself and others for a large amount
Testing Creature with transform capability
base:
Shiftling is a Normal type Creature
Shiftling attacks normally.
Shiftling shifts into a sharper form!
Shiftling performs a boosted strike!
Shiftling returns to normal.
evolved:
Morphagon is a Normal/Dragon type Creature
Morphagon attacks normally.
Morphagon morphs into a dragonic battle form!
Morphagon unleashes a devastating morph strike!
Morphagon stabilizes its form.
"""
