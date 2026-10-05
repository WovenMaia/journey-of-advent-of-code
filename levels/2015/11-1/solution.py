"""Solution for Advent of Code 2015, Day 11, Part 1."""

FORBIDDEN = frozenset("iol")


def increment(password: str) -> str:
    """Return the next eight-letter lowercase password in lexicographic order."""
    if len(password) != 8 or not password.isalpha() or not password.islower():
        raise ValueError("password must contain exactly eight lowercase letters")

    letters = list(password)
    index = len(letters) - 1
    while index >= 0 and letters[index] == "z":
        letters[index] = "a"
        index -= 1
    if index < 0:
        return "".join(letters)
    letters[index] = chr(ord(letters[index]) + 1)
    return "".join(letters)


def has_straight(password: str) -> bool:
    """Return whether the password contains three consecutive letters."""
    return any(
        ord(first) + 1 == ord(second) and ord(second) + 1 == ord(third)
        for first, second, third in zip(password, password[1:], password[2:])
    )


def has_two_different_pairs(password: str) -> bool:
    """Return whether two non-overlapping pairs use different letters."""
    pairs = set()
    index = 0
    while index < len(password) - 1:
        if password[index] == password[index + 1]:
            pairs.add(password[index])
            index += 2
        else:
            index += 1
    return len(pairs) >= 2


def is_valid(password: str) -> bool:
    """Return whether a password satisfies all Corporate Policy rules."""
    return (
        len(password) == 8
        and password.isalpha()
        and password.islower()
        and not FORBIDDEN.intersection(password)
        and has_straight(password)
        and has_two_different_pairs(password)
    )


def _skip_forbidden(password: str) -> str:
    """Jump past all candidates sharing the first forbidden letter prefix."""
    for index, letter in enumerate(password):
        if letter in FORBIDDEN:
            return password[:index] + chr(ord(letter) + 1) + "a" * (7 - index)
    return password


def next_password(password: str) -> str:
    """Find the first valid password strictly after the given password."""
    if len(password) != 8 or not password.isalpha() or not password.islower():
        raise ValueError("password must contain exactly eight lowercase letters")

    candidate = increment(password)
    while True:
        candidate = _skip_forbidden(candidate)
        if is_valid(candidate):
            return candidate
        candidate = increment(candidate)


if __name__ == "__main__":
    with open("inputs/2015/11.txt", encoding="utf-8") as input_file:
        print(next_password(input_file.read().strip()))
