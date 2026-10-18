"""Task and request handler framework for dev-toolkit-39."""

import time
from typing import Any, Callable, Dict, List, Optional


class BaseHandler:
    """Abstract base handler for processing toolkit requests."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._middlewares: List[Callable[[Dict[str, Any]], Dict[str, Any]]] = []

    def use(self, middleware: Callable[[Dict[str, Any]], Dict[str, Any]]) -> None:
        """Register middleware function for pre-processing payloads."""
        self._middlewares.append(middleware)

    def _apply_middleware(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        data = payload.copy()
        for mw in self._middlewares:
            data = mw(data)
        return data


class TaskHandler(BaseHandler):
    """Handler for registering and executing toolkit commands."""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._registry: Dict[str, Callable[..., Any]] = {}

    def register(self, command: str, func: Callable[..., Any]) -> None:
        """Bind a command keyword to a callable function."""
        self._registry[command] = func

    def handle(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Process incoming command payloads through middleware and execution."""
        processed = self._apply_middleware(payload)
        command = processed.get("command")

        if not command or command not in self._registry:
            return {
                "status": "error",
                "message": f"Unknown command: {command}",
                "timestamp": time.time(),
            }

        handler_fn = self._registry[command]
        kwargs = processed.get("args", {})

        try:
            result = handler_fn(**kwargs)
            return {
                "status": "success",
                "result": result,
                "timestamp": time.time(),
            }
        except Exception as err:
            return {
                "status": "failed",
                "error": str(err),
                "timestamp": time.time(),
            }
