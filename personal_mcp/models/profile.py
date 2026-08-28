from typing import Any

from pydantic import BaseModel, Field


class Education(BaseModel):
    degree: str
    institution: str
    percentage: float | None = None


class Profile(BaseModel):
    name: str
    title: str
    location: str | None = None
    summary: str
    education: list[Education] = Field(default_factory=list)
    professional_focus: list[str] = Field(default_factory=list)
    current_interests: list[str] = Field(default_factory=list)