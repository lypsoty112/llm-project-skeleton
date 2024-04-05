# LLM Project Skeleton

This project is a skeleton for projects that can be used as a starting point for easily creating an LLM-project using Langchain in an Object-Oriented Programming (OOP) way. It simplifies the process of building chains and components, and provides a structure for the project.

## Modules

### [**Chains**](src/chains/readme.md)

This module contains the chains of the project. Chains are sequential sets of operations that can be performed on data, such as natural language processing tasks.

### [**Components**](src/components/readme.md)

This module contains the components of the project. Components are individual building blocks that can be combined to create chains.

### [**Models**](src/models/readme.md)

This module contains the models of the project. Models are data structures that represent the information used in the project.

## Usage

1. In the project root, create a virtual environment.
2. Install the required dependencies in the virtual environment.
3. Create any additional application logic you want, such as a `main.py` file or a FastAPI server.
4. In your application logic file (e.g., `main.py`), import the chain(s) you want to use, build, and run them.
5. If necessary, run the `startup` method before running your chains. If not needed, you can remove this method.

## Modularity

- The project is modular and can be easily extended by adding new chains, components, or models.
- The chains, components, and models are separate and can be used independently of each other.
- Chains can be built using the available components.
- Components can be used independently of the chains.

## Extensibility

- Additional components can be added to the project by creating new files and directories in the `components` directory.
- Chains can call other chains, thereby creating a chain of chains.
- Components can be reused across multiple chains.
- Models can be used to define the data structures used in the project.
- The project can be extended by adding new chains, components, or models.
- The project can be used to build complex chains using simple components.

---