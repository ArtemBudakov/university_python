import unittest
from third_lab import distance, miles_to_km, mean, concat, add, call


class TestThirdLab(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(distance(0, 0, 1, 0), 1.0)
        self.assertEqual(distance(3, -2, -1, 7), 9.848857801796104)
        self.assertEqual(distance(1, 1, 0, 0), 1.4142135623730951)

    def test_miles_to_km(self):
        self.assertEqual(miles_to_km(1), 1.609)
        self.assertEqual(miles_to_km(4), 6.436)
        self.assertNotEqual(miles_to_km(2), 0)
        self.assertNotEqual(miles_to_km(2), 6.436)

    def test_mean(self):
        self.assertEqual(mean([1, 2, 2, 4]), 2.25)
        self.assertEqual(mean([1]), 1)
        self.assertEqual(mean([1, 10, 10]), 7)

    def test_concat(self):
        self.assertEqual(concat(['a']), 'a')
        self.assertEqual(concat(['a', 'ab']), 'aab')
        self.assertEqual(concat(['a', 'asdf']), 'aasdf')

    def test_add(self):
        self.assertEqual(add(1, 5), 6)
        self.assertEqual(add(22, 6), 28)
        self.assertEqual(add(22.5, 13.22), 35.72)

    def test_call(self):
        self.assertEqual(call(add, "dasdsad", "aaaaaaaaa"), "dasdsadaaaaaaaaa")
        self.assertEqual(call(add, 26, -22), 4)
        self.assertEqual(call(add, [1, 2], ["a", "b"]), [1, 2, 'a', 'b'])
        self.assertEqual(call(add, (1, "asd", 2), ("ssss", 3333, "123")), (1, 'asd', 2, 'ssss', 3333, '123'))


if __name__ == "__main__":
    unittest.main()
