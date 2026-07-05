# Development / Optional Dependencies

In the `pyproject.toml` file you can use **optional dependencies** that are organized by section.

Here’s an example of the `pyproject.toml` file:

```toml
[project]
name = “my_project”
version = “0.1.0”
dependencies = [
    “requests”,  # Always installed
]

[project.optional-dependencies]
ml = [“numpy”, “scikit-learn”]
aws = [“boto3”]
dev = [“pytest”, “black”]
```

You can install them with the following commands:

```toml
# Install only core dependencies
pip install .

# Install machine learning dependencies
pip install .[ml]

# Install AWS dependencies
pip install .[aws]

# Install dev dependencies
pip install .[dev]
```