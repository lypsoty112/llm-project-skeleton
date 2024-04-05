# The `models` Directory

The `models` directory contains the data structures and interfaces that define the input and output of each component. These models serve as the interface between the components and the rest of the application.

## Usage

1. **Define Models**: Define the models in the `models` directory.

2. **Separate Files**: For each component, it's best to have a separate model file.

3. **Subdirectories**: Use subdirectories to group related models.

4. **Model Structure**: A model should be defined as a class or an interface.

5. **Main File**: Use a `main` file to keep models that are used across multiple or all components.

Example structure:

```
models/
├── __init__.py
├── main.py             # Models used across multiple components
├── component1/
│   ├── __init__.py
│   └── model1.py       # Model for component1
└── component2/
    ├── __init__.py
    ├── model2.py       # Model for component2
    └── related_model.py
```

In this example:

- `main.py` contains models used by multiple components.
- `component1` has its own `model1.py` file.
- `component2` has `model2.py` and `related_model.py` for related models.

By following this structure, the models are organized and easy to maintain, while also providing a clear interface between the components and the application.