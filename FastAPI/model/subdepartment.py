from pydantic import BaseModel
from subdepartment_kpis import *


class subdepartmrent_kpis(BaseModel):
    SUBDEPARTMENT: [subdepartmrent_kpis]
