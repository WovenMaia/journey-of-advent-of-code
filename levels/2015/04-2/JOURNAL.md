# 2015 Day 4, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/4). I read Part 2 only after Part 1 had been accepted.

## First idea

I search positive integer suffixes in ascending order. For each suffix, I hash the secret key followed by its decimal representation and stop at the first digest whose hexadecimal form begins with six zeroes. The ordered search makes the first match the required lowest number.

## Public examples

The Part 2 prompt has no public examples. The test checks the six-zero rule and the known lowest suffix for `abcdef`.

## Complexity

Each MD5 digest has a one-in-$16^6 = 16,777,216$ chance of beginning with six hexadecimal zeroes, so the expected search takes about **16,777,216 hash attempts**. For the successful suffix $k$, this implementation takes **O(k log k)** time because decimal-suffix encoding costs O(log k) per attempt, and **O(1)** auxiliary space.

## Submission

I ran the tested solution on my own input; it returned `9962624`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 4 is therefore complete. Day 5 Part 1 is next.
