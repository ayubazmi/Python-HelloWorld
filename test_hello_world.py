import unittest

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_output(self):
        # Call the hello_world function and capture the result
        result = hello_world()
        
        # Print the result, which will be displayed in the workflow summary
        print(result)
        
        # Perform the test
        self.assertEqual(result, "Hello, World!")

if __name__ == '__main__':
    unittest.main()
