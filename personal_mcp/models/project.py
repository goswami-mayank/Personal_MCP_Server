from pydantic import BaseModel, Field


class Project(BaseModel):
    name: str
    category: str
    description: str
    technologies: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)