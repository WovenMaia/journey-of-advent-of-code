# 2016 Day 14, Part 1

**Status:** solved (05/10/2026). The published `abc` first-key example passes, the hash cache keeps the look-ahead work bounded, and the real salt finished before submitting once.

## Real input and submission

The 64th key is at index `18626`. I submitted `18626` once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 1 is solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/14). In my words: hash a salt with increasing indices and accept a hash when its first triple is followed within 1000 hashes by a matching quintuple.

## Why Python

`hashlib` supplies the exact MD5 primitive, and a list cache makes each future hash available once to both the candidate scan and its look-ahead window.

## First idea

Scan indices in order, detect only the first triple in each hash, then inspect the next thousand cached-or-new hashes for five matching characters.

## Wrong turns

There were no wrong submissions. The subtle rule is that a hash's first triple alone matters; later triples in that same hash do not create additional candidates.

## Algorithmic concept

This is **memoized streaming search**: the candidate order is sequential, while caching turns overlapping 1000-hash look-ahead windows into one computation per index.

## Complexity

If the final key is at index `k`, at most `k+1000` hashes are computed and stored. Search time is **O(k·w)** for `w=1000` substring checks, plus MD5 cost; memory is **O(k+w)**.
