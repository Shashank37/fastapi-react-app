from pydantic import BaseModel


class LEAF_KPI(BaseModel):
    DOMAIN: str
    INDUSTRY: str
    SECTOR: str
    CLASSIFICATION: str
    DEPARTMENT: str
    SUBDEPARTMENT: str
    KPIS: str
    EXPLANATION: str
    FORMULA: str
    DeptID: int
