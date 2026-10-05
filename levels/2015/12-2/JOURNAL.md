# 2015 Day 12, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/12).

## First idea

Part 2 keeps the JSON structure from Part 1 but changes how objects contribute: an object with any property whose value is the string `"red"` contributes nothing, including all descendants. Arrays are still traversed normally, even when they contain the string `"red"`. I decode the document with Python's standard-library `json` module and apply that rule during one recursive walk.

## Wrong turns

I first considered summing everything as in Part 1 and trying to subtract red sections afterward. That would lose the object boundaries needed to exclude an entire subtree. The parser-based recursive walk makes the exclusion happen before visiting an object's children, so I kept that approach. I did not submit a wrong answer.

## Public examples

The tests cover all four published examples, nested red objects, red strings inside arrays, and a property named `red` whose value is not red. That last case protects the distinction between property names and property values.

## Complexity

Let **N** be the number of decoded JSON values. The traversal visits each value at most once, so it takes **O(N)** time and **O(D)** call-stack space, where **D** is the maximum nesting depth.

The tested solution returned `96852` for my real input. I submitted that value once for Part 2. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 12 Parts 1 and 2 are therefore complete; Day 13 Part 1 is next.