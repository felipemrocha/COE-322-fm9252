import unittest
from read_animals import breed

parent1 = {'head' : 'snake', 'body' : 'goat-bee', 'arms' : 2, 'legs' : 2, 'tails' : 4}
wrong = {'head' : 2, 'body' : True, 'arms' : 'snake', 'legs' : 'goat', 'tails' : [1,2,3]}

class TestReadAnimals(unittest.TestCase):

	def test_breed(self):
		self.assertEqual(breed(parent1,parent1), str(parent1))
		self.assertRaises(AssertionError, breed, 1,2)
		self.assertRaises(AssertionError, breed, 1,parent1)
		self.assertRaises(AssertionError, breed, parent1,2)
		self.assertRaises(AssertionError, breed, True,parent1)
		self.assertRaises(AssertionError, breed, [1,2], parent1)
		self.assertRaises(AssertionError, breed, parent1, wrong)




if __name__ == '__main__':
    unittest.main()
