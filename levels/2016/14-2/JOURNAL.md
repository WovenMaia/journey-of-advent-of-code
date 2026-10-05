# 2016 Day 14, Part 2

**Status:** solved (05/10/2026). The stretched-hash primitive passes its published digest check, the cached full search finished locally in about 60 seconds, and I submitted once.

## Real input and submission

After re-hashing each digest 2016 additional times, the 64th key is at index `20092`. I submitted `20092` once. Advent of Code replied: “You got the second star! You are one gold star closer to fixing the sleigh.” Part 2 is solved and Day 14 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/14). In my words: apply the same one-time-pad rule after key stretching every MD5 digest 2016 times.

## Why Python

The standard-library MD5 implementation keeps the hot loop dependency-free. The cache is essential because every candidate shares most of its thousand-hash look-ahead with nearby candidates.

## First idea

Reuse the Part 1 stream search, but stretch each digest before looking for its first triple and cache the results by index.

## Wrong turns

There were no wrong submissions. A full browser-side run would freeze the reader, so the site intentionally uses a reduced one-key demonstration and says so rather than pretending to run the full search.

## Algorithmic concept

This is **memoized streaming search under a deterministic transform**. Stretching changes the hash stream but not the candidate/key proof.

## Complexity

For final index `k`, at most `k+1000` hashes are cached, each requiring 2017 MD5 rounds. Search time is **O(k·w·r)** for look-ahead width `w=1000` and rounds `r=2017`; memory is **O(k+w)**.
