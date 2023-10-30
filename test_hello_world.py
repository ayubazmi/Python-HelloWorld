import unittest
from hello_world import say_hello  # Import the function to be tested

class TestHelloWorld(unittest.TestCase):

    def test_hello_world_presence(self):
        result = say_hello()
        self.assertIn("Hello World!", result)

if __name__ == '__main__':
    unittest.main()
