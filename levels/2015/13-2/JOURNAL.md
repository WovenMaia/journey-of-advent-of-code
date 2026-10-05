# 2015 Day 13, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/13).

## First idea

I reused the directed preference parser and circular scoring from Part 1. I add myself as one more guest, set every relationship involving me to zero, anchor the first guest, and enumerate the remaining circular arrangements.

## Wrong turns

There were no wrong turns. The only important adjustment is that zero happiness applies in both directions for every pair involving me.

## Public examples

The tests cover the published example, the directed wraparound score, and the zero contribution from the added guest.

## Complexity

With **N** original guests, the anchored enumeration checks **N!** arrangements. Each score takes **O(N)** time, for **O(N · N!)** total time and **O(N²)** space including the preference table.

The tested solution returned `668` for my real input. I submitted that value once for Part 2. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 13 Part 2 is complete; Day 14 Part 1 is next.
