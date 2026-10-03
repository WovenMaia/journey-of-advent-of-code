# 2015 Day 3, Part 2

**Status:** solved (03/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/3). I read Part 2 only after Part 1 had been accepted.

## First idea

I keep one coordinate for Santa and one for Robo-Santa. Their instructions alternate by position, while both add destinations to the same visited-house set. The starting house appears once in that set even though both begin there.

## Public examples

The prompt's examples visit `3`, `3`, and `11` distinct houses. The tests also confirm that the shared starting house counts once when there are no moves and that an unknown direction is rejected.

## Complexity

For `n` directions, the solution takes **O(n)** expected time and **O(n)** space in the worst case for the shared visited-house set.

## Submission

I ran the tested solution on my own input; it returned `2631`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 3 is therefore complete.
