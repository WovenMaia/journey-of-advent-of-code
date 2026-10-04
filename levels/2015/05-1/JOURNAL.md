# 2015 Day 5, Part 1

**Status:** solved (04/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/5). I read Part 1 only.

## First idea

I check each string against the three rules independently: count at least three vowels, find a repeated adjacent letter, and reject any string containing `ab`, `cd`, `pq`, or `xy`. A string is nice only when all three checks pass.

## Public examples

The prompt's examples classify `ugknbfddgicrmopn` and `aaa` as nice, and `jchzalrnumimnmhp`, `haegwjzuvuyypxyu`, and `dvszwmarrgswjxmb` as naughty. The tests cover all five examples and verify that exactly two are nice.

## Complexity

For a string of length $n$, the checks take **O(n)** time and **O(1)** auxiliary space. Across the input, the total running time is **O(N)** for $N$ characters.

## Submission

I ran the tested solution on my own input; it returned `238`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 5 Part 1 is therefore complete. Day 5 Part 2 is next.
