from detection_modules.preprocessing import (
    tokenize_words,
    stem_token,
    clean_text,
    clean_array,
)


def detect_implicit_aspects(review, nlp):
    purchased_keywords = {
        "explicit": ["bought", "purchased", "ordered"],
        "noun": [
            "acquired",
            "got",
            "obtained",
            "picked",
            "selected",
            "chose",
            "decided",
            "gathered",
            "gifted",
        ],
        "adj": ["new", "latest"],
    }
    age_keywords = {
        "explicit": [
            "old",
            "new",
            "fresh",
            "latest",
            "current",
            "up-to-date",
            "modern",
            "contemporary",
            "recently released",
            "state-of-the-art",
            "cutting-edge",
            "latest technology",
            "newest model/version",
            "just released",
            "recently launched",
            "years",
        ],
        "noun": ["qwerty", "analog"],
        "adj": [
            "vintage",
            "outdated",
            "retro",
            "recent",
            "out-of-date",
            "ancient",
            "modern",
            "obsolete",
        ],
    }
    performance_keywords = {
        "explicit": ["perform", "performance"],
        "noun": [
            "work",
            "work well",
            "work efficiently",
            "function",
            "functionality",
            "operate",
            "run",
            "execute",
        ],
        "adj": [
            "Smooth",
            "Snappy",
            "fast",
            "responsive",
            "reliable",
            "efficient",
            "dynamic",
            "beast",
        ],
    }
    design_keywords = {
        "explicit": ["design", "appearance", "look"],
        "noun": ["style", "shape", "form", "structure", "outline", "configuration"],
        "adj": [
            "sleek",
            "beautiful",
            "elegant",
            "stylish",
            "minimalistic",
            "attractive",
            "eyecatching",
            "futuristic",
            "classy",
            "slim",
            "compact",
            "aesthetic",
            "comfortable ",
        ],
    }
    screen_keywords = {
        "explicit": [
            "screen",
            "display",
        ],
        "noun": [
            "monitor",
            "view",
            "picture",
            "image",
            "resolution",
            "size",
            "ratio",
            "brightness",
            "contrast",
            "pixel",
            "color",
            "viewing",
            "touchscreen",
            "amoled",
            "lcd",
            "oled",
            "refresh rate",
            "bezel",
            "hdr",
            "notch",
            "protector",
        ],
        "adj": [
            "clear",
            "sharp",
            "vivid",
            "bright",
            "dim",
            "dull",
            "high-resolution",
            "low-resolution",
            "color-rich",
            "anti-galre" "color-accurate",
            "wide-angle",
            "narrow-angle",
            "responsive",
            "smooth",
            "fast",
            "slow",
            "immersive",
            "reflective",
            "glare-free",
            "huge",
        ],
    }
    battery_keywords = {
        "explicit": [
            "battery",
        ],
        "noun": [
            "power",
            "energy",
            "charge",
            "duration",
            "life",
            "capacity",
            "runtime",
            "endurance",
            "lasting",
            "dead",
            "capacity",
            "usage",
            "drain",
            "charging time",
            "charging",
            "wireless",
            "health",
            "saver mode",
            "backup",
            "consumption",
            "charging port",
            "endurance",
        ],
        "adj": [
            "long-lasting",
            "efficient",
            "reliable",
            "powerful",
            "fast-charging",
            "wireless",
            "low-power",
            "durable",
            "energy-saving",
            "sustainable",
            "eco-friendly",
            "dependable",
        ],
    }
    brand_keywords = {
        "explicit": [
            "brand",
            "manufacturer",
        ],
        "noun": [
            "make",
            "producer",
            "label",
            "logo",
            "identity",
            "reputation",
            "status",
            "name",
            "popularity",
            "market share",
            "innovation",
            "customer support",
            "product lineup",
            "availability",
            "connectivity",
            "accessories",
            "warranty",
        ],
        "adj": [
            "popular",
            "reliable",
            "innovative",
            "iconic",
            "trusted",
            "sophisticated",
            "highquality",
            "technologically advanced",
            "user-friendly",
            "cutting-edge",
            "durable",
            "versatile",
            "efficient",
            "longlasting",
            "advanced",
            "competitive",
        ],
    }
    cost_keywords = {
        "explicit": ["price", "cost", "value", "worth"],
        "noun": ["expense", "payment", "amount", "fee", "charge", "budget", "sale"],
        "adj": [
            "low-end",
            "mid-range",
            "high-end",
            "expensive",
            "affordable",
            "costly",
            "reasonable",
            "budgetfriendly",
            "pricey",
            "inexpensive",
            "valuable",
            "cheap",
            "economical",
            "highpriced",
            "overpriced",
            "premium",
            "discounted",
            "competitive",
            "worthwhile",
            "over-budget",
            "extravagant",
            "Low-cost",
            "Pocketfriendly",
        ],
    }
    camera_keywords = {
        "explicit": ["cameras"],
        "noun": [
            "photography",
            "lens",
            "shot",
            "picture",
            "image",
            "snapshot",
            "focus",
            "flash",
            "resolution",
            "aperture",
            "zoom",
            "megapixel",
            "autofocus",
            "shutter",
            "stabilization",
            "hdr",
            "lowlight",
            "depth perception",
            "selfie",
            "video",
            "motion",
            "mode",
            "panorama",
            "telephoto",
            "ultrawide",
            "night mode",
            "macro",
            "bokeh",
        ],
        "adj": [
            "clear",
            "sharp",
            "detailed",
            "vivid",
            "bright",
            "colorful",
            "fast",
            "accurate",
            "low noise",
            "crisp",
            "dynamic",
            "balanced",
            "professional",
            "artistic",
            "smooth",
            "consistent",
            "stunning",
            "natural",
            "impressive",
        ],
    }
    os_keywords = {
        "explicit": ["operating system"],
        "noun": [
            "android",
            "ios",
            "windows",
            "windows",
            "Kaios",
            "harmonyos",
            "lineage os",
            "oxygen os",
            "oxygen",
            "miui",
            "color os",
            "color",
            "realme ui",
            "interface",
            "customization",
            "compatibility",
            "security",
            "stability",
            "updates",
            "integration",
            "navigation",
            "multitasking",
            "accessibility",
            "functionality",
            "efficiency",
            "control",
            "interface",
            "operating system version",
            "compatibility",
            "ai",
        ],
        "adj": [
            "intuitive",
            "efficient",
            "customizable",
            "seamless",
            "secure",
            "reliable",
            "stable",
            "fast",
            "responsive",
            "user",
            "robust",
            "versatile",
            "innovative",
            "modern",
            "streamlined",
            "fluid",
            "dynamic",
            "adaptive",
            "consistent",
        ],
    }
    experience_keywords = {
        "explicit": ["experience"],
        "noun": [
            "feeling",
            "impression",
            "perception",
            "sensation",
            "judgment",
            "opinion",
            "attitude",
            "reaction",
            "view",
        ],
        "adj": [
            "memorable",
            "pleasant",
            "unforgettable",
            "challenging",
            "exciting",
            "educational",
            "unique",
            "incredible",
            "fulfilling",
            "inspiring",
            "refreshing",
            "empowering",
            "eyeopening",
            "rewarding",
            "intense",
            "engaging",
            "transformative",
            "relaxing",
            "disappointing",
            "frustrating",
            "superb",
        ],
    }

    phone_keywords = {
        "subjects": ["phone", "smartphone", "cell", "device", "handset"],
        "adjectives": [
            "awesome",
            "fantastic",
            "cool",
            "superb",
            "perfect",
            "bad",
            "trash",
            "worst",
        ],
    }

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
        filtered_words = list(
            filter(
                bool,
                map(
                    clean_text,
                    clean_array(
                        [
                            word
                            for word in tokenize_words(sentence)
                            if word.lower() not in nlp.Defaults.stop_words
                        ]
                    ),
                ),
            )
        )

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
                    Aspect_Dict["explicit"][
                        element
                    ] = "The age of the phone is mentioned."

            for element in age_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][
                        element
                    ] = "The age of the phone is mentioned."

            for element in age_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][
                        element
                    ] = "The age of the phone is mentioned."

            # for every element in performance explicit list
            for element in performance_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][
                        element
                    ] = "The phone's performance is discussed."

            for element in performance_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][
                        element
                    ] = "The phone's performance is discussed."

            for element in performance_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][
                        element
                    ] = "The phone's performance is discussed."

            # for every element in design explicit list
            for element in design_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][
                        element
                    ] = "The design of the phone is mentioned."

            for element in design_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][
                        element
                    ] = "The design of the phone is mentioned."

            for element in design_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][
                        element
                    ] = "The design of the phone is mentioned."

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
                    Aspect_Dict["explicit"][
                        element
                    ] = "The Operating System is Mentioned."

            for element in os_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][
                        element
                    ] = "The Operating System is Mentioned."

            for element in os_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][
                        element
                    ] = "The Operating System is Mentioned."

            # for every element in experience explicit list
            for element in experience_keywords["explicit"]:
                if stem_token(element) in arr:
                    Aspect_Dict["explicit"][
                        element
                    ] = "The overall experience with the phone is discussed."

            for element in experience_keywords["noun"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][
                        element
                    ] = "The overall experience with the phone is discussed."

            for element in experience_keywords["adj"]:
                if stem_token(element) in arr:
                    Aspect_Dict["implicit"][
                        element
                    ] = "The overall experience with the phone is discussed."

        check_every_keyword(filtered_words)
        if len(Aspect_Dict["subject"]) > 0:
            if stem_token(Aspect_Dict["subject"][0]) in phone_keywords["subjects"]:
                if len(Aspect_Dict["adjective"]) > 0:
                    if (
                        stem_token(Aspect_Dict["adjective"][0])
                        in phone_keywords["adjectives"]
                    ):
                        Aspect_Dict["implicit"][
                            Aspect_Dict["subject"][0]
                        ] = "The Phone as whole is described."

    return aspects
