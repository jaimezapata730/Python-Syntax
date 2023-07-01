def print_upper_words(words):
    """print out each word on a separate line, but in all uppercase."""

    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """prints words that start with the letter E or e."""

    for word in words:
        if word.startwith("E") or word.startwith("e"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """pass in a set of letters, and it only prints words that start with one of those letters."""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break