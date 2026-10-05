# 2016 Day 4, Part 2

**Status:** solved (05/10/2026). The public examples pass, and I ran the solution on my own input before submitting its result once.

## Real input and submission

The solution printed `324` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 2 is therefore solved, and Day 4 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/4). In my words: decrypt each real room by rotating letters by its sector ID and find the room storing North Pole objects.

## Why Python

Python's character arithmetic makes the Caesar rotation explicit, while the Part 1 checksum predicate can be reused to exclude decoy rooms before decryption.

## Why it is available now

Part 1 ran on my own input and Advent of Code accepted the submitted answer. Only then did I open Part 2 and read its prompt.

## First idea

I rotate each lowercase letter modulo 26, turn dashes into spaces, and search only decrypted real rooms for the North Pole marker. The input has one matching room, so its sector ID is the answer.

## Wrong turns

There were no wrong turns. I filtered by the checksum before searching decrypted names, so a decoy that happens to contain a suggestive phrase cannot win.

## Algorithmic concept

This is a **filter-transform-search** pipeline: validate identity, apply a reversible character transform, then select the unique matching record.

## Complexity

For `n` rooms and `c` total name characters, the algorithm takes **O(c log a)** time for checksum ordering plus **O(c)** decryption/search time, with **O(a)** auxiliary space per room.
