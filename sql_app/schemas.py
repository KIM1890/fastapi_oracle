from typing import List, Optional
from pydantic import BaseModel
from pydantic import EmailStr

'''Employees'''


class EmployeeBase(BaseModel):
    email: EmailStr
    name: str


class EmployeeAccount(EmployeeBase):
    password: str


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int
    department_id: int

    class Config:
        orm_mode = True


class EmployeeUpdate(EmployeeBase):
    pass


'''Department'''


class DepartmentBase(BaseModel):
    room_name: str


class DepartmentCreate(DepartmentBase):
    pass


class Department(DepartmentBase):
    id: int

    employees: List[Employee] = []

    class Config:
        orm_mode = True
