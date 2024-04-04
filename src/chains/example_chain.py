from langchain_core.runnables import Runnable
from langchain.prompts.chat import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.chains.llm import LLMChain

from src.chains.baseChain import BaseChain
from src.components.llm.example_llm import ExampleLLM
from src.models.example_model import ExampleChainInput, ExampleChainOutput

PROMPT = """Your task is to respond to the human. However, each response should be crafted 
with a high degree of sarcasm. Use irony, exaggeration, or ridicule to mock or convey contempt in your answers. 
Remember, the goal is to provide some kind of response, but mainly to infuse each answer with a strong sense of 
sarcasm. Good luck!
"""


class ExampleChain(BaseChain):
    def __init__(self):
        super().__init__()
        self._llm = ExampleLLM(chat=True)
        self.llm_name: str = self._llm.llm_name
        self.chain_name: str = "example-chain"
        self.prompt: str = PROMPT

    def build(self) -> None:
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", PROMPT),
            MessagesPlaceholder(variable_name="conversation"),
            ("human", "{input}")
        ])
        built_llm = self._llm.build()
        self._chain = LLMChain(llm=built_llm, prompt=prompt_template)

    def run(self, data: ExampleChainInput) -> ExampleChainOutput:
        pre_data = self.pre_run(data)
        response = self._chain.invoke(pre_data)
        return self.post_run(response)

    async def run_async(self, data: ExampleChainInput) -> ExampleChainOutput:
        pre_data = self.pre_run(data)
        response = await self._chain.ainvoke(pre_data)
        return self.post_run(response)

    def pre_run(self, data: ExampleChainInput) -> dict:
        # Iterate over the messages and extract the content
        data_messages = data.messages.copy()
        data_messages.sort(key=lambda x: x.timestamp)
        messages: list[AIMessage | HumanMessage | SystemMessage] = [
            AIMessage(message.content) if message.role == "ai" else
            HumanMessage(message.content) if message.role == "human" else
            SystemMessage(message.content)
            for message in data_messages
        ]

        conversation = messages[:-1][-6:]
        last_message = messages[-1]

        return {"conversation": conversation, "input": last_message.content}

    def post_run(self, data: dict) -> ExampleChainOutput:
        return ExampleChainOutput(response=data["text"], metadata=data.get("metadata", {}))
