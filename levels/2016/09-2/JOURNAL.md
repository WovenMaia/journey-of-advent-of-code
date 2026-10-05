# 2016 Day 9, Part 2

**Status:** solved (05/10/2026). The recursive examples pass, and I measured the real input without expanding it.

## Real input and submission

The recursively decompressed length is `11451628995`. I submitted it once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 2 is solved and Day 9 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/9). In my words: markers inside a marker payload are now expanded recursively, so only the total length is feasible.

## Why Python

The recursive function returns lengths rather than strings, keeping the solution bounded even when the conceptual output is many gigabytes.

## First idea

Use the same cursor parser as Part 1, but recurse over each marker's exact payload interval before multiplying its length.

## Wrong turns

There were no wrong submissions. I kept the Part 1 non-recursive interpretation separate from this recursive one instead of trying to share a misleading expansion routine.

## Algorithmic concept

This is **divide-and-conquer parsing**: each marker defines a nested interval, and the parent combines its children's lengths.

## Complexity

The parser visits each input character and marker once, using **O(n)** time and **O(d)** call-stack space for maximum marker nesting depth `d`; it never allocates the expanded output.
