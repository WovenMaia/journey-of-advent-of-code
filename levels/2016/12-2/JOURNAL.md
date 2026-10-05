# 2016 Day 12, Part 2

**Status:** solved (05/10/2026). The published assembunny example passes, and I reran the interpreter with the changed initial register before submitting once.

## Real input and submission

Starting register `c` at 1 leaves `a = 9227661`. I submitted `9227661` once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 2 is solved and Day 12 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/12). In my words: run the same four-instruction assembunny machine, but initialize register `c` to one.

## Why Python

Only the initial register differs, so the interpreter remains transparent instead of introducing a special-case optimized formula.

## First idea

Reuse the Part 1 dispatch loop and expose the initial `c` value as an argument; Part 2 calls it with `1`.

## Wrong turns

There were no wrong submissions. I kept the machine semantics unchanged and changed only the documented initial state.

## Algorithmic concept

This is **parameterized virtual-machine execution**. The program stays constant while the initial machine state changes.

## Reuse potential

The interpreter is ready to serve later assembunny days: the operand resolver, relative jumps, register writes, and dispatch shape can be extended for additional opcodes without changing the core state model.

## Complexity

For `s` executed instructions, runtime is **O(s)** and the machine state uses **O(1)** space apart from the parsed program.
