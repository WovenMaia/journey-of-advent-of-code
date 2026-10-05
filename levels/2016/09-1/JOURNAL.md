# 2016 Day 9, Part 1

**Status:** solved (05/10/2026). The published examples pass, and I measured the real input before submitting once.

## Real input and submission

The one-level decompressed length is `107035`. I submitted it once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 1 is solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/9). In my words: parse `(length x repeats)` markers, repeat exactly that many following characters, and report the resulting length without materializing the expanded string.

## Why Python

A cursor and a regular expression make the marker boundaries explicit while the calculation stores only a running length.

## First idea

Remove whitespace, scan left to right, and add either one literal character or the marker's `length × repeats` contribution before jumping over its payload.

## Wrong turns

There were no wrong submissions. The important distinction was that payload markers are treated as ordinary characters in Part 1.

## Algorithmic concept

This is **streaming parsing**: each marker is consumed once and contributes directly to the answer.

## Complexity

For `n` non-whitespace characters, the scan uses **O(n)** time and **O(n)** input storage, with no decompressed-output allocation.
