# 2015 Day 21, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/21).

## First idea

I enumerated exactly one weapon, zero or one armor, and zero through two distinct rings, then compared turn counts for every loadout.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover the stated combat numbers and boss parser.

## Complexity

There are only $5\times6\times(1+6+15)$ loadouts, each checked in constant time.
