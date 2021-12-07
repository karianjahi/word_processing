"""
Create a function that counts the number
of words in a string
Make sure to run all tests and run the commands:
 coverage run -m pytest
 and
coverage html
to get the coverage of tests.
Open the index.html in the browser.
"""

# pylint: disable=C0301
def count_words(my_string):
    """
    This function counts words
    :param my_string: str - A string of words or characters
    :return: int - length of words
    """
    if not isinstance(my_string, str):
        raise TypeError("only accepts strings")

    special_characters = ['-', '+', '\n']

    for character in special_characters:
        my_string = my_string.replace(character, " ")

    words = my_string.split()
    return len(words)


if __name__ == "__main__":
    SOME_WORDS = "everlyn\nTosin"
    print(count_words(SOME_WORDS))
