from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)


result = llm.invoke("What is the capital of France?")

print("TYPE:")
print(type(result))

print("\nFULL RESULT:")
print(result)

print("\nCONTENT:")
print(result.content)

message = HumanMessage(
    content="What is Amazon ECS?"
)

print("MESSAGE:")
print(message)

print("\nMESSAGE TYPE:")
print(type(message))

result = llm.invoke([message])

print("\nAI RESPONSE:")
print(result)

print("\nAI RESPONSE TYPE:")
print(type(result))