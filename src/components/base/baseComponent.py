class BaseComponent(object):
    """
    The base class for all components in the system. This class is meant to be subclassed by all components.
    Each component and chain should subclass this class and implement the necessary methods.
    """

    def __init__(self):
        pass

    def build(self) -> object | None:
        """
        Builds the component internally. This method should be called before running the component.
        Components return a 'langchain' object that is used to run the component in the chain.
        When building this kind of component, the 'langchain' object should be returned & stored in the chain as a
        variable. Chains don't return anything, instead they store the chain in a class variable.
        :return: The built component or None if the component is a chain
        """
        return None

    def post_run(self, data: object) -> object:
        """
        Post-processes the data after running the component or chain.
        :param data: The data to post-process
        :return: The post-processed data in the correct format
        """
        return data
