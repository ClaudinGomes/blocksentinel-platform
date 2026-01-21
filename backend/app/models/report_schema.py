from pydantic import BaseModel
from typing import List


class ProjectInput(BaseModel):
    name: str
    category: str
    description: str


class RiskItem(BaseModel):
    area: str
    level: str
    notes: str


class ReportOutput(BaseModel):
    project_name: str
    overall_risk: str
    risks: List[RiskItem]
    summary: str
