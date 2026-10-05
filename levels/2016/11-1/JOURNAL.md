# 2016 Day 11, Part 1

**Status:** solved (05/10/2026). The published four-floor example passes, and the breadth-first search finished on my real input before submitting once.

## Real input and submission

The minimum is `33` elevator steps. I submitted `33` once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 1 is solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/11). In my words: move paired generators and chips through four floors with a two-item elevator while never leaving a chip exposed to another generator.

## Why Python

A compact tuple state makes breadth-first search straightforward and keeps the visited set hashable.

## First idea

Generate every one- or two-item elevator move, reject unsafe floors, and search by distance until every pair reaches floor four.

## State pruning

Each state canonicalizes the generator/chip pairs by sorting them, so swapping element names does not create duplicate work. Downward moves are omitted when no item remains below the elevator; every candidate is also checked against the generator-safety rule before entering the queue. The real search visited a bounded finite state space and completed in a fraction of a second locally.

## Wrong turns

There were no wrong submissions. The key correctness check was validating the destination state after every move, including chips temporarily separated from their generators.

## Algorithmic concept

This is **breadth-first search over a canonical state space**: the first goal state dequeued is optimal because every elevator ride costs one.

## Complexity

With `p` pairs, the canonical state space is finite (at most `4 × 4^(2p)` arrangements before safety pruning); BFS uses time and memory proportional to the reachable states.
