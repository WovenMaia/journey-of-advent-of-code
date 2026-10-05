# 2016 Day 16, Part 2

**Status:** solved (05/10/2026). The published dragon-curve example still passes, and the 35,651,584-bit real disk completed locally.

## Real input and submission

The checksum is `01101100001100100`. I did not submit an answer during this session; this journal records the local result only.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/16). In my words: use the same dragon-curve and checksum rules, but fill a 35,651,584-bit disk.

## Why Python

The standard-library string operations keep the rule visible. The implementation expands only until the requested length and truncates before reducing the checksum.

## First idea

Keep the Part 1 algorithm, change only the target disk size, and use a direct reverse-and-invert operation so the large expansion stays simple.

## Wrong turns

There was no separate Part 2 example with the large disk size. I kept the published `10000`/20-bit example as a regression check and verified the large real disk locally instead of pretending the small example exercises the full size.

## Algorithmic concept

This is **deterministic sequence expansion with reduction**. The same dragon transform works at either disk size; only the amount of generated data changes.

## Complexity

For disk size `n`, the generated data uses **O(n)** space. Expansion and checksum reduction together take **O(n)** time up to the constant number of halving passes.
