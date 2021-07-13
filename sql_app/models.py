from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Departments(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String, unique=True, index=True)

    employees = relationship('Employees', back_populates='departments', cascade="all, delete-orphan")


class Employees(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    department_id = Column(Integer, ForeignKey('departments.id'))

    departments = relationship('Departments', back_populates='employees')
