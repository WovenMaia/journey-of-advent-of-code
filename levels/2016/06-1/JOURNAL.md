# 2016 Day 6, Part 1

**Status:** solved (05/10/2026). The public example passes, and I ran the decoder on my own input before submitting its result once.

## Real input and submission

The solution printed `gyvwpxaz` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to another.” Part 1 is solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/6). In my words: recover a repeated message by taking the most frequent character in each recorded column.

## Why Python

`Counter` states the frequency operation directly, and `zip(*rows)` exposes columns without indexing scaffolding.

## First idea

I validate that the recording is rectangular, transpose it into columns, then choose the most frequent character with alphabetical tie-breaking.

## Wrong turns

There were no wrong turns. I reject ragged recordings before decoding and make the tie rule explicit instead of relying on dictionary order.

## Algorithmic concept

This is a **column-wise reduction**: each independent column is reduced to its modal symbol, then the symbols are concatenated.

## Complexity

For `r` rows and width `c`, decoding takes **O(rc)** time and **O(r)** temporary frequency space per column.
