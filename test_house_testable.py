class Kitchen(object):
	def __init__(self, name):
		self.name = name

class Bedroom(object):
	def __init__(self, name):
		self.name = name

class DummyKitchen(object):
	def __init__(self, name):
		self.name = name

class DummyBedroom(object):
	def __init__(self, name):
		self.name = name

# New and Improved is trivially testable, with any
# test-double objects as collaborators
class House(object):
	def __init__(self, kitchen, bedroom):
		self.kitchen = kitchen
		self.bedroom = bedroom

def test_house():
	# Awesome, I can use test doubles that
	# are lighter weight.
	kitchen = DummyKitchen('dummy')
	bedroom = DummyBedroom('dummy')
	house = House(kitchen, bedroom)
	
	assert house.bedroom.name == 'dummy'
	assert house.kitchen.name == 'dummy'

