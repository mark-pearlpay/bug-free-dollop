class EngineFactory(object):
	def create(self, model):
		self.name = 'real'
		return self

class Car(object):
	def __init__(self, details):
		self.model = self.readEngineModel(details)
		self.engine = EngineFactory().create(self.model);

	def readEngineModel(self, details):
		return details['model']

# The test exposes the brittleness of the Car
def test_car_engine():
	# I want to test with a fake engine
	# but I can't since the EngineFactory
	# only knows how to make real engines.
	
	# TODO test car with fake engine
	# assert car.engine.name == 'fake'