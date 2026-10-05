# 2016 Day 6, Part 2

**Status:** solved (05/10/2026). The public example passes, and I ran the decoder on my own input before submitting its result once.

## Real input and submission

The solution printed `jucfoary` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 2 is solved and Day 6 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/6). In my words: use the least frequent character in each recorded column to recover the quieter message.

## Why Python

The same rectangular parser serves both halves; only the ordering of each column's frequency key changes.

## First idea

I transpose the rows, count each column, and select the least frequent character, breaking ties alphabetically for a deterministic result.

## Wrong turns

There were no wrong turns. The tie-break is explicit, and the rectangular-input guard prevents a short row from silently changing column alignment.

## Algorithmic concept

This is the **dual of modal decoding**: the same column reduction works when the signal is defined by a minimum rather than a maximum.

## Complexity

For `r` rows and width `c`, decoding takes **O(rc)** time and **O(r)** temporary frequency space per column.
