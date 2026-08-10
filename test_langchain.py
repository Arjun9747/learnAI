from langchain_openai import ChatOpenAI


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