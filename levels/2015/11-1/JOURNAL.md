# 2015 Day 11, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/11).

## First idea

I represent the password as eight lowercase letters and implement ordinary base-26 counting from right to left. Starting with the next password, I test candidates until one has an increasing three-letter straight, no `i`, `o`, or `l`, and two different non-overlapping pairs. Since a candidate containing a forbidden letter cannot be valid, the search jumps over the whole suffix range beginning at its first forbidden letter; validation still remains responsible for every rule.

## Wrong turns

I first considered skipping directly over forbidden letters while incrementing. The direct increment helper is easier to reason about when it remains ordinary counting, so I kept that behavior and put the safe jump in the candidate search instead. I also made the pair scan consume both characters after a match: this prevents an overlapping run such as `aaa` from being counted twice. I did not submit a wrong answer.

## Public examples

The tests cover both published next-password examples, the individual validity examples, carry and wraparound, different non-overlapping pairs, and malformed inputs.

## Complexity

For an eight-letter password, incrementing and validating one candidate are **O(1)** in the fixed input size. If **C** candidates are examined, the complete search is **O(C)** time and **O(1)** additional space.

The tested solution returned `cqjxxyzz` for my real input. I submitted that value once after checking that Part 1 was still unsolved. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 11 Part 1 is therefore complete; Day 11 Part 2 is next.
