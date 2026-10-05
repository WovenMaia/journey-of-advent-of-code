# 2016 Day 24, Part 1

**Status:** staged (05/10/2026). The published example passes. The real input is pending because the Advent of Code session is unavailable.

## Real input and submission

No real input result is recorded yet. I did not submit an answer. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/24). In my words: visit every numbered location in the shortest possible route.

## Why Python

Breadth first search gives exact distances through the map, and a small permutation search chooses the best order of visits.

## First idea

Find every numbered point, run a breadth first search from each one, then sum pairwise distances for every ordering that starts at zero.

## Wrong turns

There was no wrong algorithmic turn. The published map, a single target, and the missing origin check cover the route boundaries.

## Algorithmic concept

This is **metric closure plus permutation search**. The maze becomes a complete weighted graph over points of interest before route ordering begins.

## Complexity

For `v` points and `c` map cells, distance searches cost O(vc), and route enumeration costs O(v factorial).
