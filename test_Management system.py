import unittest
import proejct

class Testproejct(unittest.TestCase):

    def test_login(self):
        result = proejct.select()
        self.assertEqual(result,proejct.select())

    def test_moviemanager(self):
        result = proejct.moviemanager()
        self.assertEqual(result,proejct.moviemanager())
    def test_select(self):
        result = proejct.select()
        self.assertEqual(result,proejct.select())
    def test_addser(self):
        result = proejct.addser()
        self.assertEqual(result,proejct.addser())

    def test_addmov(self):
        result = proejct.addmov()
        self.assertEqual(result, proejct.addmov())
