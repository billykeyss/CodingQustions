# Determine if a string s1 is a rotation of another string s2, by calling
# (only once) a function is_substring
import unittest

def is_rotation(s1, s2):
    if s1 == None or s2 == None:
        return False
    if (len(s1) != len(s2)):
        return False
    stringCombined = s1 + s1
    return s2 in stringCombined

class TestStringMethods(unittest.TestCase):

    def test_rotation(self):
        self.assertEqual(is_rotation('o', 'oo'), False)
        self.assertEqual(is_rotation(None, 'foo'), False)
        self.assertEqual(is_rotation('', 'foo'), False)
        self.assertEqual(is_rotation('', ''), True)
        self.assertEqual(is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


if __name__ == '__main__':
    unittest.main()
