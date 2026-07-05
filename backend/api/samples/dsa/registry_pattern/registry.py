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
            raise KeyError(
                f"Plugin '{name}' not found. Available: {list(cls._registry)}"
            )
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


@PluginRegistry.register("excel")
class ExcelExporter:
    def export(self, data):
        return f"Exporting {data} as EXCEL"


# --- Using the registry ---


def main() -> None:
    format_type = "json"
    exporter = PluginRegistry.get(format_type)()
    print(exporter.export({"key": "value"}))
    # Output: Exporting {'key': 'value'} as JSON


if __name__ == "__main__":
    main()
