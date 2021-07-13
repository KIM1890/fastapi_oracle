from typing import List, Optional
from pydantic import BaseModel
from pydantic import EmailStr

'''Teacher'''


class TeacherBase(BaseModel):
    giaovien_name: str


class TeacherCreate(TeacherBase):
    pass


class Teacher(TeacherBase):
    giaovien_id: int
    lophoc_id: str

    class Config:
        orm_mode = True


'''Class'''


class ClassBase(BaseModel):
    pass


class ClassCreate(ClassBase):
    pass


class Classes(ClassBase):
    id: str
    GIAOVIEN: List[Teacher] = []

    class Config:
        orm_mode = True


class ClassUpdate(ClassBase):
    pass
