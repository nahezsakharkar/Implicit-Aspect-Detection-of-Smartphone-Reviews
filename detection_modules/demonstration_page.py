from detection_modules.data import reviews
from detection_modules.demonstration import find_reviews_wrt_aspects
from detection_modules.preprocessing import process_text_conjunctions_demonstration


def demonstration_page(st, nlp):
    # Custom HTML and CSS
    html_code = """
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
            </style>
    """

    # Streamlit app
    st.markdown(html_code, unsafe_allow_html=True)

    st.header("Demonstration of Real Life Usecase")
    st.divider()
    st.subheader("Select from the Aspects to fetch corresponding Reviews")

    (
        col1,
        col2,
        col3,
        col4,
        col5,
        col6,
        col7,
        col8,
        col9,
        col10,
        col11,
        col12,
        col13,
        col14,
    ) = st.columns([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    with col1:
        camera_aspect = st.button("Camera")

    with col2:
        performance_aspect = st.button("Performance")

    with col3:
        design_aspect = st.button("Design")

    with col4:
        screen_aspect = st.button("Screen")

    with col5:
        interactibility_aspect = st.button("Interactibility")

    with col6:
        battery_aspect = st.button("Battery")

    with col7:
        brand_aspect = st.button("Brand")

    with col8:
        cost_aspect = st.button("Cost")

    with col9:
        os_aspect = st.button("OS")

    with col10:
        experience_aspect = st.button("Experience")

    with col11:
        phone_aspect = st.button("Phone")

    with col12:
        age_aspect = st.button("Age")

    with col13:
        purchased_aspect = st.button("Purchased")

    with col14:
        all_aspect = st.button("All")

    st.divider()

    if camera_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on Camera. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("camera", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on Camera. Please wait.",
            )

        my_bar.empty()

    elif performance_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on Performance. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("performance", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on Performance. Please wait.",
            )

        my_bar.empty()

    elif design_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on Design. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("design", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on Design. Please wait.",
            )

        my_bar.empty()

    elif screen_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on Screen. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("screen", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on Screen. Please wait.",
            )

        my_bar.empty()

    elif interactibility_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on Interactibility. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("interactibility", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on Interactibility. Please wait.",
            )

        my_bar.empty()

    elif battery_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on Battery. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("battery", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on Battery. Please wait.",
            )

        my_bar.empty()

    elif brand_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on Brand. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("brand", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on Brand. Please wait.",
            )

        my_bar.empty()

    elif cost_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on Cost. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("cost", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on Cost. Please wait.",
            )

        my_bar.empty()

    elif os_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on OS. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("os", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on OS. Please wait.",
            )

        my_bar.empty()

    elif experience_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on Experience. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("experience", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on Experience. Please wait.",
            )

        my_bar.empty()

    elif phone_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on Phone. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("phone", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on Phone. Please wait.",
            )

        my_bar.empty()

    elif age_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on Age. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("age", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on Age. Please wait.",
            )

        my_bar.empty()

    elif purchased_aspect:
        percentage = 0
        my_bar = st.progress(
            percentage, text="Filtering Reviews based on Purchase. Please wait."
        )
        for index, review in enumerate(reviews):
            percentage_review = int(((index + 1) * 100) / len(reviews))
            for sentence in process_text_conjunctions_demonstration(review):
                part = find_reviews_wrt_aspects("purchased", sentence, nlp)
                if part is not None:
                    st.caption(part)

            # progress_value += percentage_review - percentage
            my_bar.progress(
                percentage_review - percentage,
                text="Filtering Reviews based on Purchase. Please wait.",
            )

        my_bar.empty()

    elif all_aspect:
        for review in reviews:
            st.caption(review)

    else:
        for review in reviews:
            st.caption(review)
