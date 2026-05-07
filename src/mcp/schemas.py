from pydantic import BaseModel, Field

class ReadPromptSchema(BaseModel):
    prompt_id: str = Field(..., description="The unique ID of the prompt to retrieve from the registry.")

class WritePromptSchema(BaseModel):
    prompt_id: str = Field(..., description="The target prompt ID.")
    new_content: str = Field(..., description="The completely optimized prompt text.")
    version_tag: str = Field(..., description="Version tag for snapshotting (e.g., v1.1).")
    
class ProbeExecutionSchema(BaseModel):
    prompt_content: str = Field(..., description="The prompt content to test.")
    suite_id: str = Field(..., description="The ID of the behavioral probe suite to execute.")