# 2016 Day 2, Part 2

**Status:** solved (05/10/2026). The public examples pass, and I ran the solution on my own input before submitting its result once.

## Real input and submission

The solution printed `9A7DC` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 2 is therefore solved, and Day 2 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/2). In my words: follow the same moves on a diamond-shaped keypad whose missing positions reject movement.

## Why Python

I kept Python because the same constrained-walk model from Part 1 applies directly; only the set of valid coordinates and labels changes.

## Why it is available now

Part 1 ran on my own input and Advent of Code accepted the submitted answer. Only then did I open Part 2 and read its prompt.

## First idea

I represent the diamond keypad as a coordinate-to-label dictionary. Each move proposes a neighboring coordinate, and the current position changes only when that coordinate exists in the dictionary.

## Wrong turns

There were no wrong turns. Starting at coordinate `(0, 2)` (button `5`) and treating absent coordinates as edges handles the irregular shape without special cases.

## Algorithmic concept

This remains a **constrained state walk**: a finite state machine over a sparse graph, with keypad buttons as vertices and valid adjacent moves as edges.

## Complexity

For `m` moves across all instruction lines, the algorithm takes **O(m)** time and **O(1)** auxiliary space besides the output code.
