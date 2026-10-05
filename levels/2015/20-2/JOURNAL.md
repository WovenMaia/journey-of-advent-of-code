# 2015 Day 20, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/20).

## First idea

I kept the sieve but limited each elf to its first fifty house visits and changed the delivery multiplier to eleven.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover the first house and the first target that requires house 8.

## Complexity

With target $T$, the bounded sieve uses $O(T)$ space and at most $O(T\log T)$ additions.
