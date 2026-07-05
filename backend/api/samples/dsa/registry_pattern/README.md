# Registry Pattern

Summary of the *Registry Pattern* and its usage.

## Description

The **Registry Pattern** is a central store for objects/classes, allowing lookup by name. It provides a central location for your application to access functionality, rather than duplicating code or imports across multiple files.

**Key Benefits:**

- *Decoupling* — callers don't import concrete classes directly
- *Extensibility* — add new implementations without changing existing code
- *Dynamic Dispatch* — select behavior at runtime from a string key
- *Common real-world uses:* plugin systems, serializers, command handlers, and ML model registries.

## Solutions

The solution uses a class to create central location to register and access various **plugins** responsible for *exporting* data into various formats. A **decorator** is used to provide a convenient method of *registering* additional plugins.

```python
class PluginRegistry:
    _registry = {}

    @classmethod
    def register(cls, name):
        """Decorator to register a plugin by name."""
        def decorator(plugin_cls):
            cls._registry[name] = plugin_cls
            return plugin_cls
        return decorator

    @classmethod
    def get(cls, name):
        if name not in cls._registry:
            raise KeyError(f"Plugin '{name}' not found. Available: {list(cls._registry)}")
        return cls._registry[name]


# --- Registering implementations ---

@PluginRegistry.register("csv")
class CsvExporter:
    def export(self, data):
        return f"Exporting {data} as CSV"

@PluginRegistry.register("json")
class JsonExporter:
    def export(self, data):
        return f"Exporting {data} as JSON"

# --- Using the registry ---

format_type = "json"
exporter = PluginRegistry.get(format_type)()
print(exporter.export({"key": "value"}))
# Output: Exporting {'key': 'value'} as JSON
```

For instance, adding a new plugin is as simple as declaring a new class using the decorator.

In this example, a new plugin for exporting to Excel is being implemented.

```python
@PluginRegistry.register("excel")
class ExcelExporter:
    def export(self, data):
        return f"Exporting {data} as EXCEL"
```