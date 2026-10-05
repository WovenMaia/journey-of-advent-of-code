# 2016 Day 10, Part 1

**Status:** solved (05/10/2026). The published bot example passes, and I ran the full instruction stream before submitting once.

## Real input and submission

Bot `98` compares the 17 and 61 chips. I submitted `98` once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 1 is solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/10). In my words: route chips through bots that act whenever they hold two, and identify the bot handling the target pair.

## Why Python

A queue of ready bots mirrors the factory's event-driven rules and avoids repeatedly scanning every bot.

## First idea

Parse value assignments and routing rules, enqueue a bot as soon as it receives its second chip, then process low and high values in order.

## Wrong turns

There were no wrong submissions. I kept output bins out of Part 1's answer because only the comparison event matters here.

## Algorithmic concept

This is **event-driven simulation**: each ready bot consumes one queued event and may trigger another.

## Complexity

For `n` instructions and `b` bots, parsing and processing are **O(n + b)** time and **O(n + b)** space.
