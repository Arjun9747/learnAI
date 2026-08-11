from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

parser = StrOutputParser()


# -------------------------
# Chain 1
# -------------------------

explain_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior AWS Architect."),
    ("human", "Explain {service} in simple terms.")
])

explain_chain = explain_prompt | llm | parser


# -------------------------
# Chain 2
# -------------------------

interview_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior AWS interviewer."),
    ("human", "Based on the following explanation, create 3 interview questions:\n\n{explanation}")
])

interview_chain = interview_prompt | llm | parser


# -------------------------
# Execute Chain 1
# -------------------------

explanation = explain_chain.invoke({
    "service": "Amazon ECS"
})


# -------------------------
# Execute Chain 2
# -------------------------

questions = interview_chain.invoke({
    "explanation": explanation
})


# -------------------------
# Output
# -------------------------

print("===== EXPLANATION =====")
print(explanation)

print("\n===== INTERVIEW QUESTIONS =====")
print(questions)