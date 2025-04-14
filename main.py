"""Main code for bookbot."""
import logging
import sys
from collections import defaultdict
from pathlib import Path
from string import ascii_lowercase

from stats import get_num_words

logging.basicConfig(format="%(message)s", level=logging.INFO)

def main(file: str) -> None:
    """Execute main code for bookbot.

    Args:
        file (str): Path to file

    Returns:
        str: Contents of file

    """
    book = read_book(file)
    get_num_words(book)
    character_counts = count_characters(book)
    logging.info(f"--- Begin report of {file} ---")  # noqa: G004
    character_counts = dict(sorted(
        character_counts.items(),
        key=lambda item: item[1],
        reverse=True),
    )
    for c in character_counts:
        if c in ascii_lowercase:
            print(f"{c}: {character_counts[c]}")

def count_characters(text: str) -> dict[str, int]:
    """Count character appearances in given text.

    Args:
        text (str): Text to count from

    Returns:
        dict[str, int]: Character counts

    """
    counts = defaultdict(int)
    text = text.lower()
    for c in text:
        counts[c] += 1
    return dict(counts)

def read_book(file: Path) -> str:
    """Read book contents.

    Args:
        file (Path): File path to book

    Returns:
        str: Book contents

    """
    with Path.open(file) as f:
        return f.read()

if __name__ == "__main__":
    expected_args = 2
    if len(sys.argv) != expected_args:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = Path(sys.argv[1])
    main(book)
