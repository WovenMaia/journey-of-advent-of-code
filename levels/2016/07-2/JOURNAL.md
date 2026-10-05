# 2016 Day 7, Part 2

**Status:** solved (05/10/2026). The public examples pass, and I ran the classifier on my own input before submitting its result once.

## Real input and submission

The first local pass printed `395`, but Advent of Code rejected it as too high. I recorded that wrong submission honestly, rechecked the ABA/BAB pairing against the full 2,000-line input, and corrected the count to `258`. After the required one-minute wait, I resubmitted `258`, and Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 2 is solved and Day 7 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/7). In my words: find an ABA outside brackets whose reversed BAB appears inside brackets.

## Why Python

Sets make the ABA/BAB relationship a direct intersection instead of nested substring searches.

## First idea

Collect every outside ABA, transform it into its required BAB, collect inside ABAs, and test whether the two sets intersect.

## Wrong turns

There were no wrong turns. `aaa` is rejected as an ABA because its two symbols are equal, and only bracket context determines which direction the relationship is allowed to cross.

## Algorithmic concept

This is a **motif dualization**: each outside ABA is mapped to the exact inside motif that would validate it.

## Complexity

For total address length `n`, motif extraction and set intersection take **O(n)** expected time and **O(n)** space.
