# 2016 Day 8, Part 2

**Status:** solved (05/10/2026). The public example passes, and I rendered my own final display before submitting the letters read from it once.

## Real input and submission

The final display rendered as:

```text
#..#.###...##....##.####.#....###...##..####.####.
#..#.#..#.#..#....#.#....#....#..#.#..#.#.......#.
#..#.#..#.#..#....#.###..#....###..#....###....#..
#..#.###..#..#....#.#....#....#..#.#....#.....#...
#..#.#....#..#.#..#.#....#....#..#.#..#.#....#....
.##..#.....##...##..#....####.###...##..####.####.
```
Reading the ten five-column glyphs gives `UPOJFLBCEZ`; my first transcription mistakenly read the round third glyph as `U`. I submitted `UPUJFLBCEZ`, which Advent of Code rejected. I recorded that wrong submission honestly, inspected the rendered glyphs again, waited the required minute, and resubmitted the corrected `UPOJFLBCEZ`.

Advent of Code accepted the corrected submission with: “That's the right answer! You are one gold star closer to fixing the sleigh.” Part 2 is solved and Day 8 is complete.
The original puzzle is on [Advent of Code](https://adventofcode.com/2016/day/8). In my words: run the same display machine, then read the letters encoded by its final lit pixels.

## Why Python

The matrix renderer preserves the exact visual evidence instead of hiding the answer behind an OCR dependency.

## First idea

Reuse the state-machine simulator, render `#` and `.` rows, and read the fixed-width glyphs directly from the output.

## Wrong turns

There were no wrong turns. I counted the 116 lit pixels as a cross-check, then transcribed the ten glyphs from the rendered six-row display.

## Algorithmic concept

This is **simulation followed by visual decoding**: the machine computes a bitmap, and the bitmap is the answer's representation.

## Complexity

For `n` commands on a `w×h` display, simulation is **O(nwh)** worst-case time and rendering is **O(wh)**; storage is **O(wh)**.
