import unittest
import pytest

from alttester import *


class Loadscene(unittest.TestCase):

    altdriver = None

    @classmethod
    def setUpClass(cls):
        cls.altdriver = AltDriver()

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
        
    def test_gameplay(self):
       self.altdriver.find_object(By.NAME,"StartButton").tap()
       