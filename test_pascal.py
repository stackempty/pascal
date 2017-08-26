import unittest
import pascal
import timeit

class PascalTest(unittest.TestCase):

    def test_pascal(self):
        test_1 = pascal.pascal(0)
        self.assertEqual(test_1, [1])

        test_2 = pascal.pascal(1)
        self.assertEqual(test_2, [1,1])

        test_3 = pascal.pascal(2)
        self.assertEqual(test_3, [1,2,1])

        test_4 = pascal.pascal(3)
        self.assertEqual(test_4, [1,3,3,1])

        test_5 = pascal.pascal(10)
        self.assertEqual(test_5, [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1])

    
    def test_pascal_v2(self):
        test_1 = pascal.pascal_v2(0)
        self.assertEqual(test_1, [1])

        test_2 = pascal.pascal_v2(1)
        self.assertEqual(test_2, [1,1])

        test_3 = pascal.pascal_v2(2)
        self.assertEqual(test_3, [1,2,1])

        test_4 = pascal.pascal_v2(3)
        self.assertEqual(test_4, [1,3,3,1])

        test_5 = pascal.pascal_v2(10)
        self.assertEqual(test_5, [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1])

def main():
    unittest.main()

if __name__ == "__main__":
    main()