import unittest

def hello_world():
    return "Hello, World!"

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_output(self):
        # Call the hello_world function and capture the result
        result = hello_world()

        # Perform the test
        self.assertEqual(result, "Hello World!")  # Note the change to "Hello, World!" here

        # If the test case fails, print "gta"
        if result != "Hello, World!":
            print("gta")

if __name__ == '__main__':
    unittest.main()
