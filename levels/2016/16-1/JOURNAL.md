# 2016 Day 16, Part 1

**Status:** solved (05/10/2026). The published dragon-curve example passes, and the real disk checksum completed locally.

## Real input and submission

The checksum is `10111110010110110`. I did not submit an answer during this session; this journal records the local result only.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/16). In my words: grow a binary dragon-curve string until it fills a 272-bit disk, then repeatedly compare adjacent pairs to produce an odd-length checksum.

## Why Python

Strings make the reverse-and-invert expansion and pairwise checksum reduction easy to read for this small Part 1 disk.

## First idea

Implement the expansion literally: append `0` and the reversed, inverted copy. Truncate at the disk length, then reduce equal pairs to `1` and unequal pairs to `0` until the checksum length is odd.

## Wrong turns

There were no wrong submissions. The easy-to-miss detail is to keep reducing the checksum while its length is even, rather than stopping after one pass.

## Algorithmic concept

This is **deterministic sequence expansion with reduction**. The dragon rule defines the data, and checksum passes preserve only pair agreement.

## Complexity

For disk size `n`, the generated data uses **O(n)** space. Expansion and checksum reduction together take **O(n)** time up to the constant number of halving passes.
