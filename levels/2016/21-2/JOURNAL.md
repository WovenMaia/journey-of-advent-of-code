# 2016 Day 21, Part 2

**Status:** staged (05/10/2026). The published example passes. The real input is pending because the Advent of Code session is unavailable.

## Real input and submission

No real input result is recorded yet. I did not submit an answer. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/21). In my words: reverse the same edits to recover the original password.

## Why Python

The inverse of each operation is direct except the position based rotation, whose short password domain makes a candidate search simple and reliable.

## First idea

Walk the instructions backwards. Move, rotate, swap, and reverse have obvious inverses. For the position based rule, try every possible left rotation and keep the candidate whose forward transformation matches the current string.

## Wrong turns

There was no wrong algorithmic turn. The published example and focused inverse checks cover the reversible operations and the ambiguous rotation.

## Algorithmic concept

This is **inverse interpretation**. Reversing a program's steps turns a forward transformation into a decoder.

## Complexity

For `n` letters and `m` instructions, the candidate search costs O(mn squared) in the worst case and uses O(n) working memory.
