# 2015 Day 7, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/7). I read Part 1 only.

## First idea

I parse each assignment into a destination wire and an expression, then resolve only the requested wire. Resolution follows dependencies recursively, memoizing each wire after its value is known; this gives dependency order without repeatedly scanning the instruction list. Every result is masked with `0xffff`, so signals behave as unsigned 16-bit values, including the complement and left-shift operations.

## Wrong turns

I briefly considered repeatedly walking the instruction list until no more wires could be filled. That would work for an acyclic input, but it would rescan already resolved expressions and would need a separate failure case for unresolved cycles. Dependency resolution with a memo is both direct and explicit about undefined or cyclic wires. I did not submit any wrong answer.

## Public examples

The tests cover the complete public wire example, forward references, and the 16-bit behavior needed for complements and shifts. They assert each named result from the example rather than only checking the final target.

## Complexity

Parsing stores **O(number of wires)** expressions. Resolving a target visits each dependency at most once, so evaluation is **O(number of reachable wires)** time and space, with memoized values preventing duplicate work.

## Submission

I ran the tested solution on my own input; it returned `956`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 7 Part 1 is therefore complete.
