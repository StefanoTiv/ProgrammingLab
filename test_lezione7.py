import unittest
from CSVFile import CSVFile 

class TestInit(unittest.TestCase):
    def test_init(self):
        csv_file = CSVFile('sales')
        self.assertEqual(csv_file.name, 'sales')
