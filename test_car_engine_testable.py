# Asks for precisely what it needs
class Car(object):
    def __init__(self, engine):
        self.name = engine

class Engine(object):
    def __init__(self, engine):
        self.engine = engine

# Now we can see a flexible, injectible design
def test_car_engine():
	engine = Engine('fake')
	car = Car(engine)

	# Now testing is easy, with the car taking
	# exactly what it needs.
	assert car.engine.name == 'fake'
