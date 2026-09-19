import unittest
from originalCode import calculate_damage
from originalCode import is_alive

class testGame(unittest.TestCase):

    def test_calculate_damamge(self):
        self.assertEqual(calculate_damage(10, 5), 5)
        self.assertEqual(calculate_damage(5, 10), 0)
        self.assertEqual(calculate_damage(20, 15), 5)
        self.assertEqual(calculate_damage(0, 0), 0)
        self.assertEqual(calculate_damage(-5, -10), 5)

    def test_is_alive(self):
        self.assertTrue(is_alive(10))
        self.assertFalse(is_alive(0))
        self.assertFalse(is_alive(-5))

if __name__ == "__main__":
    unittest.main()