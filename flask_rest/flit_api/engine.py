from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

from langchain import hub
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from .credentials import key
import os

class ChatProcessor:
    def __init__(self):
        os.environ['OPENAI_API_KEY'] = key
        self.vectorstore = Chroma(persist_directory="flask_rest/flit_api/embeddings/Flit_Product_Knowledge", embedding_function=OpenAIEmbeddings())
        self.retriever = self.vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=1)

        self.contextualize_q_system_prompt = """Given a chat history and the latest user question \
            which might reference context in the chat history, formulate a standalone question \
            which can be understood without the chat history. Do NOT answer the question, \
            just reformulate it if needed and otherwise return it as is."""

        self.contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.contextualize_q_system_prompt),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}"),
            ]
        )
        self.contextualize_q_chain = self.contextualize_q_prompt | self.llm | StrOutputParser()

        self.qa_system_prompt = """
            Use the following pieces of context to answer the question at the end.\
            If you don't know the answer tell the customer to tap the call button on top right to ask in person. \
            don't try to make up an answer.\
            keep the answer as concise as possible. \
            When assisting customers, always be polite and professional. \
            Listen actively to their concerns and provide helpful information. \
            Use the same language as question but do not translate product names. When mentioning products mention it's name and size.
        {context}"""

        self.qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.qa_system_prompt),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}"),
            ]
        )

    def generate_history(self, chat_history):
        # Split the chat history at every -br- to get a list of messages
        messages = chat_history.split(" -br- ")

        # Extract human and AI pairs
        _messages = []

        for msg in messages:
            if msg.startswith("_h_:"):
                _messages.append(HumanMessage(content=msg.split(":")[1].strip()))
            elif msg.startswith("_ai_:"):
                _messages[-1] = AIMessage(content=msg.split(":")[1].strip())

        return _messages


    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def contextualized_question(self, input: dict):
        if input.get("chat_history"):
            return self.contextualize_q_chain
        else:
            return input["question"]

    def initialize_rag_chain(self):
        return (
            RunnablePassthrough.assign(
                context=self.contextualized_question | self.retriever | self.format_docs
            )
            | self.qa_prompt
            | self.llm
        )
