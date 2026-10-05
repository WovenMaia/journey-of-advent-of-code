# 2016 Day 25, Part 1

**Status:** staged (05/10/2026). The public alternating signal checks pass. The real input is pending because the Advent of Code session is unavailable.

## Real input and submission

No real input result is recorded yet. I did not submit an answer. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/25). In my words: find the lowest positive register value that emits an endless alternating clock signal.

## Why Python

The assembunny program is small, and a bounded interpreter makes each candidate's signal observable without storing an unbounded stream.

## First idea

Try positive candidates in order. Stop a candidate as soon as it emits a repeated or out of range value, and accept it after a fixed prefix of alternating bits.

## Wrong turns

There was no wrong algorithmic turn. The tests cover a looping alternating program, repeated output, out of range output, and the register seed.

## Algorithmic concept

This is **counterexample guided search**. A candidate survives only while its generated prefix agrees with the clock invariant.

## Complexity

For `k` checked signal bits, each candidate uses O(k) retained output and bounded interpreter time. The search cost is O(k times the number of candidates examined).
