# 2016 Day 5, Part 1

**Status:** solved (05/10/2026). The public example passes, and I ran the bounded MD5 search on my own input before submitting its result once.

## Real input and submission

The solution printed `c6697b55` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to another.” Part 1 is therefore solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/5). In my words: scan MD5 hashes of the door ID with increasing indices and take the sixth hex character from hashes beginning with five zeroes.

## Why Python

Python's standard `hashlib` gives a direct, dependency-free MD5 implementation and keeps the search loop visible.

## First idea

I hash `door_id + index` in order, accept only digests with the required five-zero prefix, and append their sixth characters until eight positions are filled.

## Wrong turns

There were no wrong turns. The search is intentionally bounded by an optional index limit in the function and by a documented, finite local run; the real puzzle search completed after 5,833,678 indices.

## Algorithmic concept

This is a **proof-by-filtered-enumeration** search: every candidate is generated in the prescribed order, then a cheap prefix predicate selects the rare witnesses.

## Complexity

For `k` accepted characters and `n` tested indices, the runtime is **O(n)** MD5 computations and the result storage is **O(k)**. The implementation does not retain rejected hashes.
