class Kitchen(object):
	def __init__(self):
		self.name = 'real'

class Bedroom(object):
	def __init__(self):
		self.name = 'real'

# Basic new operators called directly in
# the constructor. (Forever
# preventing a seam to create different
# kitchen and bedroom collaborators).
class House(object):
	def __init__(self):
		self.kitchen = Kitchen()
		self.bedroom = Bedroom()

def test_house():
	# Darn! I'm stuck with those Kitchen and
	# Bedroom objects created in the
	# constructor. 

	# TODO test car with dummy kitchen and bedroom
	# assert house.bedroom.name == 'dummy'
	# assert house.kitchen.name == 'dummy'