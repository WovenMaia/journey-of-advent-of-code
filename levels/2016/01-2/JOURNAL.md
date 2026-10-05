# 2016 Day 1, Part 2

**Status:** solved (05/10/2026). The public examples pass, and I ran the solution on my own input before submitting its result once.

## Real input and submission

The solution printed `141` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to finding the Easter Bunny.” Part 2 is therefore solved, and Day 1 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/1). In my words: follow the same turn sequence, but report the Manhattan distance to the first intersection visited twice.

## Why Python

I kept Python because the new idea is a set of coordinates, and Python's built-in set makes the invariant readable: every coordinate in `visited` has already been walked.

## Why it is available now

Part 1 ran on my own input and Advent of Code accepted the submitted answer. Only then did I open Part 2 and read its prompt.

## First idea

Part 1 jumped from intersection to intersection. Part 2 needs every block, so I kept the same cyclic headings but expanded each distance into unit steps. After each step I test membership before adding the coordinate to the visited set.

## Wrong turns

There were no wrong turns. I made the starting coordinate visited before walking so a return to the origin is handled exactly like every other repeated location.

## Algorithmic concept

This is a **first duplicate search** over a stream of coordinates. The set gives expected O(1) membership checks while the walk preserves the order in which locations are encountered.

## Complexity

For `b` walked blocks, the algorithm takes **O(b)** expected time and **O(b)** auxiliary space for the visited set.
