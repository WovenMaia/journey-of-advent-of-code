# 2015 Day 8, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/8). I read Part 1 only.

## First idea

Each input line is a quoted string literal. I count its code characters directly, then scan between the outer quotes to count the in-memory characters: an ordinary character consumes one source character, `\\` and `\"` each consume two source characters but represent one character, and `\x` plus two hexadecimal digits consumes four source characters but represents one character. The answer is the sum of code length minus memory length for every line.

## Wrong turns

I considered using Python's string-literal evaluator, but that would accept escape forms outside this puzzle's language and make the counting rules implicit. The small explicit scanner validates the three permitted escape forms and keeps code length separate from decoded length. I did not submit any wrong answer.

## Public examples

The tests cover the four published literals and their total difference of `12`, plus combined backslash, quote, and hexadecimal escapes. They also check that input line endings are ignored and malformed hexadecimal escapes are rejected.

## Complexity

For **N** source characters across all lines, the scanner takes **O(N)** time and **O(1)** extra space besides the input iterator.

## Submission

I ran the tested solution on my own input; it returned `1350`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 8 Part 1 is therefore complete; Day 8 Part 2 is next.
