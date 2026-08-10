from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7 
)

prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a AWS Senior Architect"),
     ("human", "Explain {service} in simple terms.")]
)

parser = StrOutputParser()

#The output of one becomes the input of the next.
chain = prompt | llm | parser

result = chain.invoke({"service": "Amazon ECS"})

print(result)
