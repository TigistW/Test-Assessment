import unittest
from string_functions import *

class TestToUpper(unittest.TestCase):
    '''
    tests the to_upper functionality
    '''
    def test_upper(self):
        self.assertEqual(to_upper(''), '')
        self.assertEqual(to_upper('ASGARD'), 'ASGARD')
        self.assertEqual(to_upper('a2sv'), 'A2SV')
        self.assertTrue(to_upper("a2sv").isupper())
        self.assertFalse(to_upper("a2sv").islower())
    
class TestToLower(unittest.TestCase):
    '''
    tests the to_lower functionality
    
    '''
    def test_lower(self):
        self.assertEqual(to_upper(''), '')
        self.assertEqual(to_lower('asgard'), 'asgard')
        self.assertEqual(to_lower('A2SV'), 'a2sv')
        self.assertTrue(to_lower("A2SV").islower())
        self.assertFalse(to_lower("a2sv").isupper())
    

class TestCapitalize(unittest.TestCase):
    '''
    tests the capitalize functionality
    '''
    def test_capitalize(self):
        self.assertEqual(capitalize('a'), 'A')
        self.assertEqual(capitalize('2'), '2')
        self.assertEqual(capitalize('a2sv'), 'A2sv')
        self.assertEqual(capitalize(''), '')
    
if __name__ == '__main__':
    unittest.main()
