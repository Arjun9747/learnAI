from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

llm = ChatOpenAI(
    model ="gpt-4o-mini",
    temperature=0.7
)

prompt =ChatPromptTemplate.from_messages([
    ("system","You are a senior AWS Architect."),
    ("human","Explain {service} in simple terms.")
])

#Take the output of prompt and pass it as the input to llm 
#Langchain Expression Language (LEL) allows you to use the pipe operator (|) to chain together different components in a LangChain workflow. In this case, we are chaining the prompt and the llm together so that the output of the prompt is passed as input to the llm.
chain = prompt | llm

services = [
    "Amazon S3", "Amazon ECS", "Amazon EC2"]

for service in services:
    result= chain.invoke({"service": service})

    print(f"{service}:")
    print(result.content)
    print()