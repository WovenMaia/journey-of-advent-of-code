# 2016 Day 17, Part 1

**Status:** solved (05/10/2026). The three published path examples pass, and the real passcode runs locally.

## Real input and submission

The local result is `RDURRDDLRD`; I did not submit an answer during this session. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/17). In my words: use an MD5 hash to decide which doors are open while finding the shortest route through a four-by-four vault.

## Why Python

`hashlib` and `collections.deque` make the hash-driven breadth-first search direct and readable.

## First idea

Treat each `(x, y, path)` as a state. Hash the passcode plus path, enqueue open in-bounds doors, and return the first state reaching the lower-right room.

## Wrong turns

There was no wrong algorithmic turn. I kept the unreachable `hijkl` example as a guard that the search may legitimately return no route.

## Algorithmic concept

This is **breadth-first search over an implicit graph**. The hash changes the outgoing edges at every state, but queue order still proves the first goal path is shortest.

## Complexity

For a fixed four-by-four grid, the explored state count is finite but paths may revisit rooms with different hashes. Each state uses O(1) extra data beyond its path, and each expansion computes one MD5 digest.
