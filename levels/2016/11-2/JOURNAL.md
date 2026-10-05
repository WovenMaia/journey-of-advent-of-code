# 2016 Day 11, Part 2

**Status:** solved (05/10/2026). The reduced three-pair check passes, and the canonical breadth-first search finished on my real input before submitting once.

## Real input and submission

Adding the two new pairs changes the minimum to `57` steps. I submitted `57` once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 2 is solved and Day 11 is complete.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/11). In my words: solve the expanded paired-item transport problem with the same safety rules and elevator capacity.

## Why Python

Part 2 reuses the same canonical state representation and search discipline while adding the two pairs at floor one.

## First idea

Keep the Part 1 transition engine, add the two extra `(generator, chip)` pairs to the initial state, and let BFS prove the shortest route.

## State pruning

Pair names are erased by sorting pair locations, downward moves are skipped when no item is below the elevator, and unsafe candidate floors never enter `seen`. This prevents equivalent label permutations and pointless descents from multiplying the queue. The real search completed in about 2.6 seconds locally.

The site deliberately uses a **reduced demo** rather than running the seven-pair search in a browser button: a full search would freeze the reader's page. The page explains the pruning and animates a small state transition instead.

## Wrong turns

There were no wrong submissions. The only adjustment was keeping the public page's demonstration small while leaving the real solver exact.

## Algorithmic concept

This is **optimal state-space search with symmetry reduction**. BFS's first all-on-floor-four state is the minimum number of stops.

## Complexity

The finite canonical state space grows exponentially with the number of pairs; BFS stores the reachable safe states and their frontier rather than any expanded physical history.
