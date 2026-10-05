# 2016 Day 15, Part 1

**Status:** solved (05/10/2026). The published two-disc example passes, and the real disc schedule finished before the first submission.

## Real input and submission

The earliest button time is `148737`. I submitted `148737` once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 1 is solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/15). In my words: find the first integer time at which a capsule reaches every disc while its slot is at position zero.

## Why Python

The input is tiny and the direct congruence check mirrors the timing rule without hiding the capsule's one-second-per-disc offset.

## First idea

Try button times from zero upward. For disc number `n`, its position when reached is `(initial + time + n) % positions`; every disc must equal zero.

## Wrong turns

There were no wrong submissions. The only easy-to-miss detail is that disc numbering starts at one because the first disc is reached one second after pressing the button.

## Algorithmic concept

This is **constraint search over modular congruences**. The first satisfying timestamp is the answer, and checking times in order preserves minimality.

## Complexity

For `t` tested timestamps and `d` discs, runtime is **O(t·d)** and extra space is **O(d)** for the parsed schedule.
