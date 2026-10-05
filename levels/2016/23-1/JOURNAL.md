# 2016 Day 23, Part 1

**Status:** staged (05/10/2026). The published example passes. The real input is pending because the Advent of Code session is unavailable.

## Real input and submission

No real input result is recorded yet. I did not submit an answer. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/23). In my words: execute self modifying assembunny code with register `a` initialized to 7.

## Why Python

The instruction set is small, and a mutable list of token lists makes the toggle rule direct.

## First idea

Keep an instruction pointer and four registers. Execute valid instructions, toggle the operation at the computed target, and skip invalid register destinations rather than inventing behavior for them.

## Wrong turns

There was no wrong algorithmic turn. The published toggle example, an invalid destination, and a configurable initial register check the interpreter boundaries.

## Algorithmic concept

This is **self modifying interpretation**. The program changes its own operation names while the arguments remain fixed.

## Complexity

For `s` executed instructions and `p` program lines, execution costs O(s) time and O(p) memory.
