"""Public examples for Advent of Code 2016, Day 4, Part 1."""

import unittest

from solution import is_real, parse_rooms, sector_sum


class RoomExamples(unittest.TestCase):
    def test_published_examples(self) -> None:
        text = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""
        self.assertEqual(sector_sum(text), 1514)

    def test_frequency_ties_are_alphabetical(self) -> None:
        self.assertTrue(is_real("a-b-c-d-e-f-g-h", "abcde"))
        self.assertFalse(is_real("totally-real-room", "decoy"))

    def test_malformed_rooms_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid room"):
            parse_rooms("not-a-room")


if __name__ == "__main__":
    unittest.main()
