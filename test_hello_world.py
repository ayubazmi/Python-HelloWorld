import unittest
from hello_world import say_hello

class TestHelloWorld(unittest.TestCase):

    def test_hello_world_output(self):
        self.assertEqual(say_hello(), "Hello, World!")

    def test_hello_world_type(self):
        self.assertTrue(isinstance(say_hello(), str))

if __name__ == '__main__':
    unittest.main()
