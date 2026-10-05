# 2015 Day 14, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/14).

## First idea

I reuse the flight/rest cycle calculation from Part 1. At each second, I calculate every reindeer's distance, find the current lead, and award one point to every reindeer at that distance. The answer is the greatest score after the full race.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover the published example at 1000 seconds, tied leaders receiving points together, the Part 1 distance boundaries, and an empty document.

## Complexity

With **N** reindeer and **T** seconds, scoring takes **O(NT)** time and **O(N)** space.

The tested solution returned `1084` for my real input. I submitted that value once for Part 2. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 14 is complete; Day 15 Part 1 is next.
