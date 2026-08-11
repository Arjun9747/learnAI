from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()

class AWSService(BaseModel):
    service: str = Field(description = "AWS Service name:")
    description: str = Field(description = "Description of the AWS Service")
    use_case: str = Field(description = "Use case of the AWS Service")
    compute_option: str = Field(description = "Compute option of the AWS Service")


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

#creates a new LLM runnable configured to return data matching AWSService.
structured_llm = llm.with_structured_output(AWSService)
result = structured_llm.invoke("Explain Amazon ECS in simple terms.")


print(result)

