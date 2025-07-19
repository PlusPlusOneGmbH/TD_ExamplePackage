'''Info Header Start
Name : extExampleExtension
Author : Wieland PlusPlusOne@AMB-ZEPH15
Saveorigin : Dev.toe
Saveversion : 2023.12000
Info Header End'''


from TDStoreTools import StorageManager
import TDFunctions as TDF

class extExampleExtension:
	"""
	extExampleExtension description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

		# properties
		TDF.createProperty(self, 'MyProperty', value=0, dependable=True,
						   readOnly=False)

		# attributes:
		self.a = 0 # attribute
		self.B = 1 # promoted attribute

		# stored items (persistent across saves and re-initialization):
		storedItems = [
			# Only 'name' is required...
			{'name': 'StoredProperty', 'default': None, 'readOnly': False,
			 						'property': True, 'dependable': True},
		]
		# Uncomment the line below to store StoredProperty. To clear stored
		# 	items, use the Storage section of the Component Editor
		
		# self.stored = StorageManager(self, ownerComp, storedItems)

	def myFunction(self, v):
		debug(v)

	def PromotedFunction(self, v):
		debug(v)
