#                     User
#                      │
#                      ▼
#              AWS AI Architect
#                      │
#                  LangGraph
#                      │
#         ┌────────────┼────────────┐
#         ▼            ▼            ▼
#        RAG          Tools       Memory
#         │            │            │
#         ▼            ▼            ▼
#    AWS Docs       AWS APIs    Conversation
#         │            │
#         └────────────┼────────────┘
#                      ▼
#                     LLM
#                      │
#                      ▼
#           Architecture Recommendation


# User question
#      ↓
# LangGraph
#      ↓
# Prompt
#      ↓
# LLM
#      ↓
# AWS Architecture Recommendation




from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)


explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior AWS Architect."),
    ("human", "Explain {service} in simple terms.")
])

parser = StrOutputParser()

#create chain 1
explain_chain = explain_prompt | llm | parser

#create second prompt which expects explanation as input and generates interview questions based on that explanation
interview_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior AWS Architect."),
    ("human", "Based on this AWS service explanation, create 3 interview questions:\n\n{explanation}")
])

#create chain 2
interview_chain = interview_prompt | llm | parser

#                  Chain 1
# Amazon ECS ─────────────────→ ECS explanation
#                                   │
#                                   ↓
#                  Chain 2
#                          explanation
#                               ↓
#                      3 interview questions

explanation = explain_chain.invoke({"service": "Amazon ECS"})

explanation = explain_chain.invoke({
    "service": "Amazon ECS"
})

interview_questions = interview_chain.invoke({
    "explanation": explanation
})

print("Explanation:")
print(explanation)

print("\nInterview Questions:")
print(interview_questions)

