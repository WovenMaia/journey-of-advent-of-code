# 2016 Day 8, Part 1

**Status:** solved (05/10/2026). The public example passes, and I ran the display simulator on my own input before submitting its result once.

## Real input and submission

The solution counted `116` lit pixels. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to another.” Part 1 is solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/8). In my words: execute rectangle, row-rotation, and column-rotation instructions on a 50×6 pixel display, then count the lit pixels.

## Why Python

A list of boolean rows makes each operation and wraparound behavior explicit without bringing in a graphics dependency.

## First idea

Keep a 50×6 matrix, apply each command in order, and render/count only after the full instruction stream has run.

## Wrong turns

There were no wrong turns. Row and column rotations copy wrapped slices rather than dropping pixels, and dimensions are validated before mutation.

## Algorithmic concept

This is a **state-machine simulation**: each instruction transforms a finite display state, and the final state answers the question.

## Complexity

For `n` commands on a `w×h` display, the simulation uses **O(nwh)** worst-case time and **O(wh)** space.
