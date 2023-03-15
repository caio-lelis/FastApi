from typing import Optional

from pydantic import BaseModel as SCBaseModel

#ressaltar que podemos ter diferentes modelos para um mesmo esquema.

class CursoSchema(SCBaseModel):
    id : Optional [int]
    titulo: str
    aulas: int
    horas: int
    
    class Config:
        orm_mode=True
