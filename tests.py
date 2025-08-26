import unittest
from main import suma 
class TestPrueba(unittest.Testcase):
    def test_suma (self):
        self.assertequal(suma(2,3),5)
        if __name__== "__main__":
            unittest.main()