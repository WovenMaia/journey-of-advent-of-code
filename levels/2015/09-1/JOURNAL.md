# 2015 Day 9, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/9).

## First idea

The input gives one distance for every pair of locations. I parse each line into an undirected edge, collect the locations, then enumerate every permutation as a possible route. Each route visits every location exactly once; the minimum sum of its consecutive edges is the answer.

## Wrong turns

I first considered choosing the locally cheapest next edge. That greedy approach can leave an expensive final connection and does not guarantee the shortest Hamiltonian path, so I replaced it with exhaustive route enumeration. I did not submit a wrong answer.

## Public examples

The tests include the published three-location example, line-ending handling, blank-line handling, one-shot iterables, and rejection of malformed distance records.

## Complexity

For **V** locations and a complete distance graph, enumeration takes **O(V! × V)** time and **O(V)** extra space for each route beyond the parsed graph.

## Submission

I ran the tested solution on my own input; it returned `207`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 9 Part 1 is therefore complete; Day 9 Part 2 is next.
