# 2016 Day 4, Part 1

**Status:** solved (05/10/2026). The public examples pass, and I ran the solution on my own input before submitting its result once.

## Real input and submission

The solution printed `245102` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 1 is therefore solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/4). In my words: identify real rooms by their five-letter frequency checksum and sum their sector IDs.

## Why Python

Python's `Counter` directly expresses the frequency table, while sorting with a two-part key makes the frequency and alphabetical tie-break rules visible.

## First idea

I parse each room with one anchored regular expression, remove dashes for counting, sort letters by descending frequency and ascending letter, and compare the first five letters with the supplied checksum.

## Wrong turns

There were no wrong turns. Dashes are separators rather than letters, and the checksum comparison keeps the tie-break alphabetical instead of relying on incidental dictionary order.

## Algorithmic concept

This is a **canonical signature check**. Each encrypted name is reduced to a deterministic five-letter signature, then the room is classified by equality.

## Complexity

For `n` rooms and `c` total name characters, the algorithm takes **O(c log a)** time where `a` is the alphabet size, and **O(a)** auxiliary space per room.
