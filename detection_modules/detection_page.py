from detection_modules.detection import detect_implicit_aspects


def detect_implicit_aspects_page(st, nlp):
    st.header("Detect Implicit Aspects from Smartphone Reviews")
    st.write("Enter a smartphone review to detect its implicit aspects.")

    review = st.text_input("Review")
    doc = nlp(review)

    if review:
        aspects = detect_implicit_aspects(doc, nlp)
        if len(aspects) > 0:
            # words = review.split()
            # for i in range(len(words)):
            #     if words[i] in aspects.keys():
            #         words[i] = f"<b><u>{words[i]}</u></b>"

            # # Join words back into sentence
            # sentence = " ".join(words)

            # # Display sentence with bold text
            # st.markdown(sentence, unsafe_allow_html=True)

            has_explicit = any(
                isinstance(value, dict)
                and "explicit" in value
                and bool(value["explicit"])
                for value in aspects.values()
            )
            if has_explicit:
                st.subheader("The Explicit aspects in the review are:")
                for key, value in aspects.items():
                    st.write(key)
                    if (
                        isinstance(value, dict)
                        and "explicit" in value
                        and value["explicit"]
                    ):
                        for k, v in value["explicit"].items():
                            st.write("  " + k + ": " + v)
            else:
                st.write("No Explicit Aspects found in the review.")

            has_implicit = any(
                isinstance(value, dict)
                and "implicit" in value
                and bool(value["implicit"])
                for value in aspects.values()
            )

            if has_implicit:
                st.subheader("The Implicit aspects in the review are:")
                for key, value in aspects.items():
                    st.write(key)
                    if (
                        isinstance(value, dict)
                        and "implicit" in value
                        and value["implicit"]
                    ):
                        for k, v in value["implicit"].items():
                            st.write("  " + k + ": " + v)
            else:
                st.write("No Implicit Aspects found in the review.")

        else:
            st.write("No Aspects found in the review.")
