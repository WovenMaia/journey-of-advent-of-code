# 2015 Day 14, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/14).

## First idea

I parse each reindeer's speed and repeating flight/rest durations. For a race duration, whole cycles contribute a fixed distance; the final partial cycle contributes only its flying seconds. The winner is the greatest resulting distance.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover the published two-reindeer example at 1000 seconds, partial flight and rest boundaries, and an empty document.

## Complexity

With **N** reindeer, parsing and scoring take **O(N)** time and **O(N)** space.

The tested solution returned `2696` for my real input. I submitted that value once for Part 1. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 14 Part 1 is complete; Day 14 Part 2 is next.
