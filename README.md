# GitDemo

Simple repository that provides a small email utility module `GitDemo.py`.

**Files of interest**
- `GitDemo.py`: email utilities with `validate_email` and `normalize_email`, and a simple CLI.
- `tests/test_gitdemo.py`: pytest-style unit tests.
- `tests/run_tests.py`: simple test runner that does not require external packages.

**Usage (CLI)**

Run the script directly to validate email addresses or print normalized addresses:

```bash
python GitDemo.py alice@example.com
python GitDemo.py --normalize " User@Example.COM "
```

**Usage (import in Python)**

```python
from GitDemo import validate_email, normalize_email

print(validate_email("user@example.com"))        # True/False
print(normalize_email("User@Example.COM"))      # User@example.com
```

**Running tests**

This repository includes a lightweight test runner that does not depend on external packages. Run:

```bash
python -m tests.run_tests
```

If you prefer to use pytest (requires internet access to install), install it and run:

```bash
# Install (optional)
python -m pip install --user pytest

# Run pytest
pytest
```

**Notes**
- The module uses a conservative regular expression for email validation and intentionally does not implement the full RFC.
- If you don't see changes on GitHub, ensure you are logged into the correct account and that the repository is not private to another user.

---

If you want, I can also add examples, CI configuration (GitHub Actions) to run the tests, or expand the README with API details.
