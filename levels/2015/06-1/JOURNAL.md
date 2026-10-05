# 2015 Day 6, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/6). I read Part 1 only.

## First idea

I model the one-million-light board as 1,000 `bytearray` rows. Each light is one byte: `0` for off and `1` for on. I parse each instruction into an operation and two inclusive coordinate pairs, then update every affected row slice in input order. Turning on and off use a repeated byte slice; toggling translates each affected byte from 0 to 1 or from 1 to 0.

## Wrong turns

My first representation was a Python list of one million booleans. It would work, but a list stores references to Python objects and spends much more memory than the one byte per light that this problem needs. A set of lit coordinates would also make each coordinate much heavier and offers no benefit when large rectangles touch most of the board. The bytearray rows keep the fixed board close to one megabyte while leaving the operations direct.

## Public examples

The tests cover the three individual examples: lighting the whole board, toggling its first row, and switching off the four central lights after the board is on. They also combine three small ranges to pin inclusive endpoints and instruction order.

## Complexity

The board uses **O(1,000,000)** bytes for its light state. Each instruction takes time proportional to the number of cells in its inclusive rectangle, so the complete run is **O(sum of rectangle areas)**. Parsing and the final count add **O(number of instructions + 1,000,000)** time.

## Submission

I ran the tested solution on my own input; it returned `400410`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 6 Part 1 is therefore complete.
