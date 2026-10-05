# 2015 Day 12, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/12).

## First idea

The input is one JSON document, so I decode it with Python's standard-library `json` module and recursively visit the resulting arrays and objects. Numbers contribute their value; strings and the container structure contribute nothing. This naturally handles negative values and arbitrary nesting without scanning text that may belong to strings.

## Wrong turns

I considered extracting signed integers with a regular expression, but that would risk counting digits inside JSON strings and would ignore the document structure. I kept the parser-based approach instead. I did not submit a wrong answer.

## Public examples

The tests cover every published example, including nested arrays and objects, negative numbers, empty containers, and the fact that digits inside strings are not numbers in the document.

## Complexity

Let **N** be the number of decoded JSON values. The traversal visits each value once, so it takes **O(N)** time and **O(D)** call-stack space, where **D** is the maximum nesting depth.
The tested solution returned `156366` for my real input. I submitted that value once for Part 1. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 12 Part 1 is complete; Day 12 Part 2 is next.
