# Notebook Template

Notebook for exploring *AI / ML* data.

## Quickstart

First, a local project environment needs to be created, then the project's modules will be installed into locally into a virtual environment.

1. Clone the repository.

   ```sh
   git clone https://github.com/bellanov/notebook-template.git
   cd notebook-template
   ```

2. Create a virtual environment.

   ```sh
   # Create Virtual Environment
   python3 -m venv .venv

   # Activate Virtual Environment
   source .venv/bin/activate
   .\.venv\Scripts\Activate.ps1

   # Install Dependencies
   pip install -r requirements.txt -r dev-requirements.txt
   pip install -e .

   # Deactivate Virtual Environment
   deactivate
   ```

4. Create environment file(s) to store configurations.

   ```sh
   # Automatically parsed and stored in ENV dictionary.
   touch .env
   ```

5. Execute a Notebook.

   ```sh
   marimo edit notebooks/env.py
   ```

## Testing

Execute unit tests to validate the installation.

```sh
# Execute Unit Tests
scripts/test.sh
```

## Execute Notebook

*Execute* any of the Notebooks in the `notebooks/` directory using *Marimo*.

```sh
marimo run notebooks/env.py
marimo run notebooks/bar.py
```

## Edit Notebook

*Edit* any of the Notebooks in the `notebooks/` directory using *Marimo*.

```sh
marimo edit notebooks/env.py
marimo edit notebooks/bar.py
```
