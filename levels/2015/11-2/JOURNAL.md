# 2015 Day 11, Part 2

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/11).

## First idea

Part 2 keeps the same password rules and asks for the next valid password after the one found in Part 1. I therefore reused the same increment, validation, and forbidden-letter jump, then applied `next_password` twice to the original input. This keeps the two searches independent and makes the second result explicit rather than changing the validity rules.

## Wrong turns

I initially looked for a new Part 2 validation rule, but the authenticated puzzle page shows that the policy is unchanged: only the starting password has advanced. I kept the Part 1 validator unchanged and made the only new operation the second search. I did not submit a wrong answer.

## Public examples

The tests retain both published next-password examples and all Part 1 validity, carry, pair, and malformed-input checks. They also check that two searches advance past the first valid password for each published starting example.

## Complexity

For an eight-letter password, incrementing and validating one candidate are **O(1)** in the fixed input size. If **C₁** and **C₂** candidates are examined by the two searches, the complete Part 2 search is **O(C₁ + C₂)** time and **O(1)** additional space.

The tested solution returned `cqkaabcc` for my real input. I submitted that value once for Part 2. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 11 Parts 1 and 2 are therefore complete; Day 12 Part 1 is next.
