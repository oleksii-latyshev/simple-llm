import importlib
import pkgutil

import tools as _tools_package


def discover_tools() -> dict:
    """Scan the tools/ package and register every sub-package that exposes the
    required interface: TOOL_NAME, TOOL_DESCRIPTION, TOOL_ARGS_SCHEMA, execute().
    """
    registry: dict = {}
    for module_info in pkgutil.iter_modules(_tools_package.__path__):
        if not module_info.ispkg:
            continue
        module = importlib.import_module(f"tools.{module_info.name}")

        required = ("TOOL_NAME", "TOOL_DESCRIPTION", "TOOL_ARGS_SCHEMA", "execute")
        if not all(hasattr(module, attr) for attr in required):
            continue

        name = module.TOOL_NAME
        registry[name] = {
            "module": module,
            "schema": {
                "type": "function",
                "function": {
                    "name": name,
                    "description": module.TOOL_DESCRIPTION,
                    "parameters": module.TOOL_ARGS_SCHEMA.model_json_schema(),
                },
            },
        }
    return registry
