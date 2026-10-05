# 2015 Day 13, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/13).

## First idea

I parse the directed happiness changes, then enumerate every circular seating arrangement. Fixing the alphabetically first guest at the first position removes equivalent rotations; each arrangement's score adds both directed changes for each adjacent pair, including the wraparound pair.

## Wrong turns

There were no wrong turns. I briefly considered scoring only one direction for each pair, but the input is directed, so both neighbours' changes must be included.

## Public examples

The test covers the published four-person example and a small circular arrangement that checks both directions and the wraparound pair.

## Complexity

With **N** guests, the anchored enumeration checks **(N - 1)!** arrangements. Each score takes **O(N)** time, for **O(N!)** total time and **O(N)** working space beyond the preference table.

The tested solution returned `709` for my real input. I submitted that value once for Part 1. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 13 Part 1 is therefore complete; Day 13 Part 2 is next.
