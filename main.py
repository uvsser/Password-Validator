from string import punctuation


def password_validator(password: str) -> dict[str, bool]:
    
    # optimization: Convert punctuation string to a Set.
    special_chars = set(punctuation)

    # We build a dictionary to check ALL conditions independently.
    validator = {
        'length': len(password) >= 8,
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'digits': any(c.isdigit() for c in password),
        'special_characters': any(c in special_chars for c in password)
    }

    return validator
