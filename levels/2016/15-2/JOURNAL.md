# 2016 Day 15, Part 2

**Status:** solved (05/10/2026). The published two-disc schedule still passes as a regression check, and the solver adds the seventh disc required by Part 2 before searching the real schedule.

## Real input and submission

The earliest button time is `2353212`. I did not submit a second answer during this session; this journal records the local result only.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/15). In my words: add one more disc to the timing constraints and find the first button time at which every slot is aligned.

## Why Python

The input is tiny, and a direct modular search keeps the extra disc and the one-second-per-disc offset visible.

## First idea

Reuse the Part 1 congruence check, append disc number seven with eleven positions at position zero, and try button times from zero upward.

## Wrong turns

There was no separate published Part 2 example. I kept the published Part 1 schedule as a regression check and used a small expected-value check for the added disc rather than inventing a claim about an AoC example.

## Algorithmic concept

This is **constraint search over modular congruences**. Testing timestamps in increasing order preserves the first satisfying timestamp.

## Complexity

For `t` tested timestamps and `d` discs, runtime is **O(t·d)** and extra space is **O(d)** for the parsed schedule.
