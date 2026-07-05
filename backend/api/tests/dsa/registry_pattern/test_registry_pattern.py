"""Unit tests for registry pattern sample."""

import pytest

from samples.dsa.registry_pattern.registry import (
    CsvExporter,
    ExcelExporter,
    JsonExporter,
    PluginRegistry,
)


@pytest.mark.unit
def test_plugin_registry_get_json():
    """Test getting JSON exporter from registry."""
    exporter_cls = PluginRegistry.get("json")
    assert exporter_cls == JsonExporter


@pytest.mark.unit
def test_plugin_registry_get_csv():
    """Test getting CSV exporter from registry."""
    exporter_cls = PluginRegistry.get("csv")
    assert exporter_cls == CsvExporter


@pytest.mark.unit
def test_plugin_registry_get_excel():
    """Test getting Excel exporter from registry."""
    exporter_cls = PluginRegistry.get("excel")
    assert exporter_cls == ExcelExporter


@pytest.mark.unit
def test_csv_exporter_export():
    """Test CSV exporter export method."""
    exporter = CsvExporter()
    result = exporter.export({"key": "value"})
    assert "CSV" in result
    assert "key" in result or "value" in result


@pytest.mark.unit
def test_json_exporter_export():
    """Test JSON exporter export method."""
    exporter = JsonExporter()
    result = exporter.export({"key": "value"})
    assert "JSON" in result


@pytest.mark.unit
def test_excel_exporter_export():
    """Test Excel exporter export method."""
    exporter = ExcelExporter()
    result = exporter.export({"key": "value"})
    assert "EXCEL" in result


@pytest.mark.unit
def test_plugin_registry_get_nonexistent():
    """Test getting a nonexistent plugin raises KeyError."""
    with pytest.raises(KeyError):
        PluginRegistry.get("nonexistent")
