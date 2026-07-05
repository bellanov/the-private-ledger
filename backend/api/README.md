# python-samples

A series of Python *samples* are available spanning the categories below.

| Sample | Description |
|---|---|
| [*args_kwargs*](https://github.com/bellanov/python-samples/tree/main/samples/args_kwargs) | Overview of *args & kwargs* and their usage. |
| [*assert*](https://github.com/bellanov/python-samples/tree/main/samples/assert) | Overview of *assert* and its usage. |
| [*asychronous_programming*](https://github.com/bellanov/python-samples/tree/main/samples/asychronous_programming) | Overview of *Asynchronous Programming* in Python. |
| [*classes*](https://github.com/bellanov/python-samples/tree/main/samples/classes) | Overview of *Classes / Object-Oriented Programming (OOP)* and their usage. |
| [*control_flow*](https://github.com/bellanov/python-samples/tree/main/samples/control_flow) | Overview of *Control Flow* and its usage. |
| [*counters*](https://github.com/bellanov/python-samples/tree/main/samples/counters) | Overview of *Counters* and their usage. |
| [*defaultdict*](https://github.com/bellanov/python-samples/tree/main/samples/defaultdict) | Overview of *defaultdict* and its usage. |
| [*dictionaries*](https://github.com/bellanov/python-samples/tree/main/samples/dictionaries) | Overview of *Dictionaries* and their usage. |
| [*dsa*](https://github.com/bellanov/python-samples/tree/main/samples/dsa) | Data Structures and Algorithms (DSA). |
| [*exceptions*](https://github.com/bellanov/python-samples/tree/main/samples/exceptions) | Overview of *Exceptions* and their usage. |
| [*functions*](https://github.com/bellanov/python-samples/tree/main/samples/functions) | Overview of *Functions* and their usage. |
| [*hello_world*](https://github.com/bellanov/python-samples/tree/main/samples/hello_world) | A very simple *Python* program. |
| [*introduction*](https://github.com/bellanov/python-samples/tree/main/samples/introduction) | A general introduction to the *Python* programming language. |
| [*iterables_and_generators*](https://github.com/bellanov/python-samples/tree/main/samples/iterables_and_generators) | Overview of *Iterables & Generators* and their usage. |
| [*list_comprehensions*](https://github.com/bellanov/python-samples/tree/main/samples/list_comprehensions) | Overview of *List Comprehensions* and their usage. |
| [*lists*](https://github.com/bellanov/python-samples/tree/main/samples/lists) | Overview of *Lists* and their usage. |
| [*modules*](https://github.com/bellanov/python-samples/tree/main/samples/modules) | Overview of *Modules* and their usage. |
| [*randomness*](https://github.com/bellanov/python-samples/tree/main/samples/randomness) | Overview of *Randomness* in Python. |
| [*regex*](https://github.com/bellanov/python-samples/tree/main/samples/regex) | Overview of *Regular Expressions* in Python. |
| [*sets*](https://github.com/bellanov/python-samples/tree/main/samples/sets) | Overview of *Sets* and their usage. |
| [*sorting*](https://github.com/bellanov/python-samples/tree/main/samples/sorting) | Overview of *Sorting* and its usage. |
| [*strings*](https://github.com/bellanov/python-samples/tree/main/samples/strings) | Overview of *Strings* and their usage. |
| [*truthiness*](https://github.com/bellanov/python-samples/tree/main/samples/truthiness) | Overview of *Truthiness* in Python. |
| [*tuples*](https://github.com/bellanov/python-samples/tree/main/samples/tuples) | Overview of *Tuples* and their usage. |
| [*type_annotations*](https://github.com/bellanov/python-samples/tree/main/samples/type_annotations) | Overview of *Type Annotations* in Python. |
| [*virtual_environments*](https://github.com/bellanov/python-samples/tree/main/samples/mvirtual_environments) | Overview of *Virtual Environments* and their usage. |
| [*whitespace_formatting*](https://github.com/bellanov/python-samples/tree/main/samples/whitespace_formatting) | Overview of *Whitespace Formatting* in Python. |
| [*zip_argument_unpacking*](https://github.com/bellanov/python-samples/tree/main/samples/zip_argument_unpacking) | Overview of *zip & Argument Unpacking* in Python. |

## Script Execution

First, a local project environment needs to be created, then the project's modules will be installed into locally into a virtual environment.

1. Clone the repository.

   ```sh
   git clone https://github.com/bellanov/python-template.git
   cd python-template
   ```

2. Create a virtual environment.

   ```sh
   # Create Virtual Environment
   python3 -m venv .venv

   # Activate Virtual Environment
   
   # Linux
   source .venv/bin/activate

   # Windows
   .venv\Scripts\activate
   .venv\Scripts\Activate.ps1

   # Install all dependencies (runtime and development)
   pip install -e ".[dev]"

   # Deactivate Virtual Environment
   deactivate
   ```

## Testing, Linting, and Formatting

Execute the tests to validate your installation.

### Linux

```sh
scripts/test.sh
```

### Windows

```sh
.\scripts\test.ps1
```