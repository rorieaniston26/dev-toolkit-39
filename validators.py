import re
from functools import lru_cache
from typing import Pattern

# Precompiled patterns to avoid redundant compilation during validation
_EMAIL_REGEX: Pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
_UUID_REGEX: Pattern = re.compile(r'^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$', re.IGNORECASE)

@lru_cache(maxsize=128)
def validate_email(email: str) -> bool:
    """Validates email format using cached regex check."""
    if not email:
        return False
    return bool(_EMAIL_REGEX.match(email))

@lru_cache(maxsize=128)
def validate_uuid(uuid_str: str) -> bool:
    """Validates UUID format using cached regex check."""
    if not uuid_str:
        return False
    return bool(_UUID_REGEX.match(uuid_str))

def clear_validation_cache() -> None:
    """Clears internal lru_cache for memory management."""
    validate_email.cache_clear()
    validate_uuid.cache_clear()