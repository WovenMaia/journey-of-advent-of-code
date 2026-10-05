"""Public examples for Advent of Code 2016, Day 7, Part 2."""

import unittest

from solution import count_ssl, supports_ssl


class SslExamples(unittest.TestCase):
    def test_published_examples(self) -> None:
        self.assertTrue(supports_ssl("aba[bab]xyz"))
        self.assertFalse(supports_ssl("xyx[xyx]xyx"))
        self.assertTrue(supports_ssl("aaa[kek]eke"))
        self.assertTrue(supports_ssl("zazbz[bzb]cdb"))

    def test_count(self) -> None:
        self.assertEqual(count_ssl("aba[bab]xyz\nxyx[xyx]xyx"), 1)


if __name__ == "__main__":
    unittest.main()
