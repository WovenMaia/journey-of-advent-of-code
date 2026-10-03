# 2015 Day 2, Part 2

**Status:** solved (03/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/2). I read Part 2 only after Part 1 had been accepted.

## First idea

For each present, I sort its three dimensions. The wrapping portion is twice the sum of the two shortest dimensions; the bow is the product of all three. I add those two quantities for every line.

## Public examples

The prompt's two example presents require `34` and `14` feet of ribbon. Together they require `48`. The tests cover those values, multiple lines, malformed dimensions, and non-positive dimensions.

## Complexity

For `n` presents, the solution takes **O(n)** time and **O(1)** auxiliary space per present.

## Submission

I ran the tested solution on my own input; it returned `3783758`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 2 is therefore complete.
