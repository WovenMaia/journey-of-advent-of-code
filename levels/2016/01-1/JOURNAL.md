# 2016 Day 1, Part 1

**Status:** solved (05/10/2026). The public examples pass, and I ran the solution on my own input before submitting its result once.

## Real input and submission

The solution printed `239` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to finding the Easter Bunny.” Part 1 is therefore solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/1). In my words: turn left or right on a city grid, walk each requested distance, and report the Manhattan distance to the final intersection.

## Why Python

I chose Python because the level is a small state machine: a heading, a coordinate, and a sequence of turns. Tuples keep coordinates explicit while the standard library is unnecessary overhead.

## First idea

I represent North, East, South, and West as a cyclic tuple of vectors. Each turn advances or rewinds the heading index, then one vector-times-distance update moves the coordinate.

## Wrong turns

There were no wrong turns. I first checked the examples against signed coordinates and kept parsing strict so an accidental malformed token cannot silently change the route.

## Algorithmic concept

The route is a **state transition fold**. Each instruction consumes the previous heading and position and produces the next state. The answer is the Manhattan norm of the final coordinate.

## Complexity

For `n` instructions, the algorithm takes **O(n)** time and **O(1)** auxiliary space.
