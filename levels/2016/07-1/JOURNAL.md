# 2016 Day 7, Part 1

**Status:** solved (05/10/2026). The public examples pass, and I ran the classifier on my own input before submitting its result once.

## Real input and submission

The solution counted `105` TLS-supporting addresses. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to another.” Part 1 is solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/7). In my words: count addresses containing an ABBA outside brackets but none inside hypernet sequences.

## Why Python

String slicing and `zip` make the four-character symmetry test readable, while a small parser keeps bracket context explicit.

## First idea

Split each address into alternating supernet and hypernet sequences, search every sequence for a non-palindromic ABBA, and apply the outside/inside predicate.

## Wrong turns

There were no wrong turns. `aaaa` is rejected because the paired characters must differ, and an ABBA inside any bracketed sequence vetoes the address.

## Algorithmic concept

This is a **context-sensitive pattern predicate**: the same local motif has different meaning depending on which parsed region contains it.

## Complexity

For total address length `n`, classification is **O(n)** time and **O(n)** space for the parsed sequences.
