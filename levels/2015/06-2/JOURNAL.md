# 2015 Day 6, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/6). I read Part 2 only.

## First idea

I kept the 1,000 by 1,000 row-oriented board from Part 1, but changed each cell from a binary value to an unsigned integer brightness. Each instruction is parsed into an operation and two inclusive coordinate pairs, then applied in input order. Turning on adds one, toggling adds two, and turning off subtracts one only when the current value is positive.

## Wrong turns

My first instinct was to reuse Part 1's `bytearray` rows. That cannot represent brightness values above 255, so it would silently wrap or require special handling. I also considered a dictionary of only nonzero cells, but the real instructions cover large rectangles and dictionary entries would add overhead to nearly every coordinate. Fixed `array("I")` rows keep the board compact while allowing direct integer updates.

## Public examples

The tests cover increasing one cell, increasing every cell by two, the rule that brightness cannot become negative, and a small sequence that checks inclusive endpoints and instruction order.

## Complexity

The board stores **O(1,000,000)** unsigned integers. Each instruction takes time proportional to the number of cells in its inclusive rectangle, so the complete run is **O(sum of rectangle areas)**. Parsing and the final total add **O(number of instructions + 1,000,000)** time.

## Submission

I ran the tested solution on my own input; it returned `15343601`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 6 Part 2 is therefore complete.
