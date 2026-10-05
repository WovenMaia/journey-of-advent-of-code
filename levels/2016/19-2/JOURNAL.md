# 2016 Day 19, Part 2

**Status:** solved (05/10/2026). The published five-elf example passes, and the real input runs locally.

## Real input and submission

The local result is `1410967`; I did not submit an answer during this session. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/19). In my words: each elf steals from the elf directly across the remaining circle until one remains.

## Why Python

The survivor pattern is piecewise arithmetic, so a power-of-three recurrence avoids simulating millions of removals.

## First idea

Find the greatest power of three not exceeding `n`. At an exact power it is the winner; in the first third-sized interval the winner is the remainder, and in the final interval it advances twice as quickly after the midpoint.

## Wrong turns

There was no wrong algorithmic turn. I checked the published five-elf example and the boundaries around powers of three, where the piecewise formula changes.

## Algorithmic concept

This is **cyclic elimination with a radix-three pattern**. Removing the opposite position changes the survivor sequence at powers of three rather than powers of two.

## Complexity

Finding the greatest power of three takes O(log n) time and O(1) memory.
