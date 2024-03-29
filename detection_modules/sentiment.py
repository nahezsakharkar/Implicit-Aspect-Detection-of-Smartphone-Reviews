from textblob import TextBlob
from detection_modules.preprocessing import stem_token


def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity


def get_sentiment_label(sentiment):
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"


def replace_words(sentence):
    string_sentence = sentence.text.lower()

    dictionary = {
        "goat": "great",
        "trash": "bad",
        "bang for the buck": "great",
        "snappy": "great",
        "beast": "great",
        "lag": "bad",
        "pricey": "bad",
        "lit": "great",
        "op": "great",
        "pocket rocket": "great",
    }

    words = [stem_token(word) for word in string_sentence.split()]
    new_sentence = []

    i = 0
    while i < len(words):
        current_word = words[i]

        # Check for multi-word combinations starting from the current word
        for j in range(len(words), i, -1):
            combined_key = " ".join(words[i:j])
            if combined_key in dictionary:
                new_sentence.append(dictionary[combined_key])
                i = j
                break
        else:
            # If no multi-word combination is found, check for single-word replacement
            if current_word in dictionary:
                new_sentence.append(dictionary[current_word])
                i += 1
            else:
                new_sentence.append(current_word)
                i += 1

    new_sentence = " ".join(new_sentence)
    return new_sentence


def findSentiment(sentence):
    sentiment = get_sentiment(replace_words(sentence))
    label = get_sentiment_label(sentiment)
    return label
