# The `components` Directory

The `components` directory contains the building blocks of the chains. A component is a wrapper for a Langchain object or another object. Building a chain is done in an Object-Oriented Programming (OOP) way, so components are used to construct the chain. Components can range from tools, Large Language Models (LLMs), processors, output parsers, database tools, and more.

## Base Class (`BaseComponent`)

The `BaseComponent` class is the base class for all components and chains. It includes the following methods:

- `build`: Builds the component. If the component is a chain, it should build the chain; otherwise, it returns the Langchain object, allowing the chain to be built.
- `post_run`: Runs after the chain is executed in order to process the response into the correct output.

## Usage

1. Components are always called with the `build` method.
2. The `post_run` method is called internally after the chain is executed, usually within the `run` or `run_async` methods.
3. Each component should be built before the chain is built.
4. Each component should be a subclass of `BaseComponent`.
5. Components can contain other components, so a component can have multiple components.
6. A chain can have different components to call, allowing multiple components to be called within a single chain.
7. Components offer a lot of possibilities, so it's important to keep the code clean and modular.

---