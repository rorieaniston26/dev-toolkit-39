import re

# regex patterns for general toolkit input validation
EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
NUMERIC_PATTERN = re.compile(r'^\d+$')

def validate_input(data: dict, schema: dict) -> bool:
    """checks if data satisfies the provided type schema"""
    for key, expected_type in schema.items():
        if key not in data:
            return False
        if not isinstance(data[key], expected_type):
            return False
    return True

def sanitize_string(value: str) -> str:
    """strips whitespace and enforces basic safety"""
    return str(value).strip()

def is_valid_email(email: str) -> bool:
    """verifies format of user provided email strings"""
    return bool(EMAIL_PATTERN.match(email))

def is_valid_numeric(value: str) -> bool:
    """verifies that string input consists only of digits"""
    return bool(NUMERIC_PATTERN.match(value))

# validation schemas for core processing loop
PROCESS_SCHEMA = {
    "user_id": int,
    "task_name": str,
    "priority": int
}