# 2015 Day 10, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/10).

## First idea

The input is a digit string. Each pass scans its consecutive runs from left to right and emits the run length followed by the repeated digit. Keeping the current run's start index avoids repeatedly slicing the sequence, and building the next value from pieces keeps the transformation direct.

## Wrong turns

I first considered treating the sequence as individual digit counts, but that loses the order of adjacent runs: `211` must distinguish one `2` followed by two `1`s. I also tried running the script from inside the level directory; its established entry-point convention resolves `inputs/` from the repository root, so the real-input command is run from the root instead. I did not submit a wrong answer.

## Public examples

The tests cover the published sequence of transformations, repeated passes, independent runs, and rejection of non-digit or negative-input arguments.

## Complexity

If the successive sequence lengths are **L₀, L₁, ..., L₄₀**, the run scan takes **O(L₀ + L₁ + ... + L₄₀)** time and **O(max Lᵢ)** space for the current and next sequences.

## Submission

The tested solution returned `492982` for my real input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 10 Part 1 is therefore complete; Day 10 Part 2 is next.
