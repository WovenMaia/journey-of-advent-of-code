# 2016 Day 20, Part 1

**Status:** solved (05/10/2026). The published firewall example passes, and the real blacklist runs locally.

## Real input and submission

The local result is `14975795`; I did not submit an answer during this session. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/20). In my words: given blocked inclusive IP ranges, find the smallest address that is not blocked.

## Why Python

Sorting the ranges and sweeping one candidate address keeps the interval invariant visible and handles overlaps without expanding individual addresses.

## First idea

Start at zero. Every range beginning at or before the candidate extends the blocked frontier; the first range beginning after it exposes the answer.

## Wrong turns

There was no wrong algorithmic turn. The public example, overlapping ranges, adjacent ranges, and a fully blocked bounded space cover the sweep boundaries.

## Algorithmic concept

This is **interval union scanning**. Sorted ranges reduce the question to finding the first gap in the merged coverage.

## Complexity

For `m` ranges, sorting costs O(m log m), the sweep costs O(m), and the range list uses O(m) memory.
