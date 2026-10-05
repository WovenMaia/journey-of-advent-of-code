# 2016 Day 5, Part 2

**Status:** solved (05/10/2026). The public example passes, and I ran the bounded MD5 search on my own input before submitting its result once.

## Real input and submission

The solution printed `8c35d1ab` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 2 is solved and Day 5 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/5). In my words: qualifying hashes now name a password position with their sixth character, and contribute the seventh character only to an empty valid position.

## Why Python

`hashlib` keeps the expensive part standard-library-only, while a list of optional characters makes “first result per position” explicit.

## First idea

I scan indices once, ignore hashes without five leading zeroes or with an invalid/already-filled position, and stop as soon as every position has a character.

## Wrong turns

There were no wrong turns. I do not overwrite filled positions, and I reject positions outside `0` through `7`. The real search completed after 26,383,110 indices.

## Algorithmic concept

This is an **ordered sparse fill**: a stream of rare witnesses fills a fixed array, preserving the first witness for each position.

## Complexity

For `n` tested indices and password length `k`, runtime is **O(n)** MD5 computations and storage is **O(k)**. The implementation retains only the eight output slots, never the rejected digests.

The full MD5 search is intentionally bounded by an optional index limit in the function. The browser page runs only a reduced demonstration so it stays responsive.
