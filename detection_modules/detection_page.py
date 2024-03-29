from detection_modules.detection import detect_implicit_aspects
from detection_modules.sentiment import findSentiment
from annotated_text import annotated_text
from detection_modules.preprocessing import process_text_conjunctions


def detect_implicit_aspects_page(st, nlp):
    st.header("Detect Implicit Aspects from Smartphone Reviews")
    st.write("Enter a smartphone review to detect its implicit aspects.")

    review = st.text_area("Review")
    # doc = nlp(review)
    # sentences = [sent.text for sent in doc.sents]
    sentences = process_text_conjunctions(review)

    if review:
        with st.spinner("Aspect Detection in progress. Please wait."):
            aspects = detect_implicit_aspects(sentences, nlp)
        st.success("The Detection Process was successfully completed!")
        st.toast("The Detection Process was successfully completed!", icon="✅")

        if len(aspects) > 0:
            # words = review.split()
            # for i in range(len(words)):
            #     if words[i] in aspects.keys():
            #         words[i] = f"<b><u>{words[i]}</u></b>"

            # # Join words back into sentence
            # sentence = " ".join(words)

            # # Display sentence with bold text
            # st.markdown(sentence, unsafe_allow_html=True)

            st.divider()

            has_explicit = any(
                isinstance(value, dict)
                and "explicit" in value
                and bool(value["explicit"])
                for value in aspects.values()
            )
            if has_explicit:
                st.subheader("The Explicit aspects in the review are:")
                for key, value in aspects.items():
                    # st.write(key)
                    if (
                        isinstance(value, dict)
                        and "explicit" in value
                        and value["explicit"]
                    ):
                        for k, v in value["explicit"].items():
                            st.write(key)
                            st.write("  " + k + ": " + v)
            else:
                st.write("No Explicit Aspects found in the review.")

            st.divider()

            has_implicit = any(
                isinstance(value, dict)
                and "implicit" in value
                and bool(value["implicit"])
                for value in aspects.values()
            )

            if has_implicit:
                st.subheader("The Implicit aspects in the review are:")
                for key, value in aspects.items():
                    # st.write(key)
                    if (
                        isinstance(value, dict)
                        and "implicit" in value
                        and value["implicit"]
                    ):
                        for k, v in value["implicit"].items():
                            st.write(key)
                            st.write("  " + k + ": " + v)
            else:
                st.write("No Implicit Aspects found in the review.")

            st.divider()
            st.subheader("The Sentiment of the Review:")

            for sentence in sentences:
                annotated_text(
                    (
                        sentence,
                        findSentiment(nlp(sentence)),
                    )
                )

            st.divider()

        else:
            st.write("No Aspects found in the review.")
