import sys
import os

# Ensure repository root is on sys.path so we can import GitDemo.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from GitDemo import validate_email, normalize_email


def run():
    failed = 0

    cases = [
        ("user@example.com", True),
        (" user@example.com ", True),
        ("user.name+tag@sub.example.co.uk", True),
        ("invalid@@example.com", False),
        ("no-at-symbol.example.com", False),
        (123, False),
    ]

    for email, expected in cases:
        try:
            result = validate_email(email)
            assert result is expected
        except AssertionError:
            print(f"FAIL validate_email: {email!r} -> {result!r} (expected {expected!r})")
            failed += 1

    try:
        assert normalize_email("User@Example.COM") == "User@example.com"
        assert normalize_email("  alice@EXAMPLE.COM  ") == "alice@example.com"
    except AssertionError:
        print("FAIL normalize_email tests")
        failed += 1

    try:
        try:
            normalize_email(123)
            print("FAIL normalize_email should have raised TypeError for non-string")
            failed += 1
        except TypeError:
            pass
    except Exception:
        print("FAIL unexpected error in normalize_email non-string test")
        failed += 1

    if failed:
        print(f"Tests completed: {failed} failure(s)")
        return 1
    print("All tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(run())
