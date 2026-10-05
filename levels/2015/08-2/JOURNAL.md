# 2015 Day 8, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/8). I read Part 2 after completing Part 1.

## First idea

The new representation wraps each original code literal in a pair of quotes. Every quote and backslash already present in the code must be escaped once in that representation, so its length is the original code length plus two surrounding quotes plus one character for each existing quote or backslash. Summing that increase over the input gives the answer without decoding the strings or building replacement strings.

## Wrong turns

I first checked the examples by manually spelling out their encoded forms. That is useful for confirming the rule, but it is unnecessary work for the full input and risks confusing source characters with memory characters. The final solution counts the characters directly. I did not submit any wrong answer.

## Public examples

The tests cover the four published literals and their total encoded-minus-original difference of `19`. They also cover a literal containing both backslashes and an escaped quote, ignore line endings, and reject an unquoted value.

## Complexity

For **N** source characters across all lines, the calculation takes **O(N)** time and **O(1)** extra space besides the input iterator.

## Submission

I ran the tested solution on my own input; it returned `2085`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 8 Part 2 is therefore complete; Day 9 Part 1 is next.
