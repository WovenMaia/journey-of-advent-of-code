# 2015 Day 22, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/22).

## First idea

I kept the best-first spell-state search and applied hard mode's one hit point loss before every player-turn effect. States that cannot survive the penalty or boss turn are discarded immediately.

## Wrong turns

There were no wrong turns.

## Public examples

The tests exercise the low-health hard-mode rule and a normal starting state with a winning path.

## Complexity

The visited-state map and current best mana bound prune the finite spell search.
