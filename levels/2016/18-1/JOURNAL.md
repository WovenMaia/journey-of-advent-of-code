# 2016 Day 18, Part 1

**Status:** solved (05/10/2026). Both published row-count examples pass, and the real 40-row input runs locally.

## Real input and submission

The local result is `1926`; I did not submit an answer during this session. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/18). In my words: generate rows of traps from neighboring tiles and count safe tiles over forty rows.

## Why Python

A short string transformation makes the neighbor rule obvious and keeps only the current row in memory.

## First idea

Pad each row with safe sentinels. A tile is a trap exactly when its left and right neighbors differ; count dots before producing the next row.

## Wrong turns

There was no wrong algorithmic turn. The two public examples cover both the compact three-row and ten-row cases.

## Algorithmic concept

This is **cellular automaton iteration**. The next row is a deterministic local transform of the current row, with edge sentinels representing safe space beyond the hallway.

## Complexity

For width `w` and `r` rows, the algorithm uses O(w) memory and O(wr) time.
