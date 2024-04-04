# The `models` directory
Models define what goes in and out of a given component. They are the interface between the component and the rest of the application.

## Correct usage
- Define the model in the `models` directory.
- For each component, it's best to have a separate model file.
- Subdirectories can be used to group related models.
- The model should be a class or an interface.
- A `main` file should be used to keep models that are used in multiple, or all components.