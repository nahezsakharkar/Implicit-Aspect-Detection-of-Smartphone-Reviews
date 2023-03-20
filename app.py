from spacy.language import Language
import spacy
import streamlit as st
from spacy.symbols import ORTH, LEMMA, POS

nlp = spacy.load("en_core_web_sm")


def set_custom_boundaries(doc):
    for token in doc[:-1]:
        # Check for comma or conjunction as sentence boundary
        if token.text in [",", "and", "or", "but", "yet", "so", "nor"]:
            doc[token.i+1].is_sent_start = True
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


def detect_implicit_aspects(review):

    purchased_keywords = {"explicit": ["bought", "purchased", "ordered"], "noun": ["acquired", "got", "obtained", "picked", "selected", "chose", "decided", "gathered", "gifted"],
                          "adj": ["new", "latest"]}
    age_keywords = {"explicit": ["old", "new", 'fresh', 'latest', 'current', 'up-to-date', 'modern', 'contemporary',
                                 'recently released', 'state-of-the-art', 'cutting-edge', 'latest technology', 'newest model/version',
                                 'just released', 'recently launched', "years"], "noun": ["qwerty", "analog"],
                    "adj": ["vintage", "outdated", "retro", "recent", "out-of-date", "ancient", "modern", "obsolete"]}
    performance_keywords = {"explicit": ["perform", "performance"], "noun": ["work", "work well", "work efficiently", "function", "functionality", "operate", "run", "execute"],
                            "adj": ["Smooth", "Snappy", "fast", "responsive", "reliable", "efficient", "dynamic", "beast"]}
    design_keywords = {"explicit": ["design", "appearance", "look"], "noun": ["style", "shape", "form", "structure", "outline", "configuration"],
                       "adj": ["sleek", "beautiful", "elegant", "stylish", "minimalistic", "attractive", "eyecatching",
                               "futuristic", "classy", "slim", "compact", "aesthetic", "comfortable "]}
    screen_keywords = {"explicit": ["screen", "display", ], "noun": ["monitor", "view", "picture", "image", "resolution", "size", "ratio", "brightness",
                                                                     'contrast', 'pixel', 'color', 'viewing', 'touchscreen', 'amoled', 'lcd', 'oled', 'refresh rate',
                                                                     'bezel', 'hdr', 'notch', 'protector'],
                       "adj": ['clear', 'sharp', 'vivid', 'bright', 'dim', 'dull', 'high-resolution', 'low-resolution', 'color-rich', "anti-galre"
                               'color-accurate', 'wide-angle', 'narrow-angle', 'responsive', 'smooth', 'fast', 'slow', 'immersive', 'reflective', 'glare-free', "huge"]}
    battery_keywords = {"explicit": ["battery", ], "noun": ["power", "energy", "charge", "duration", "life", "capacity", "runtime", "endurance", "lasting", "dead",
                                                            'capacity', 'usage', 'drain', 'charging time', 'charging', 'wireless', 'health', 'saver mode',
                                                            'backup', 'consumption', 'charging port', 'endurance'],
                        "adj": ['long-lasting', 'efficient', 'reliable', 'powerful', 'fast-charging', 'wireless', 'low-power',  'durable',
                                'energy-saving', 'sustainable', 'eco-friendly', 'dependable']}
    brand_keywords = {"explicit": ["brand", "manufacturer", ], "noun": ["make", "producer", "label", "logo", "identity", "reputation", "status", "name", 'popularity',
                                                                        'market share', 'innovation', 'customer support', 'product lineup', 'availability',
                                                                        'connectivity',  'accessories', 'warranty'],
                      "adj": ['popular', 'reliable', 'innovative', 'iconic', 'trusted', 'sophisticated', 'highquality', 'technologically advanced',
                              'user-friendly', 'cutting-edge', 'durable',  'versatile', 'efficient', 'longlasting', 'advanced', 'competitive']}
    cost_keywords = {"explicit": ["price", "cost", "value", "worth"], "noun": ["expense", "payment", "amount", "fee", "charge", "budget", "sale"],
                     "adj": ["low-end", "mid-range", "high-end", "expensive", "affordable", "costly", "reasonable", "budgetfriendly", "pricey", "inexpensive",
                             "valuable", "cheap", "economical", "highpriced", "overpriced", "premium", "discounted", "competitive", "worthwhile",
                             "over-budget", "extravagant", "Low-cost", "Pocketfriendly"]}
    camera_keywords = {"explicit": ["cameras"], "noun": ["photography", "lens", "shot", "picture", "image", "snapshot", "focus", "flash", "resolution", 'aperture',
                                                         'zoom', 'megapixel', 'autofocus', 'shutter', 'stabilization',  'hdr', 'lowlight',
                                                         'depth perception', 'selfie', 'video', 'motion',  'mode', 'panorama', 'telephoto',
                                                         'ultrawide', 'night mode', 'macro', 'bokeh'],
                       "adj": ['clear', 'sharp', 'detailed', 'vivid', 'bright', 'colorful', 'fast', 'accurate',  'low noise', 'crisp', 'dynamic',
                               'balanced', 'professional', 'artistic', 'smooth', 'consistent',  'stunning', 'natural', 'impressive']}
    os_keywords = {"explicit": ["operating system"], "noun": ["android", "ios", "windows", "windows", "Kaios", "harmonyos", "lineage os", "oxygen os", "oxygen", "miui", "color os",
                                                              "color", "realme ui", 'interface', 'customization', 'compatibility', 'security', 'stability', 'updates', 'integration',
                                                              'navigation', 'multitasking', 'accessibility',  'functionality', 'efficiency',
                                                              'control', 'interface', 'operating system version',  'compatibility', 'ai'],
                   "adj": ['intuitive', 'efficient', 'customizable', 'seamless', 'secure', 'reliable', 'stable', 'fast',  'responsive', 'user',
                           'robust', 'versatile', 'innovative', 'modern', 'streamlined',  'fluid', 'dynamic', 'adaptive', 'consistent']}
    experience_keywords = {"explicit": ["experience"], "noun": ["feeling", "impression", "perception", "sensation", "judgment", "opinion", "attitude", "reaction", "view"],
                           "adj": ['memorable', 'pleasant', 'unforgettable', 'challenging', 'exciting', 'educational', 'unique', 'incredible',
                                   'fulfilling', 'inspiring', 'refreshing', 'empowering', 'eyeopening', 'rewarding', 'intense', 'engaging', 'transformative',
                                   'relaxing', 'disappointing', 'frustrating', "superb"]
                           }

    phone_keywords = {"subjects" : ["phone", "smartphone", "cell", "device", "handset"], 
                      "adjectives" : ["awesome", "fantastic", "cool", "superb", "perfect", "bad", "trash", "worst"]}

    aspects = {}
    # adding sentences as key in aspects = {"sentence-1" : {}, "sentence-2" : {}}
    for sent in review.sents:
        aspects[sent] = {}

    for sentence, Aspect_Dict in aspects.items():
        Aspect_Dict["subject"] = []
        Aspect_Dict["object"] = []
        Aspect_Dict["adjective"] = []
        Aspect_Dict["explicit"] = {}
        Aspect_Dict["implicit"] = {}
        # filtered words has all the tokens of all sentences each
        filtered_words = list(filter(bool, map(clean_text, clean_array(
            [word for word in tokenize_words(sentence) if word.lower() not in nlp.Defaults.stop_words]))))

        for token in sentence:
            if token.dep_ == "nsubj":
                Aspect_Dict["subject"].append(token.text)
            if token.dep_ == "dobj":
                Aspect_Dict["object"].append(token.text)
            if token.pos_ == "ADJ" or token.pos_ == "ADV":
                Aspect_Dict["adjective"].append(token.text)

        def check_every_keyword(arr):
            # for every element in purchases explicit list
            for element in purchased_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][element] = "The phone was purchased."

            for element in purchased_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The phone was purchased."

            for element in purchased_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The phone was purchased."

            # for every element in age explicit list
            for element in age_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][element] = "The age of the phone is mentioned."

            for element in age_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The age of the phone is mentioned."

            for element in age_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The age of the phone is mentioned."

            # for every element in performance explicit list
            for element in performance_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][element] = "The phone's performance is discussed."

            for element in performance_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The phone's performance is discussed."

            for element in performance_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The phone's performance is discussed."

            # for every element in design explicit list
            for element in design_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][element] = "The design of the phone is mentioned."

            for element in design_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The design of the phone is mentioned."

            for element in design_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The design of the phone is mentioned."

            # for every element in screen explicit list
            for element in screen_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][element] = "The screen is discussed."

            for element in screen_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The screen is discussed."

            for element in screen_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The screen is discussed."

            # for every element in battery explicit list
            for element in battery_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][element] = "The battery life is discussed."

            for element in battery_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The battery life is discussed."

            for element in battery_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The battery life is discussed."

            # for every element in brand explicit list
            for element in brand_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][element] = "The brand is mentioned."

            for element in brand_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The brand is mentioned."

            for element in brand_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The brand is mentioned."

            # for every element in cost explicit list
            for element in cost_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][element] = "The cost is mentioned."

            for element in cost_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The cost is mentioned."

            for element in cost_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The cost is mentioned."

            # for every element in camera explicit list
            for element in camera_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][element] = "The camera is discussed."

            for element in camera_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The camera is discussed."

            for element in camera_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The camera is discussed."

            # for every element in os explicit list
            for element in os_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][element] = "The Operating System is Mentioned."

            for element in os_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The Operating System is Mentioned."

            for element in os_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The Operating System is Mentioned."

            # for every element in experience explicit list
            for element in experience_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][element] = "The overall experience with the phone is discussed."

            for element in experience_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The overall experience with the phone is discussed."

            for element in experience_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][element] = "The overall experience with the phone is discussed."

        check_every_keyword(filtered_words)
        if len(Aspect_Dict["subject"]) > 0:
            if stem_token(Aspect_Dict["subject"][0]) in phone_keywords["subjects"]:
                if len(Aspect_Dict["adjective"]) > 0:
                    if stem_token(Aspect_Dict["adjective"][0]) in phone_keywords["adjectives"]:
                            Aspect_Dict["implicit"][Aspect_Dict["subject"][0]] = "The Phone as whole is described."

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
            aspects = detect_implicit_aspects(doc)
            if len(aspects) > 0:
                # words = review.split()
                # for i in range(len(words)):
                #     if words[i] in aspects.keys():
                #         words[i] = f"<b><u>{words[i]}</u></b>"

                # # Join words back into sentence
                # sentence = " ".join(words)

                # # Display sentence with bold text
                # st.markdown(sentence, unsafe_allow_html=True)
                
                has_explicit = any(isinstance(value, dict) and "explicit" in value and bool(
                    value["explicit"]) for value in aspects.values())
                if has_explicit:
                    st.subheader("The Explicit aspects in the review are:")
                    for key, value in aspects.items():
                        st.write(key)
                        if isinstance(value, dict) and "explicit" in value and value["explicit"]:
                            for k, v in value["explicit"].items():
                                st.write("  " + k + ": " + v)
                else:
                    st.write("No Explicit Aspects found in the review.")
                    

                has_implicit = any(isinstance(value, dict) and "implicit" in value and bool(
                    value["implicit"]) for value in aspects.values())

                if has_implicit:
                    st.subheader("The Implicit aspects in the review are:")
                    for key, value in aspects.items():
                        st.write(key)
                        if isinstance(value, dict) and "implicit" in value and value["implicit"]:
                            for k, v in value["implicit"].items():
                                st.write("  " + k + ": " + v)
                else:
                    st.write("No Implicit Aspects found in the review.")

            else:
                st.write("No Aspects found in the review.")

    # Show the appropriate page based on the user's choice
    if choice == "Detect Implicit Aspects":
        detect_implicit_aspects_page()
    elif choice == "About":
        about_page()


# Run the app
if __name__ == "__main__":
    app()
