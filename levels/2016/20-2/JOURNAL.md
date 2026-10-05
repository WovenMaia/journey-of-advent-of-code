# 2016 Day 20, Part 2

**Status:** solved (05/10/2026). The published firewall count example passes, and the real blacklist runs locally.

## Real input and submission

The local result is `101`; I did not submit an answer during this session. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/20). In my words: count every address not covered by the blocked ranges across the full 32-bit space.

## Why Python

The sorted interval sweep from Part 1 naturally becomes a gap counter, without enumerating billions of addresses.

## First idea

Keep a candidate frontier. Add each gap before the next range, merge overlap by advancing the frontier, and add the tail after the last range.

## Wrong turns

There was no wrong algorithmic turn. The public example, overlapping ranges, and a fully blocked bounded space check both gap boundaries and the zero-count case.

## Algorithmic concept

This is **measure of an interval complement**. Sorting turns the union of blocked intervals into a linear scan whose gaps are exactly the allowed addresses.

## Complexity

For `m` ranges, sorting costs O(m log m), the sweep costs O(m), and the range list uses O(m) memory.
