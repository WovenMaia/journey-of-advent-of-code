# 2015 Day 2, Part 1

**Status:** solved (30/09/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/2). I opened its prompt only after completing Day 1 on the site.

## First idea

Each line describes one rectangular present. I compute its three face areas, double their sum for the surface, then add the smallest face as the extra allowance. The total is the sum of that calculation over every line.

## Public examples

The prompt's two example presents require `58` and `43` square feet, respectively. Together they require `101`. The tests cover those values, multiple lines, malformed dimensions, and non-positive dimensions.

## Complexity

For `n` presents, the solution takes **O(n)** time. Each present uses **O(1)** auxiliary space.

## Submission

I ran the tested solution on my own input; it returned `1588178`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Part 1 is therefore solved.
