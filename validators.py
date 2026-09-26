import re
from typing import Optional

# Standard validation regular expressions
EMAIL_REGEX = re.compile(r"^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$")
URL_REGEX = re.compile(r"^https?://[^\\s/$.?#].[^\\s]*$")


def is_valid_email(email: Optional[str]) -> bool:
    """Validate if the provided string is a properly formatted email address.

    Args:
        email: The string to validate.

    Returns:
        True if the string is a valid email, False otherwise.
    """
    if not email:
        return False
    return bool(EMAIL_REGEX.match(email))


def is_valid_url(url: Optional[str]) -> bool:
    """Validate if the provided string is a properly structured URL.

    Args:
        url: The string to validate.

    Returns:
        True if the string is a valid URL, False otherwise.
    """
    if not url:
        return False
    return bool(URL_REGEX.match(url))


def is_strong_password(password: Optional[str], min_length: int = 8) -> bool:
    """Check if the password meets basic strength criteria.

    Criteria:
    - At least the minimum specified length.
    - Contains at least one uppercase letter.
    - Contains at least one lowercase letter.
    - Contains at least one digit.

    Args:
        password: The password string to evaluate.
        min_length: The minimum required length (default is 8).

    Returns:
        True if the password meets all criteria, False otherwise.
    """
    if not password or len(password) < min_length:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    return has_upper and has_lower and has_digit
