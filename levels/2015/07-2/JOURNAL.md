# 2015 Day 7, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/7). I read Part 2 only.

## First idea

Part 2 changes the circuit in two passes: first evaluate wire `a` with the Part 1 circuit, then replace wire `b` with that signal and reset every other wire before evaluating `a` again. I reuse the Part 1 evaluator for both passes; the Part 2 wrapper materializes the instructions once so it can evaluate the original circuit and build the rewired one without consuming a one-shot input twice.

## Wrong turns

I considered adding a special case inside the recursive evaluator for wire `b`. That would mix the Part 2 reset rule into the general circuit semantics and make the first pass harder to reason about. Keeping the override as a separate transformed instruction list leaves the existing 16-bit evaluator unchanged and makes the two passes explicit. I did not submit any wrong answer.

## Public examples

The Part 1 evaluator is checked against representative wires from the published example. A small circuit checks that Part 1's signal replaces `b`, and a one-shot iterable checks that materializing the instructions preserves the two-pass behavior.

## Complexity

The wrapper makes two circuit evaluations and one instruction-list rewrite. With **W** wires and **D** reachable dependencies, this takes **O(W + D)** time and **O(W)** space; the evaluator's memoization prevents repeated dependency work within each pass.

## Submission

I ran the tested solution on my own input; it returned `40149`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 7 Part 2 is therefore complete.
