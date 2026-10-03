# 2015 Day 3, Part 1

**Status:** solved (03/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/3). I opened it only after completing Day 2.

## First idea

I represent each house as an `(x, y)` coordinate, start with the origin in a set, and translate the coordinate once per direction. Adding every destination to the set makes revisits harmless; the answer is the final set size.

## Public examples

The prompt's examples visit `2`, `4`, and `2` distinct houses. The tests also confirm that the starting house counts when there are no moves and that an unknown direction is rejected.

## Complexity

For `n` directions, the solution takes **O(n)** expected time and **O(n)** space in the worst case for the visited-house set.

## Submission

I ran the tested solution on my own input; it returned `2572`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Part 2 then became available.
