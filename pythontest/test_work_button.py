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
        
    def test_workbutton(self):
        self.altdriver.find_object(By.NAME,"SettingButton").tap()
        self.altdriver.find_object(By.NAME,"About").tap()
        self.altdriver.find_object(By.NAME,"BackButton").tap()
        self.altdriver.find_object(By.NAME,"CloseButton").tap()