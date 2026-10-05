"""Public examples for Advent of Code 2016, Day 12, Part 2."""

import unittest

from solution import run


EXAMPLE = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""


class AssembunnyExamples(unittest.TestCase):
    def test_published_program_still_runs(self) -> None:
        self.assertEqual(run(EXAMPLE)["a"], 42)

    def test_part_two_starts_c_at_one(self) -> None:
        self.assertEqual(run("cpy c a")["a"], 1)

    def test_invalid_instruction_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "invalid instruction"):
            run("mul a b")


if __name__ == "__main__":
    unittest.main()
