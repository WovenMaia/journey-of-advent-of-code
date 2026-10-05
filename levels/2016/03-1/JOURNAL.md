# 2016 Day 3, Part 1

**Status:** solved (05/10/2026). The public examples pass, and I ran the solution on my own input before submitting its result once.

## Real input and submission

The solution printed `869` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 1 is therefore solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/3). In my words: count the listed triples whose side lengths satisfy the strict triangle inequality.

## Why Python

Python's sorting and tuple handling make the geometric condition direct: after ordering the sides, only the two shorter sides need to be compared with the longest.

## First idea

I parse each non-empty row into three integers, sort the triple, and test whether the first two values sum to more than the third. Summing those booleans gives the count.

## Wrong turns

There were no wrong turns. I kept the inequality strict, so a degenerate triple such as `1 2 3` is correctly rejected.

## Algorithmic concept

This is a **streaming predicate count**. Each row is independent, and a normalized local predicate decides whether it contributes one to the total.

## Complexity

For `n` rows, the algorithm takes **O(n)** time (each row has three fixed-size sides) and **O(n)** space for the parsed rows.
