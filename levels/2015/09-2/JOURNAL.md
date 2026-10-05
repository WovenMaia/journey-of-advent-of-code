# 2015 Day 9, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/9).

## First idea

Part 2 keeps the same route model as Part 1 and changes only the objective: enumerate every permutation of the locations and keep the largest route distance instead of the smallest. The parser and undirected distance representation are reused exactly so the two parts describe the same graph.

## Wrong turns

I briefly considered reversing the Part 1 result or selecting the locally most expensive next edge. Neither works in general: reversing preserves a route's distance, and a greedy choice can block the globally longest route. I did not submit a wrong answer.

## Public examples

The tests include the published three-location example, line-ending handling, blank-line handling, one-shot iterables, and rejection of malformed distance records.

## Complexity

For **V** locations and a complete distance graph, enumeration takes **O(V! × V)** time and **O(V)** extra space for each route beyond the parsed graph.

## Submission

The tested solution returned `804` for my real input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 9 Part 2 is therefore complete; Day 10 Part 1 is next.
