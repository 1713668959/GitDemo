import re

def validate_email(email):
    """Validate the email address using a regular expression."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

if __name__ == "__main__":
    test_emails = []