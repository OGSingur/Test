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

    def test_loadscene(self):       
        self.altdriver.load_scene('Main',True)

   
    def test_find_cat(self):
        cat = self.altdriver.find_object(By.NAME,"CatMesh")
        print(cat)
        assert(cat)
        