# 2015 Day 4, Part 1

**Status:** solved (05/10/2026).

The original puzzle is on [Advent of Code](https://adventofcode.com/2015/day/4). I read Part 1 only.

## First idea

I search positive integer suffixes in ascending order. For each suffix, I hash the secret key followed by its decimal representation and stop at the first digest whose hexadecimal form begins with five zeroes. The ordered search makes the first match the required lowest number.

## Public examples

The prompt's examples return `609043` for `abcdef` and `1048970` for `pqrstuv`; both are covered by the tests.

## Complexity

Each MD5 digest has a one-in-$16^5 = 1,048,576$ chance of beginning with five hexadecimal zeroes, so the expected search takes about **1,048,576 hash attempts**. For the successful suffix $k$, this implementation takes **O(k log k)** time because decimal-suffix encoding costs O(log k) per attempt, and **O(1)** auxiliary space.

## Wrong turns

There were no algorithmic wrong turns. On 04/10 the input endpoint answered as if I were logged out, so the level stayed staged instead of borrowing another person's input. The browser's Advent of Code session turned out to be valid all along; the request had simply not carried it. Sending that session cookie with the request returned my own input.

## Submission

I ran the tested solution on my own input; it returned `282749`. I submitted that value once. Advent of Code replied: “That's the right answer! You are one gold star closer to powering the weather machine.” Day 4 Part 2 is next.
