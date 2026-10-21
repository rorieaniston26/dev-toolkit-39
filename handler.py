from typing import Dict, Any, Optional, Callable

class RequestHandler:
    """Handles incoming request processing and routing."""

    def __init__(self, routes: Dict[str, Callable[[Dict[str, Any]], Any]]) -> None:
        self._routes: Dict[str, Callable[[Dict[str, Any]], Any]] = routes

    def process_request(self, path: str, payload: Dict[str, Any]) -> Optional[Any]:
        """
        Routes a request based on path and returns the result.

        :param path: The endpoint path identifier.
        :param payload: Dictionary containing request data.
        :return: Result from the handler function or None if not found.
        """
        handler = self._routes.get(path)
        if not handler:
            return None
        
        return handler(payload)

    def register_route(self, path: str, callback: Callable[[Dict[str, Any]], Any]) -> None:
        """
        Adds a new route to the internal handler map.

        :param path: The path to register.
        :param callback: The function to execute on match.
        """
        self._routes[path] = callback

    def get_route_count(self) -> int:
        """
        Returns total number of registered routes.
        """
        return len(self._routes)