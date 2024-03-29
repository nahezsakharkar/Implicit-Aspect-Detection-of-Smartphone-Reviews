import streamlit as st

# preprocessor import
from detection_modules.preprocessing import nlp

# pages import
from about_page import about
from detection_modules.detection_page import detect_implicit_aspects_page
from detection_modules.demonstration_page import demonstration_page


# Streamlit app
def app():
    st.set_page_config(
        page_title="Implicit Aspect Detection",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("Implicit Aspect Detection from Smartphone Reviews")

    menu = ["Detect Implicit Aspects", "Demonstration", "About"]
    choice = st.sidebar.selectbox("Select an option", menu)

    # Define the pages
    def about_page():
        about(st)

    def detect_aspects_page():
        detect_implicit_aspects_page(st, nlp)

    def demonstrate_reviews_page():
        demonstration_page(st, nlp)

    # Show the appropriate page based on the user's choice
    if choice == "Detect Implicit Aspects":
        detect_aspects_page()
    elif choice == "Demonstration":
        demonstrate_reviews_page()
    elif choice == "About":
        about_page()


# Run the app
if __name__ == "__main__":
    app()
