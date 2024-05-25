# The `Chains` Directory

This directory contains the chains of the project. Chains are wrappers for Langchain's components, designed to make it easier to use them in an Object-Oriented Programming (OOP) way. Chains are essentially the programs being run. Each chain can be called with a `run` method, which will execute the chain and return the result. This approach allows applications built on top of the chains to be called in an OOP manner, making it easier to swap out components, test, debug, and maintain the code.

## Base Class (`BaseChain`)

The `BaseChain` class is the base class for all chains. It includes the following methods and properties:

### Methods

- `build`: Builds the chain.
- `run`: Runs the chain.
- `run_async`: Runs the chain asynchronously.
- `pre_run`: Runs before the chain is executed in order to process the data for the chain.
- `post_run`: Runs after the chain is executed in order to process the response into the correct output.

### Properties

- `llm`: The Large Language Model (LLM) component.
- `chain`: The chain to be executed.
- `prompt`: The prompt to be used.

## Usage

1. Chains are always called with the `run` method.
2. Before executing each chain, the `build` method should be called.
3. The `pre_run` method is called internally before the chain is executed, usually within the `run` or `run_async` methods.
4. The `post_run` method is called internally after the chain is executed, usually within the `run` or `run_async` methods.
5. The `llm` property should be set to the LLM component, which is a subclass of `BaseLLM`.
6. Additional components, such as tools, processors, metadata, and others, can also be added.
7. A chain can have different chains to call, allowing multiple chains to be executed within a single chain.
8. Chains offer a lot of possibilities, so it's essential to keep the code clean and modular.
