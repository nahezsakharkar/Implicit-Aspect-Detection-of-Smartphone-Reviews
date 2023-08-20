from spacy.language import Language
import spacy
from spacy.symbols import ORTH, LEMMA, POS

nlp = spacy.load("en_core_web_sm")


def set_custom_boundaries(doc):
    for token in doc[:-1]:
        # Check for comma or conjunction as sentence boundary
        if token.text in [",", "and", "or", "but", "yet", "so", "nor"]:
            doc[token.i + 1].is_sent_start = True
    return doc


Language.component("set_custom_boundaries", func=set_custom_boundaries)
nlp.add_pipe("set_custom_boundaries", before="parser")


def tokenize_words(text):
    tokens = []
    for token in text:
        tokens.append(token.text)
    return tokens


def stem_token(word):
    texts = tokenize_words(nlp(word))
    return list(filter(bool, map(clean_text, clean_array(texts))))[0]


def clean_text(text):
    doc = nlp(text)
    return " ".join(token.lemma_ for token in doc if token.is_alpha)


def clean_array(texts):
    cleaned_text = []
    for doc in nlp.pipe(texts, disable=["parser", "ner"]):
        words = [token.text for token in doc if token.is_alpha]
        cleaned_text.append(" ".join(words))
    return cleaned_text
