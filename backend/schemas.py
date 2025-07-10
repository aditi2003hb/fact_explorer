from pydantic import BaseModel

class FactBase(BaseModel):
    category: str
    content: str

class FactCreate(FactBase):
    pass

class FactOut(FactBase):
    id: int

    class Config:
        orm_mode = True
