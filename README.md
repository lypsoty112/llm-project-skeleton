# llm-project-skeleton
This project is a skeleton for projects that can be used as a starting point for easily creating an LLM-project using Langchain
in an OOP way. It simplifies the process of building chains & components, and provides a structure for the project.

## Modules
- [**chains**](src/chains/readme.md) - Contains the chains of the project.
- [**components**](src/components/readme.md) - Contains the components of the project.
- [**models**](src/models/readme.md) - Contains the models of the project.

## Correct usage
- In the project root, create a virtual environment, and any application logic you want to add on top of the skeleton, such as a `main.py` file, a fastapi server, etc.
- Make sure to install the correct dependencies in the virtual environment.
- In the `main.py` file, import the chain(s) you want to use, build & run them.
- Make sure to run the `startup` method first, or remove it if not needed.

## Modularity
- The project is modular, and can be easily extended by adding new chains, components, or models.
- The chains, components, and models are all separate, and can be used independently of each other.
- The chains can be built using the components.
- The components can be used independently of the chains.

## Extra components
- Other components can be added to the project by creating new files & directories in the `components` directory.
- Chains can call other chains, thereby creating a chain of chains.
- Components can be reused across chains.
- Models can be used to define the data structures used in the project.
- The project can be extended by adding new chains, components, or models.
- The project can be used to build complex chains using simple components.