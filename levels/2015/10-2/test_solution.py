"""Public examples for Advent of Code 2015, Day 10, Part 2."""

import unittest

from solution import look_and_say, result_length


class LookAndSayExamples(unittest.TestCase):
    def test_public_examples(self) -> None:
        sequence = "1"
        expected = ("11", "21", "1211", "111221", "312211")
        for value in expected:
            sequence = look_and_say(sequence, 1)
            self.assertEqual(sequence, value)

    def test_multiple_repetitions_match_repeated_steps(self) -> None:
        self.assertEqual(look_and_say("1", 5), "312211")
        self.assertEqual(result_length("1", 5), 6)

    def test_runs_are_counted_independently(self) -> None:
        self.assertEqual(look_and_say("211", 1), "1221")

    def test_invalid_sequence_and_repetition_count_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            look_and_say("", 1)
        with self.assertRaises(ValueError):
            look_and_say("12a", 1)
        with self.assertRaises(ValueError):
            look_and_say("1", -1)


if __name__ == "__main__":
    unittest.main()
