import unittest
import pytest

from alttester import *


class Startbutton(unittest.TestCase):

    altdriver = None

    @classmethod
    def setUpClass(cls):
        cls.altdriver = AltDriver()

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()

    def test_startbutton(self):
        self.altdriver.load_scene('Start')
        self.altdriver.find_object(By.NAME, "StartButton").tap()