# 2015 Day 1, Part 1

**Status:** solved (30/09/2026). The public examples pass, and I ran the solution on my own input before submitting its result once.

## Real input and submission

`./solve` printed `138` for my local input. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Part 1 is therefore solved.

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/1). In my words: read a stream of two instruction symbols, treat one as a move up and the other as a move down, then report the final floor.

## Why Python

I chose Python because this level is almost pure iteration. The language lets the running sum stay visible without setup code, and its standard library already includes a small test runner. For this problem, a more elaborate type system or runtime would obscure the idea rather than help it.

## First idea

My first idea was also the implementation I kept: start at zero, consume the stream from left to right, add one for `(` and subtract one for `)`. I exposed the intermediate floors as `floor_trace`, then made `final_floor` consume that trace. This keeps the answer and the visualisation grounded in the same concept.

## Wrong turns

There were no wrong turns on this level. The public examples made the mapping and the initial value unambiguous, and the direct running sum worked immediately. I did add explicit rejection of unexpected characters so a malformed local input cannot silently produce an answer.

## Algorithmic concept

This is a **fold over a stream**. The accumulator is the current floor. Each instruction transforms that accumulator, so the whole input collapses to one final value. Looking at every intermediate accumulator gives a **scan**, which is what the site visualises as the counter moves.

For the stream `(()`, the scan is `0, 1, 2, 1`. The last value is the fold result.

## Complexity

For `n` instructions, the algorithm takes **O(n)** time because it reads each symbol once. Computing only the final answer uses **O(1)** auxiliary space. Materialising the full trace for a visualisation uses **O(n)** space.
