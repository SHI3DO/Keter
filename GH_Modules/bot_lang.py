import json


async def load_text(lang: str, text: str):
    try:
        with open("langs/" + lang + ".json", "r", encoding="UTF-8") as f:
            locale_dict = json.load(f)
        return locale_dict[text]
    except KeyError:
        return "Error: Language Text Not Found"
    except FileNotFoundError:
        return "Error: Language File Not Found"
