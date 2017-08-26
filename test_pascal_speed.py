import unittest
import pascal
import time

class PascalTestSpeed(unittest.TestCase):

    def test_pascal_speed(self):
        t0 = time.time()
        pascal.pascal(10000)
        t1 = time.time()
        total_time = t1 - t0
        print("\nv1 time: %ss" % str(total_time))

    def test_pascal_speed_v2(self):
        t0 = time.time()
        pascal.pascal_v2(10000)
        t1 = time.time()
        total_time = t1 - t0
        print("\nv2 time: %ss" % str(total_time))

def main():
    unittest.main()

if __name__ == "__main__":
    main()