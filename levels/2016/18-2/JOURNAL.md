# 2016 Day 18, Part 2

**Status:** solved (05/10/2026). The published examples still pass, and the 400,000-row real input runs locally.

## Real input and submission

The local result is `19986699`; I did not submit an answer during this session. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/18). In my words: keep the same row rule but count safe tiles over 400,000 rows.

## Why Python

The current-row string is enough state; no large grid needs to be retained.

## First idea

Carry the Part 1 recurrence over the larger row count without changing the rule. Count each row before replacing it, so the memory stays bounded by the hallway width.

## Wrong turns

There is no distinct large-row public example. I reused both published Part 1 examples as regression checks and verified the full 400,000-row input locally.

## Algorithmic concept

This is **streaming cellular-automaton reduction**: each row is consumed once for its safe count and replaced by its deterministic successor.

## Complexity

For width `w` and `r` rows, the algorithm uses O(w) memory and O(wr) time; the larger row count changes runtime, not the state representation.
