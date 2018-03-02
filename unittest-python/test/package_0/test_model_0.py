import unittest

from package_0.model_0 import MyClass_0


class Test(unittest.TestCase):

    def setUp(self):
        self.my_class = MyClass_0()

    def tearDown(self):
        self.my_class = None

    def test_00_assertEqual(self):
        self.assertEqual("string", self.my_class.get_string())


if __name__ == "__main__":
    unittest.main()
