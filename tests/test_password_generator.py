# test_password_generator.py
import string
import unittest
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        password = generate_password()
        self.assertEqual(len(password), 10)

    def test_password_composition(self):
        password = generate_password()
        # Checks for 2 uppercase, 2 lowercase, 2 digits, and 2 punctuation
        counts = {'upper': 0, 'lower': 0, 'digit': 0, 'punct': 0}
        for char in password:
            if char.isupper():
                counts['upper'] += 1
            elif char.islower():
                counts['lower'] += 1
            elif char.isdigit():
                counts['digit'] += 1
            elif char in string.punctuation:
                counts['punct'] += 1
        self.assertEqual(counts['upper'], 2)
        self.assertEqual(counts['lower'], 2)
        self.assertEqual(counts['digit'], 2)
        self.assertEqual(counts['punct'], 2)

if __name__ == '__main__':
    unittest.main()
