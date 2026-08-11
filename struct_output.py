from dotenv import load_dotenv
import dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

class AWSService(BaseModel):
    service: str = Field(description="The name of the AWS service to explain.")
    category: Literal["Compute", "Storage", "Database", "Networking", "Security"] = Field(description="The category of the AWS service.")
    description: str = Field(description="A brief description of the AWS service.")
    usecases: list[str] = Field(description="A list of common use cases for the AWS service.")
    beginner_friendly: bool = Field(description="Indicates whether the explanation should be beginner-friendly.")

    #create LLM instance
    #use consistency because structured data task needs consistency in the output format
llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
       
    )

structured_llm = llm.with_structured_output(AWSService)

#send a normal language request to the model 
#Langchain ensures that returned result are strucuted as pydantic model 
result = structured_llm.invoke("Explain Amazon S3 in simple terms.")

print(result)

#convert pydantic model to dictionary
print(result.model_dump())

#access individual fields of the pydantic model
print("Recommended Use Cases:", result.usecases)
print("category:", result.category)
print("usecases:", result.usecases)


