A simple and efficient Python function to validate passwords against common security rules.

Features:

The validator checks whether a password meets the following criteria:

Minimum length of 8 characters

Contains at least one uppercase letter

Contains at least one lowercase letter

Contains at least one digit

Contains at least one special character (from string.punctuation)

Each rule is evaluated independently, allowing you to see exactly which conditions pass or fail.

Usage example:
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

