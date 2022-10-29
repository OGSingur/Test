import unittest
import pytest

from alttester import *

class Searchanimals(unittest.TestCase):
    
    altdriver = None

    @classmethod
    def setUpClass(cls):
        cls.altdriver = AltDriver()

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
    
    def test_find_animals(self):
        rat = self.altdriver.find_object(By.NAME,"Rat")
        dog = self.altdriver.find_object(By.NAME,"Dog")
        cat = self.altdriver.find_object(By.NAME,"Cat")
        print(rat)
        print(dog)
        print(cat)

        assert(rat and dog and cat)    