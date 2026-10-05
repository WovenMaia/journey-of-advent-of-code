# 2016 Day 17, Part 2

**Status:** solved (05/10/2026). The three published longest-path examples pass, and the real passcode runs locally.

## Real input and submission

The local result is `526`; I did not submit an answer during this session. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/17). In my words: continue exploring every hash-controlled route, then report the length of the longest route that reaches the vault.

## Why Python

The same standard-library breadth-first search as Part 1 keeps the path-dependent door rule visible.

## First idea

Do not stop at the first goal. Record every goal path length, do not expand goal states, and keep the maximum.

## Wrong turns

There was no separate Part 2 input format or new puzzle example. The three published passcodes exercise both branching and the need to continue after the first successful route.

## Algorithmic concept

This is **complete search with terminal-state aggregation**. Reaching the vault ends one route, while other queued states may still produce a longer route.

## Complexity

The state count is finite for the four-by-four vault but can be much larger than Part 1 because all successful routes are explored. Each state stores its path and one MD5 digest is computed per non-terminal state.
