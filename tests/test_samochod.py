import unittest
from unittest.mock import *
from src.samochod import *


class TestSamochod(unittest.TestCase):

    def setUp(self):
        self.temp = Car()

    def test_needsFuel_return_false(self):
        self.temp.needsFuel = Mock(name='needsFuel')
        self.temp.needsFuel.return_value = False
        self.assertEqual(self.temp.needsFuel(), False)

    def test_needsFuel_return_true(self):
        self.temp.needsFuel = Mock(name='needsFuel')
        self.temp.needsFuel.return_value = True
        self.assertEqual(self.temp.needsFuel(), True)

    @patch.object(Car, 'driveTo')
    def test_driveTo_patch(self, mock_method):
        mock_method.return_value = 'Szczecinek'
        result = self.temp.driveTo('Szczecinek')
        self.assertEqual(result, 'Szczecinek')

    @patch.object(Car, 'getEngineTemperature')
    def test_getEngineTemperature_patch(self, mock_method):
        mock_method.return_value = 60
        result = self.temp.getEngineTemperature()
        self.assertEqual(result, 60)


if __name__ == '__main__':
    unittest.main()
