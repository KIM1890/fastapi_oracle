from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.oracle import CLOB
from .database import Base


class Teacher(Base):
    __tablename__ = 'GIAOVIEN'

    giaovien_id = Column(Integer, primary_key=True, index=True)
    giaovien_name = Column(String, index=True)
    lophoc_id = Column(Integer, ForeignKey('LOPHOC.id'), index=True)

    classes = relationship('Classes', back_populates='teacher')


class Classes(Base):
    __tablename__ = 'LOPHOC'

    id = Column(Integer, primary_key=True, index=True)
    giaovienc = Column(CLOB)

    teacher = relationship('Teacher', back_populates='classes')
