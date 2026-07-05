"""Development / Optional Dependencies.

Overview of *Development / Optional Dependencies* in Python projects.

Optional dependencies allow projects to specify different groups of dependencies
for different use cases.
"""


def demo_dependency_structure() -> dict:
    """Demonstrate the structure of optional dependencies."""
    dependencies_structure = {
        "core": ["# Always installed", "requests"],
        "optional_groups": {
            "ml": ["numpy", "scikit-learn"],
            "aws": ["boto3"],
            "dev": ["pytest", "black"],
        },
    }
    return dependencies_structure


def demo_pyproject_toml() -> str:
    """Demonstrate pyproject.toml structure."""
    pyproject = """[project]
name = "my_project"
version = "0.1.0"
dependencies = [
    "requests",  # Always installed
]

[project.optional-dependencies]
ml = ["numpy", "scikit-learn"]
aws = ["boto3"]
dev = ["pytest", "black"]
"""
    return pyproject


def demo_pip_install_commands() -> dict:
    """Demonstrate different pip install commands."""
    commands = {
        "core_only": "pip install .",
        "ml_dependencies": "pip install .[ml]",
        "aws_dependencies": "pip install .[aws]",
        "dev_dependencies": "pip install .[dev]",
        "multiple_groups": "pip install .[ml,aws,dev]",
    }
    return commands


def demo_poetry_structure() -> str:
    """Demonstrate Poetry-based dependency management."""
    poetry = """[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.28.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0"
black = "^22.0"

[tool.poetry.group.ml.dependencies]
numpy = "^1.20"
scikit-learn = "^1.0"
"""
    return poetry


def demo_requirements_txt() -> str:
    """Demonstrate requirements.txt format."""
    req_file = """# Core requirements
requests>=2.28.0

# To install with dev dependencies:
# pip install -r requirements.txt -r requirements-dev.txt
"""
    return req_file


def demo_why_optional_dependencies() -> list:
    """List reasons for using optional dependencies."""
    reasons = [
        "Smaller install footprint for basic users",
        "Clear separation of concerns (core vs. extras)",
        "Easier dependency management",
        "Reduced conflicts in dependency trees",
        "Different users get what they need",
    ]
    return reasons


def main() -> None:
    """Demonstrate development dependency concepts."""
    # Show dependency structure
    structure = demo_dependency_structure()
    assert "core" in structure
    assert "optional_groups" in structure
    print("✓ Dependency structure understood")

    # Show pyproject.toml format
    pyproject = demo_pyproject_toml()
    assert "[project.optional-dependencies]" in pyproject
    assert "ml = " in pyproject
    print("✓ pyproject.toml format understood")

    # Show pip install commands
    commands = demo_pip_install_commands()
    assert "pip install ." in commands["core_only"]
    assert "[ml]" in commands["ml_dependencies"]
    print("✓ Pip install commands understood")

    # Show Poetry structure
    poetry = demo_poetry_structure()
    assert "tool.poetry.dependencies" in poetry
    assert "tool.poetry.group" in poetry
    print("✓ Poetry structure understood")

    # Show requirements.txt
    req = demo_requirements_txt()
    assert "requirements" in req
    print("✓ Requirements.txt format understood")

    # Show reasons for optional dependencies
    reasons = demo_why_optional_dependencies()
    assert len(reasons) > 0
    print("✓ Reasons for optional dependencies identified")

    print("\nAll development dependency concepts demonstrated successfully!")
    print("\nBest Practices:")
    print("- Use pyproject.toml for modern Python projects")
    print("- Group dependencies by purpose (dev, ml, aws, etc.)")
    print("- Keep core dependencies minimal")
    print("- Document which extras to install for different use cases")
    print("- Use requirements.txt for lock files")


if __name__ == "__main__":
    main()
