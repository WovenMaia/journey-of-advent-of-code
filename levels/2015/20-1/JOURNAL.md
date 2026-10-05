# 2015 Day 20, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/20).

## First idea

I used a sieve: each elf adds ten times its number to every multiple in one pass, then the first house over the target is selected.

## Wrong turns

There were no wrong turns.

## Public examples

The tests check the first house and the example house 4 total.

## Complexity

With target $T$, the sieve uses $O(T)$ space and $O(T\log T)$ additions.
