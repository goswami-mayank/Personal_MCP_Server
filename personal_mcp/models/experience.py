from pydantic import BaseModel, Field


class Experience(BaseModel):
    organization: str
    role: str
    description: str
    technologies: list[str] = Field(default_factory=list)
    domains: list[str] = Field(default_factory=list)