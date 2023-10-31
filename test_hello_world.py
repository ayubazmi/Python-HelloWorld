import unittest
import xmlrunner

def hello_world():
    return "Hello, World!"

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_output(self):
        self.assertEqual(hello_world(), "Hello, World!")

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
