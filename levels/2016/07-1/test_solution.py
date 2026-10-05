"""Public examples for Advent of Code 2016, Day 7, Part 1."""

import unittest

from solution import count_tls, supports_tls


class TlsExamples(unittest.TestCase):
    def test_published_examples(self) -> None:
        self.assertTrue(supports_tls("abba[mnop]qrst"))
        self.assertFalse(supports_tls("abcd[bddb]xyyx"))
        self.assertFalse(supports_tls("aaaa[qwer]tyui"))
        self.assertTrue(supports_tls("ioxxoj[asdfgh]zxcvbn"))

    def test_count(self) -> None:
        self.assertEqual(count_tls("abba[mnop]qrst\nabcd[bddb]xyyx"), 1)


if __name__ == "__main__":
    unittest.main()
