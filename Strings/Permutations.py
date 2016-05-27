# Determine if a string is a permutation of another string
import unittest

def permutations(str1, str2):
    return (sorted(str1) == sorted(str2));

class TestStringMethods(unittest.TestCase):

    def test_rotation(self):
        self.assertEqual(permutations('', 'foo'), False)
        self.assertEqual(permutations('Nib', 'bin'), False)
        self.assertEqual(permutations('act', 'cat'), True)
        self.assertEqual(permutations('a ct', 'ca t'), True)
        print('Success: test_permutation')

if __name__ == '__main__':
    unittest.main()
