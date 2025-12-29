Password Validator

A simple and efficient Python function to validate passwords against common security rules.

Features

The validator checks whether a password meets the following criteria:

Minimum length of 8 characters

Contains at least one uppercase letter

Contains at least one lowercase letter

Contains at least one digit

Contains at least one special character (from string.punctuation)

Each rule is evaluated independently, allowing you to see exactly which conditions pass or fail.

Code Overview
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

Usage
Example
result = password_validator("Secure@123")
print(result)

Output
{
    'length': True,
    'uppercase': True,
    'lowercase': True,
    'digits': True,
    'special_characters': True
}
