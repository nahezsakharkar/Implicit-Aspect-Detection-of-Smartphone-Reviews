import spacy
import streamlit as st
from spacy.symbols import ORTH, LEMMA, POS

nlp = spacy.load("en_core_web_sm")


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


def detect_implicit_aspects(review):
    words = tokenize_words(review)
    filtered_words = list(filter(bool, map(clean_text, clean_array(
        [word for word in words if word.lower() not in nlp.Defaults.stop_words]))))

    purchased_keywords = ["bought", "purchased", "acquired", "got",
                          "obtained", "picked", "selected", "chose", "decided", "gathered"]
    age_keywords = ["old", "new", "years", "vintage", "outdated",
                    "recent", "out-of-date", "ancient", "modern", "obsolete"]
    performance_keywords = ["performance", "work", "work well",
                            "work efficiently", "function", "functionality", "operate", "run", "execute"]
    design_keywords = ["design", "appearance", "look", "style",
                       "aesthetic", "shape", "form", "structure", "outline", "configuration"]
    screen_keywords = ["screen", "display", "monitor", "view", "picture",
                       "image", "resolution", "size", "aspect ratio", "brightness"]
    battery_keywords = ["battery", "power", "energy", "charge", "duration",
                        "life", "capacity", "runtime", "endurance", "lasting", "dead"]
    brand_keywords = ["brand", "manufacturer", "make", "producer",
                      "label", "logo", "identity", "reputation", "status", "name"]
    cost_keywords = ["price", "cost", "value", "worth", "expense", "payment",
                     "amount", "fee", "charge", "budget", "low-end", "mid-range", "high-end", "sale", "expensive", "affordable",  "costly", "reasonable", "budget-friendly", "pricey", "inexpensive", "valuable", "cheap", "economical",
                     "high-priced", "overpriced", "premium", "discounted", "competitive", "worthwhile", "over-budget", "extravagant", "Low-cost", "Pocket-friendly"]
    camera_keywords = ["cameras", "photography", "lens", "shot",
                       "picture", "image", "snapshot", "focus", "flash", "resolution"]
    os_keywords = ["android", "ios", "windows phone", "windows", "Kaios",
                           "harmonyos", "lineageOS", "oxygen os", "oxygen", "miui", "color os", "color", "realme ui"]
    experience_keywords = ["experience", "feeling", "impression", "perception",
                           "sensation", "judgment", "opinion", "attitude", "reaction", "view"]

    aspects = {}
    for key in purchased_keywords:
        if stem_token(key).lower() in filtered_words:
            aspects[key] = "The phone was purchased."

    for key in age_keywords:
        if stem_token(key).lower() in filtered_words:
            aspects[key] = "The age of the phone is mentioned."

    for key in performance_keywords:
        if stem_token(key).lower() in filtered_words:
            aspects[key] = "The phone's performance is discussed."

    for key in design_keywords:
        if stem_token(key).lower() in filtered_words:
            aspects[key] = "The design of the phone is mentioned."

    for key in screen_keywords:
        if stem_token(key).lower() in filtered_words:
            aspects[key] = "The screen size is discussed."

    for key in battery_keywords:
        if stem_token(key).lower() in filtered_words:
            aspects[key] = "The battery life is discussed."

    for key in brand_keywords:
        if stem_token(key).lower() in filtered_words:
            aspects[key] = "The brand is mentioned."

    for key in cost_keywords:
        if stem_token(key).lower() in filtered_words:
            aspects[key] = "The cost is mentioned."

    for key in camera_keywords:
        if stem_token(key).lower() in filtered_words:
            aspects[key] = "The camera is discussed."
            
    for key in os_keywords:
        if key.lower() in filtered_words:
            aspects[key] = "The Operating System is Mentioned."

    for key in experience_keywords:
        if stem_token(key).lower() in filtered_words:
            aspects[key] = "The overall experience with the phone is discussed."

    return aspects


# Streamlit app
def app():
    st.set_page_config(
        page_title="Implicit Aspect Detection",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("Implicit Aspect Detection from Smartphone Reviews")

    menu = ["Detect Implicit Aspects", "About"]
    choice = st.sidebar.selectbox("Select an option", menu)

    # Define the pages
    def about_page():
        st.header("About Implicit Aspect Detection from Smartphone Reviews")
        st.subheader("Introduction")
        st.write("Implicit aspect detection is the process of identifying implicit aspects of a product that are not explicitly mentioned in a review. In the case of smartphone reviews, implicit aspects could include factors such as battery life, camera quality, and user interface, which are not always mentioned in the review but can greatly influence the reviewer's overall opinion of the device. Detecting these implicit aspects can provide valuable insights into the strengths and weaknesses of a product and help manufacturers improve their offerings.")
        st.subheader("Approaches to implicit aspect detection")
        st.write("There are several approaches to implicit aspect detection in smartphone reviews. One approach is to use natural language processing (NLP) techniques to analyze the text of the review and identify patterns and themes that relate to particular aspects of the device. Another approach is to use machine learning algorithms to automatically categorize reviews based on their content, with different categories corresponding to different aspects of the device.")
        st.subheader("Challenges of implicit aspect detection")
        st.write("One of the main challenges of implicit aspect detection from smartphone reviews is the high degree of variability and subjectivity in the language used by reviewers. Reviews may contain slang, idiomatic expressions, or other language quirks that make it difficult for automated algorithms to accurately identify the implicit aspects of the device being discussed. Additionally, different reviewers may have different opinions about which aspects of the device are most important, making it challenging to develop a universal set of criteria for implicit aspect detection.")
        st.subheader("Importance of implicit aspect detection")
        st.write("Despite the challenges, implicit aspect detection is an important tool for manufacturers of smartphones and other consumer electronics. By understanding the implicit aspects of their products that are most important to customers, manufacturers can focus their efforts on improving those aspects and enhancing the overall customer experience. Implicit aspect detection can also help manufacturers identify emerging trends in the market and stay ahead of the competition.")
        st.subheader("Future directions")
        st.write("As the field of implicit aspect detection continues to evolve, new techniques and approaches will be developed to improve the accuracy and reliability of the process. One promising direction is the use of deep learning algorithms that can identify more complex patterns and relationships in the language used in reviews. Another direction is the integration of implicit aspect detection with other forms of market research, such as social media analytics and customer surveys, to provide a more complete picture of customer needs and preferences. With continued innovation and development, implicit aspect detection has the potential to revolutionize the way manufacturers approach product development and customer satisfaction.")

        st.subheader("The following technologies were used to build this app:")
        st.write("- spaCy: Spacy is a popular and powerful open-source library for natural language processing tasks. It provides efficient and accurate tools for tasks such as tokenization, named entity recognition, part-of-speech tagging, and dependency parsing, and is well-suited for large-scale applications. With a user-friendly API and a growing community of contributors, Spacy has become a widely-used tool in academia, industry, and government.")
        st.write("- Streamlit: Streamlit is an open-source Python library that makes it easy to build interactive data science web applications. With Streamlit, developers can quickly create data visualizations, machine learning models, and other interactive components with a simple and intuitive API. Streamlit also provides tools for sharing and deploying applications to the web.")

        st.subheader("The following techniques were used to build this app:")
        st.write("- Rule Based Technique: Rule-based techniques are one approach to implicit aspect detection in natural language processing. This technique involves the creation of a set of rules or heuristics that can identify implicit aspects of a product or service based on specific patterns in the text. For example, a rule-based system might identify aspects related to a product's size or color based on specific adjectives or descriptions in the text. One advantage of rule-based techniques is that they can be highly accurate when applied to specific domains or languages. However, developing effective rules can be time-consuming and require significant expertise in the domain being analyzed. Additionally, rule-based systems may struggle to handle complex and nuanced language, or new and previously unseen patterns in the text. Despite these limitations, rule-based techniques remain a valuable tool in implicit aspect detection, particularly when combined with other approaches such as machine learning.")
        
        st.subheader("About the creators of the App:")
        st.write(
            "This App(Mini Project) was created by Nahez Sakharkar(44), Karan Pansare(34) and Moin Qazi(40) Under the mentorship of Mr. Ameya Parkar.")

    def detect_implicit_aspects_page():
        st.header("Detect Implicit Aspects from Smartphone Reviews")
        st.write("Enter a smartphone review to detect its implicit aspects.")

        review = st.text_input("Review")
        doc = nlp(review)

        if review:
            implicit_aspects = detect_implicit_aspects(doc)
            if len(implicit_aspects) > 0:
                st.write("The implicit aspects in the review are:")
                words = review.split()
                for i in range(len(words)):
                    if words[i] in implicit_aspects.keys():
                        words[i] = f"<b><u>{words[i]}</u></b>"

                # Join words back into sentence
                sentence = " ".join(words)

                # Display sentence with bold text
                st.markdown(sentence, unsafe_allow_html=True)

                for key, value in implicit_aspects.items():
                    st.write(key + " : " + value)

            else:
                st.write("No implicit aspects found in the review.")

    # Show the appropriate page based on the user's choice
    if choice == "Detect Implicit Aspects":
        detect_implicit_aspects_page()
    elif choice == "About":
        about_page()


# Run the app
if __name__ == "__main__":
    app()
