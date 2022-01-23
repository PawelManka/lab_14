from app import hello, extract_sentiment, text_contain_word, bubblesort

from textblob import TextBlob
import pytest

def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want


testdata = ["I think today will be a great day", "I do not think this will turn out well"]

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False)
    ]


@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output

testdata = [
    ([1, 3, 2, 5, 4], [1, 2, 3, 4, 5]),
    ([6, 2, 23, 1, 5, 1], [1, 1, 2, 5, 6, 23])
    ]

@pytest.mark.parametrize('sample, expected_output', testdata)
def test_text_contain_word(sample, expected_output):

    assert bubblesort(sample) == expected_output