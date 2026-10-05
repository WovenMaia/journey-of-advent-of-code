"""Public examples for Advent of Code 2016, Day 4, Part 2."""

import unittest

from solution import decrypt, find_north_pole_sector, is_real, parse_rooms


class RoomExamples(unittest.TestCase):
    def test_published_decryption_example(self) -> None:
        self.assertEqual(decrypt("qzmt-zixmtkozy-ivhz", 343), "very encrypted name")

    def test_only_real_north_pole_room_is_selected(self) -> None:
        text = """northpole-object-storage-0[oetra]
qzmt-zixmtkozy-ivhz-343[zimth]"""
        self.assertEqual(find_north_pole_sector(text), 0)

    def test_decoys_are_not_decrypted_as_targets(self) -> None:
        self.assertTrue(is_real("qzmt-zixmtkozy-ivhz", "zimth"))
        with self.assertRaisesRegex(ValueError, "invalid room"):
            parse_rooms("bad room")


if __name__ == "__main__":
    unittest.main()
