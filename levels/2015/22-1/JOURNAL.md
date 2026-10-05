# 2015 Day 22, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/22).

## First idea

I represented timers and resources in an immutable state and used a best-first search by spent mana. Effects are applied at both turn starts, and dominated states are pruned.

## Wrong turns

There were no wrong turns.

## Public examples

The tests cover both published fights: 226 and 641 mana.

## Complexity

The search is finite under the mana and best-cost bounds; the visited map keeps one cheapest cost per combat state.
