import pytest

from GitDemo import validate_email, normalize_email


@pytest.mark.parametrize(
    "email,expected",
    [
        ("user@example.com", True),
        (" user@example.com ", True),
        ("user.name+tag@sub.example.co.uk", True),
        ("invalid@@example.com", False),
        ("no-at-symbol.example.com", False),
        (123, False),
    ],
)
def test_validate_email_param(email, expected):
    assert validate_email(email) is expected


def test_normalize_email_lowercases_domain():
    assert normalize_email("User@Example.COM") == "User@example.com"


def test_normalize_email_strips_whitespace():
    assert normalize_email("  alice@EXAMPLE.COM  ") == "alice@example.com"


def test_normalize_non_string_raises():
    with pytest.raises(TypeError):
        normalize_email(123)
