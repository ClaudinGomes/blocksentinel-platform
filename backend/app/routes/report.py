from fastapi import APIRouter
from app.models.report_schema import ProjectInput, ReportOutput
from app.services.analysis_engine import generate_report

router = APIRouter(prefix="/report", tags=["Reports"])


@router.post("/generate", response_model=ReportOutput)
def generate(project: ProjectInput):
    return generate_report(project)
