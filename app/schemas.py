from typing import List, Optional
from pydantic import BaseModel
from pydantic import EmailStr

'''Teacher'''


class TeacherBase(BaseModel):
    giaovien_name: str
    lophoc_id: int


class TeacherCreate(TeacherBase):
    giaovien_id: int


class Teacher(TeacherBase):
    giaovien_id: int
    lophoc_id: str

    class Config:
        orm_mode = True


class TeacherUpdate(TeacherBase):
    pass


'''Class'''


class ClassBase(BaseModel):
    pass


class ClassCreate(ClassBase):
    giaovienc: Optional[dict] = None


class Classes(ClassBase):
    GIAOVIEN: List[Teacher] = []

    class Config:
        orm_mode = True


class ClassUpdate(ClassBase):
    giaovienc: Optional[dict] = None
