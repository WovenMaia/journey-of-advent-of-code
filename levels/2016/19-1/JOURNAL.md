# 2016 Day 19, Part 1

**Status:** solved (05/10/2026). The published five-elf example passes, and the real input runs locally.

## Real input and submission

The local result is `1816277`; I did not submit an answer during this session. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/19). In my words: elves in a circle repeatedly steal from the next elf until one remains.

## Why Python

The survivor pattern is clearer as a small arithmetic formula than as a list simulation for the large input.

## First idea

This is Josephus with step two. For `n`, remove the highest power of two, double the remainder, and shift back to one-based elf numbering.

## Wrong turns

There was no wrong algorithmic turn. The five-elf example and powers-of-two checks make the indexing convention explicit.

## Algorithmic concept

This is **Josephus elimination**. Rotating the circle after each removal gives a simple recurrence whose closed form is `2(n - 2^floor(log2 n)) + 1`.

## Complexity

The formula uses O(1) time and O(1) memory.
