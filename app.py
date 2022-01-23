from textblob import TextBlob

def hello(name):
    output = f'Hello {name}'
    return output

def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text


def bubblesort(tab: list) -> list:

    l = len(tab)

    for i in range(l - 1):
        for j in range(0, l - i - 1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab


if __name__ == "__main__":
    pass