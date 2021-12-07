from word_processor import count_words

def test_corpus(get_text_from_file):
    """
    testing a fixture
    :param get_text_from_file: name of the function
    :return: None
    """
    assert count_words(get_text_from_file) > 10