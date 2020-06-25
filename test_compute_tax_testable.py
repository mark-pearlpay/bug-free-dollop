# Reworked, it only asks for the specific
# objects that it needs to collaborate with.
class SalesTaxCalculator(object):
	# Note that we no longer use user or invoice,
	# nor do we dig inside the address
	def computeTax(self, address, amount):
		return amount * self.getTaxRate(address)

	def getTaxRate(self, address):
		if address == 'makati':
			return 0.3

		if address == 'quezon':
			return 0.1

# The new API is clearer in what collaborators it needs.
def test_compute_tax():
	calc = SalesTaxCalculator()

	# Only ask the objects that are needed
	tax = calc.computeTax('makati', 100)

	# TODO test computed tax for makati
	assert tax == 30.0