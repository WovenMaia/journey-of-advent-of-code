# 2015 Day 5, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/5). I read Part 2 only.

## First idea

The old three rules are discarded. I scan each string for two independent conditions: a two-letter pair must recur at a later, non-overlapping position, and some letter must recur with exactly one character between the two copies. The first condition keeps the earliest index for each pair, so an adjacent overlapping occurrence such as the two `aa` pairs in `aaa` does not count.

## Wrong turns

My first mental shortcut was to treat any repeated pair as sufficient. That would incorrectly accept strings such as `ieodomkazucvgmuy`, which has the separated-letter pattern but no repeated pair. I also had to keep the pair's first occurrence instead of replacing it after an overlap; otherwise a later valid non-overlapping occurrence could be missed.

## Public examples

The prompt's examples classify `qjhvhtzxzqqjkmpb` and `xxyxx` as nice, while `uurcxstgmygtbstg` and `ieodomkazucvgmuy` are naughty. The tests cover all four examples, verify that exactly two are nice, and pin the overlapping `aaa` edge case.

## Complexity

For a string of length $n$, both scans take **O(n)** time and the pair-index map uses **O(n)** auxiliary space. Across the input, the total running time is **O(N)** for $N$ characters.

## Submission

I ran the tested solution on my own input; it returned `69`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 5 Part 2 is therefore complete.
