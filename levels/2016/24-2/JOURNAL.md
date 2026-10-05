# 2016 Day 24, Part 2

**Status:** staged (05/10/2026). The published example passes. The real input is pending because the Advent of Code session is unavailable.

## Real input and submission

No real input result is recorded yet. I did not submit an answer. The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/24). In my words: visit every location and return to zero using the shortest route.

## Why Python

The distance graph from Part 1 is reusable. Part 2 changes only the route objective by appending the return edge to zero.

## First idea

Measure every pair of points with breadth first search, enumerate target orders, and add the final distance from the last target back to zero.

## Wrong turns

There was no wrong algorithmic turn. The published map, a single target round trip, and the missing origin check cover the changed objective.

## Algorithmic concept

This is **a travelling salesperson tour on a maze metric**. The return edge closes each candidate path into a cycle.

## Complexity

For `v` points and `c` map cells, distance searches cost O(vc), route enumeration costs O(v factorial), and memory is O(c plus v squared).
