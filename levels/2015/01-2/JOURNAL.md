# 2015 Day 1, Part 2

**Status:** solved (30/09/2026).

## Real input and submission

I ran the staged solution on my own input; it returned `1771`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Part 2 is therefore solved.

## Why it is available now

Part 1 ran on my own input and Advent of Code accepted the submitted answer. Only then did I open Part 2 on the site and read its prompt.

## First idea

I will keep the same running floor, but stop immediately when it first reaches the basement. The answer is the instruction's one-based position, so enumeration begins at one.

## Public examples

The site shows that `)` enters the basement at position `1`, while `()())` does so at position `5`. The tests also cover an instruction stream that never reaches the basement and malformed input.

## Completion

The public examples, real-input run, and accepted one-time submission now all agree: this level is solved.
