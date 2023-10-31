import unittest
from io import StringIO
import sys

def hello_world():
    return "Hello World!"

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_output(self):
        # Redirect stdout to capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        hello_world()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Get the captured output
        output = captured_output.getvalue().strip()

        # Perform the test
        self.assertEqual(output, "Hello World!")

if __name__ == '__main__':
    unittest.main()
