# 2015 Day 1, Part 2

**Status:** staged (30/09/2026).

## Why it is available now

Part 1 ran on my own input and Advent of Code accepted the submitted answer. Only then did I open Part 2 on the site and read its prompt.

## First idea

I will keep the same running floor, but stop immediately when it first reaches the basement. The answer is the instruction's one-based position, so enumeration begins at one.

## Public examples

The site shows that `)` enters the basement at position `1`, while `()())` does so at position `5`. The tests also cover an instruction stream that never reaches the basement and malformed input.

## Submission boundary

The implementation and public examples are staged, but I have not run Part 2 on my real input or submitted an answer. Its status stays **staged** until both happen.
