# The `Chains` directory
Chains are wrappers for Langchain's, with the idea of making it easier to use in an OOP way.
Chains are basically the program being run. Each chain can be called with a `run` method, which will run the chain and return the result.
This way, applications on top of the chain can be called in an OOP way & easily swapped out. This makes testing, debugging, and maintaining the code easier.

## Base class (`BaseChain`)
- The `BaseChain` class is the base class for all chains.
- Methods: 
  - `build`: Builds the chain.
  - `run`: Runs the chain.
  - `run_async`: Runs the chain asynchronously.
  - `pre_run`: Runs before the chain is run in order to process the data for the chain.
  - `post_run`: Runs after the chain is run in order to process the response into the correct output.
- Properties:
  - `llm`: The LLM component.
  - `chain`: The chain to be run.
  - `prompt`: The prompt to be used.

## Correct usage
- Chains are always called with the `run` method.
- Before each chain is run, the `build` method should be called.
- The `pre_run` method is called internally before the chain is run, usually in the `run` or `run_async` methods.
- The `post_run` method is called internally after the chain is run, usually in the `run` or `run_async` methods.
- The `llm` property should be set to the LLM component, which is a subclass from `BaseLLM`.
- Tools, processors, metadata, and other components can also be added.
- A chain can have different chains to call, so multiple chains can be called in a single chain.
- A lot of possibilities can be done with chains, so it's important to keep the code clean and modular.