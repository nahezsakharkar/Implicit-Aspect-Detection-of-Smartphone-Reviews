from spacy.language import Language
import spacy
from spacy.symbols import ORTH, LEMMA, POS
import re

nlp = spacy.load("en_core_web_sm")


def set_custom_boundaries(doc):
    for token in doc[:-1]:
        # Check for comma or conjunction as sentence boundary
        if token.text in [",", "or", "yet", "so", "nor"]:
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


def process_text_conjunctions(input_text):
    def split_and_remove(text):
        # Split sentences based on "but", commas, and periods
        sentences = re.split(r"[.,]|but", text)

        # Remove unwanted words (e.g., "but", commas, and periods) and filter out empty strings
        cleaned_sentences = [
            " ".join(
                word
                for word in sentence.split()
                if word.lower() not in {"but", ",", "."}
            )
            for sentence in sentences
            if sentence.strip()
        ]

        return cleaned_sentences

    def find_and_remove_objects(sentences):
        new_sentences = []
        for sentence in sentences:
            if "and" in sentence:
                # Process the sentence using spaCy
                doc = nlp(sentence)

                # Find named entities (objects)
                objects = [
                    ent.text
                    for ent in doc.ents
                    if ent.label_ == "PRODUCT" or ent.label_ == "ORG"
                ]

                if objects:
                    # Remove identified objects and "and" from the sentence
                    cleaned_sentence = " ".join(
                        word
                        for word in sentence.split()
                        if word.lower() not in {"and"} and word not in objects
                    )

                    # print(f"Original sentence: '{sentence}'")
                    # print(f"Objects found: {', '.join(objects)}")
                    # print(f"Cleaned sentence: '{cleaned_sentence}'\n")
                    # del sentences[index]
                    new_sentences.append(
                        [f"{name} {cleaned_sentence}" for name in objects]
                    )
                    # return sentences

                else:
                    parts = sentence.split("and")
                    filtered_parts = [part.strip() for part in parts if part.strip()]
                    for parts in filtered_parts:
                        new_sentences.append(parts)

            else:
                new_sentences.append(sentence)

        return new_sentences

    return find_and_remove_objects(split_and_remove(input_text))


def process_text_conjunctions_demonstration(input_text):
    # Split sentences based on "but", commas, and periods
    sentences = re.split(r"[.,]|but", input_text)

    # Remove unwanted words (e.g., "but", commas, and periods) and filter out empty strings
    cleaned_sentences = [
        " ".join(
            word for word in sentence.split() if word.lower() not in {"but", ",", "."}
        )
        for sentence in sentences
        if sentence.strip()
    ]

    return cleaned_sentences
