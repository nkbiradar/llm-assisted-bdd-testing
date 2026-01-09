ALLOWED_KEYWORDS = ["login", "username", "password", "click"]

def validate_scenarios(text):
    print("Validating generated scenarios...")
    return any(word in text.lower() for word in ALLOWED_KEYWORDS)
