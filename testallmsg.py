from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(
    model ="gpt-4o-mini",
    temperature=0.7
)

result = llm.invoke("what is the capital of France?")

system_message = SystemMessage(
    content="You are a Senior AWS architect."
)

human_message = HumanMessage(
    content="What is Amazon ECS?"
)

messages = [system_message, human_message]

result1 = llm.invoke(messages)

print("First Response:")
print(result1.content)

messages.append(result1)

result2=llm.invoke(messages)

print("\nSecond Response:")
print(result2.content)