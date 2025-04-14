import logging


def get_num_words(book: str) -> None:
    """Print word count in given book.

    Args:
        book (str): Book text.

    """
    words = book.split()
    logging.info(f"{len(words)} words found in the document")  # noqa: G004
