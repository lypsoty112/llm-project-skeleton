# The `components` directory
Components can be seen as the building blocks of the chain. A component is, once again,
a wrapper for a Langchain object, or another object. Building a chain is also done in 
an OOP way, so components are used to build the chain. Components range from tools, LLM's, 
processors, output parsers, database tools, and more.

## Base class (`BaseComponent`)
The `BaseComponent` class is the base class for all components & chains. It has the following methods:
- `build`: Builds the component. If the component is a chain, it should build the chain, otherwise it returns the langchain object, so the chain can be built.
- `post_run`: Runs after the chain is run in order to process the response into the correct output.

## Correct usage
- Components are always called with the `build` method.
- The `post_run` method is called internally after the chain is run, usually in the `run` or `run_async` methods.
- Each component should be built before the chain is built.
- Each component should be a subclass of `BaseComponent`.
- Components can contain other components, so a component can have multiple components.
- A chain can have different components to call, so multiple components can be called in a single chain.
- A lot of possibilities can be done with components, so it's important to keep the code clean and modular.