import re
from typing import Pattern

"""Simple email utilities.

Functions:
- `validate_email(email)`: returns True if the email looks valid.
- `normalize_email(email)`: strips whitespace and lowercases the domain.

This module is intentionally small and uses a conservative regex.
"""

EMAIL_PATTERN: Pattern[str] = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def validate_email(email: str) -> bool:
    """Return True if `email` matches a simple email pattern.

    The check is regex-based and intentionally conservative: it accepts
    common ASCII email forms but does not fully implement the RFC.
    Non-string inputs return False.
    """
    if not isinstance(email, str):
        return False
    email = email.strip()
    return bool(EMAIL_PATTERN.fullmatch(email))


def normalize_email(email: str) -> str:
    """Normalize an email address.

    - Strips surrounding whitespace.
    - Lowercases the domain part only (local part preserved as-is).

    Raises `TypeError` if `email` is not a string.
    """
    if not isinstance(email, str):
        raise TypeError("email must be a string")
    email = email.strip()
    if "@" in email:
        local, domain = email.rsplit("@", 1)
        return f"{local}@{domain.lower()}"
    return email.lower()


def _main(argv=None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Simple email validator")
    parser.add_argument("emails", nargs="*", help="Email addresses to check")
    parser.add_argument("--normalize", action="store_true", help="Print normalized email")
    args = parser.parse_args(argv)

    if not args.emails:
        parser.print_help()
        return 0

    for e in args.emails:
        if args.normalize:
            try:
                print(normalize_email(e))
            except TypeError:
                print(f"invalid input: {e}")
        else:
            print(f"{e}: {'VALID' if validate_email(e) else 'INVALID'}")

    return 0


if __name__ == "__main__":
    raise SystemExit(_main())

