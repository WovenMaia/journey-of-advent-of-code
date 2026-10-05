# 2015 Day 10, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/10).

## First idea

Part 2 keeps the Part 1 transformation and extends the run count from 40 to 50. I use `itertools.groupby` to walk each maximal run once, emitting its length and digit in order. The sequence remains a string throughout, so each pass is linear in the value it has to read and produce.

## Wrong turns

I first wondered whether the Part 2 length could be obtained by extrapolating the Part 1 result, but the sequence's run structure—not just its current length—determines the next pass. I also kept the tempting approach of counting all digits in one pass out of the implementation: global counts lose the order of adjacent runs. I did not submit a wrong answer.

## Public examples

The tests cover the published sequence of transformations, repeated passes, independent runs, and rejection of non-digit or negative-input arguments.

## Complexity

If the successive sequence lengths are **L₀, L₁, ..., L₅₀**, the run scan takes **O(L₀ + L₁ + ... + L₅₀)** time and **O(max Lᵢ)** space for the current and next sequences.

The tested solution returned `6989950` for my real input. I submitted that value once after checking that Part 2 was still unsolved. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 10 is therefore complete; Day 11 Part 1 is next.
