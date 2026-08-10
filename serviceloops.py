from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)
services = ["ECS", "S3", "Lambda", "DynamoDB"]

#invoking the llm with a simple string prompt
for service in services:
    result = llm.invoke(
        f"Explain {service} in simple terms."
    )
    print(f"{service}:")
    print(f"{result.content}")
    print()