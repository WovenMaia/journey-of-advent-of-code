# 2016 Day 12, Part 1

**Status:** solved (05/10/2026). The published assembunny example passes, and I ran the interpreter on the real program before submitting once.

## Real input and submission

Register `a` ends at `318007`. I submitted `318007` once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 1 is solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/12). In my words: execute `cpy`, `inc`, `dec`, and relative `jnz` instructions until the instruction pointer leaves the program.

## Why Python

A small direct interpreter keeps instruction-pointer behavior visible and is easy to reuse for later assembunny days.

## First idea

Tokenize each line, resolve register-or-integer operands, and advance the instruction pointer explicitly for each operation.

## Wrong turns

There were no wrong submissions. I treated `jnz` offsets as relative to the jump instruction itself, so an offset of `2` skips exactly one following instruction.

## Algorithmic concept

This is **virtual-machine interpretation**: the program is data, and the register dictionary plus instruction pointer are its complete machine state.

## Reuse potential

The interpreter's dispatch loop and operand resolver are deliberately small and are the natural base for later assembunny extensions such as `tgl` and `out`.

## Complexity

For `s` executed instructions, runtime is **O(s)** and the machine state uses **O(1)** space apart from the parsed program.
