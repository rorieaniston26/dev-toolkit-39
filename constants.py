from typing import Final, Dict, Any

# Application configuration defaults
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# API status codes
STATUS_SUCCESS: Final[int] = 200
STATUS_CREATED: Final[int] = 201
STATUS_BAD_REQUEST: Final[int] = 400
STATUS_UNAUTHORIZED: Final[int] = 401
STATUS_NOT_FOUND: Final[int] = 404
STATUS_SERVER_ERROR: Final[int] = 500

# Supported environment mapping
ENV_MAPPING: Final[Dict[str, str]] = {
    "dev": "development",
    "stg": "staging",
    "prd": "production"
}

def get_status_message(code: int) -> str:
    """
    Return the standard message for a given HTTP status code.

    :param code: The integer HTTP status code.
    :return: Human-readable status description.
    """
    messages: Dict[int, str] = {
        200: "Success",
        201: "Resource Created",
        400: "Bad Request",
        401: "Unauthorized Access",
        404: "Resource Not Found",
        500: "Internal Server Error"
    }
    return messages.get(code, "Unknown Status Code")