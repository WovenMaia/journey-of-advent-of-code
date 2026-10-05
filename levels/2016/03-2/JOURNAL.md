# 2016 Day 3, Part 2

**Status:** solved (05/10/2026). The public examples pass, and I ran the solution on my own input before submitting its result once.

## Real input and submission

The solution printed `1544` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 2 is therefore solved, and Day 3 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/3). In my words: regroup each three-row block vertically by columns, then count the valid triangles.

## Why Python

Python's tuples and comprehensions make the regrouping explicit: a three-row block becomes three column triples before the same strict predicate from Part 1 is applied.

## Why it is available now

Part 1 ran on my own input and Advent of Code accepted the submitted answer. Only then did I open Part 2 and read its prompt.

## First idea

I parse the rows once, take each consecutive group of three, transpose that small matrix by columns, and count the resulting triples that satisfy the triangle inequality.

## Wrong turns

There were no wrong turns. I reject incomplete groups instead of silently dropping rows, so the required vertical grouping remains explicit.

## Algorithmic concept

This is a **small matrix transpose followed by a local predicate**. The input's row layout is transformed into the puzzle's column layout, then each independent triple is classified.

## Complexity

For `n` rows, the algorithm takes **O(n)** time and **O(n)** space for the parsed rows; each three-row transpose has fixed size.
