# 2016 Day 21, Part 1

**Status:** staged (05/10/2026). The published example passes. The real input is pending because the Advent of Code session is unavailable.

## Real input and submission

No real input result is recorded yet. I did not submit an answer. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/21). In my words: apply a sequence of string edits to scramble `abcdefgh`.

## Why Python

Each instruction is a small list transformation, and Python makes the index and slice operations explicit.

## First idea

Parse each instruction with a full match, then mutate a list of letters. Rotations normalize their distance so examples also cover distances larger than the password.

## Wrong turns

There was no wrong algorithmic turn. The public example and individual operation checks cover swaps, movement, reversal, and both rotation forms.

## Algorithmic concept

This is **reversible string rewriting**. Every instruction changes one local property of an ordered sequence while preserving the letters.

## Complexity

For `n` letters and `m` instructions, the implementation uses O(mn) time and O(n) working memory.
