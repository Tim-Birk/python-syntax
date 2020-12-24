def print_upper_words(words, must_start_with):
    """This function should print each word on a separate line in all uppercase"""

    for word in words:
        for char in must_start_with:
            if word[0].upper() == char.upper():
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})