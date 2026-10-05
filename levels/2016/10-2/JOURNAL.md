# 2016 Day 10, Part 2

**Status:** solved (05/10/2026). The published output example passes, and I ran the full instruction stream before submitting once.

## Real input and submission

Outputs 0, 1, and 2 contain values whose product is `4042`. I submitted `4042` once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 2 is solved and Day 10 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/10). In my words: run the same bot network, record output bins, and multiply the first three outputs.

## Why Python

The Part 1 event loop already models the network; this version records output destinations as terminal events.

## First idea

Reuse the ready-bot queue, sort each pair once, send each chip to its configured bot or output, and multiply outputs after the queue drains.

## Wrong turns

There were no wrong submissions. I waited for all three output bins rather than assuming the first three events were the answer.

## Algorithmic concept

This is **event-driven simulation with sinks**: bots are transient actors and output bins are persistent terminal state.

## Complexity

For `n` instructions and `b` bots, parsing and processing are **O(n + b)** time and **O(n + b)** space.
