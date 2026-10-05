# 2016 Day 2, Part 1

**Status:** solved (05/10/2026). The public examples pass, and I ran the solution on my own input before submitting its result once.

## Real input and submission

The solution printed `97289` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 1 is therefore solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/2). In my words: follow one line of directional moves per code button, ignoring moves that leave the keypad.

## Why Python

I kept Python because a dictionary of valid coordinates makes the keypad boundary explicit while the movement loop stays small and readable.

## First idea

I model each button as a coordinate and each direction as a one-step vector. For each instruction line I try every move, committing only candidates that are present in the keypad map, then record the button reached at the end of the line.

## Wrong turns

There were no wrong turns. Empty lines are ignored and every non-empty line is validated before it can alter the keypad state.

## Algorithmic concept

This is a **constrained state walk**. The current button is state, each direction is a transition, and the keypad map defines which transitions are legal.

## Complexity

For `m` moves across all instruction lines, the algorithm takes **O(m)** time and **O(1)** auxiliary space besides the output code.
