"""Solution for Advent of Code 2015, Day 18, Part 1."""


def parse_grid(document: str) -> tuple[str, ...]:
    """Parse the rectangular light grid."""
    rows = tuple(line for line in document.splitlines() if line)
    if not rows or any(set(row) - {".", "#"} for row in rows):
        raise ValueError("grid must contain only '.' and '#'")
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError("grid must be a non-empty rectangle")
    return rows


def step(grid: tuple[str, ...]) -> tuple[str, ...]:
    """Advance all lights simultaneously by one step."""
    height, width = len(grid), len(grid[0])
    result: list[str] = []
    for row in range(height):
        next_row: list[str] = []
        for column in range(width):
            neighbours = sum(
                0 <= row + dr < height
                and 0 <= column + dc < width
                and grid[row + dr][column + dc] == "#"
                for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
                if (dr, dc) != (0, 0)
            )
            on = grid[row][column] == "#"
            next_row.append("#" if neighbours == 3 or (on and neighbours == 2) else ".")
        result.append("".join(next_row))
    return tuple(result)


def part_one(document: str, steps: int = 100) -> int:
    """Return the number of lights on after the requested steps."""
    grid = parse_grid(document)
    for _ in range(steps):
        grid = step(grid)
    return sum(row.count("#") for row in grid)


if __name__ == "__main__":
    with open("inputs/2015/18.txt", encoding="utf-8") as input_file:
        print(part_one(input_file.read()))
