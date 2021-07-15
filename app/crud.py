from sqlalchemy.orm import Session
import json
from . import schemas
from .models import Classes, Teacher
from fastapi import HTTPException


# convert list to dict
def convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct


########################################################################################
'''class'''


# create classes


def create_class(db: Session, class_data: schemas.ClassCreate):
    # giaovienc = [{'giaovienID': 4, 'giaovienName': 'Trinh Van Quang', 'Code': '2'}]
    classes = Classes(id=class_data.id, giaovienc=json.dumps(class_data.giaovienc))
    db.add(classes)
    db.commit()
    db.refresh(classes)
    return classes


# read multiple class
def get_class_multi(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Classes).offset(skip).limit(limit).all()


# read all class
def get_class_all(db: Session):
    db_class = db.query(Classes).all()
    return db_class


# read class with id
def get_class_id(db: Session, id: int):
    return db.query(Classes).filter(Classes.id == id).first()


# update classes
def update_classes(id: int, classes_data: schemas.ClassUpdate, db: Session):
    db_classes = db.query(Classes).filter(Classes.id == id).first()
    if db_classes is None:
        raise HTTPException(status_code=404, detail='Mã lớp không tồn tại')
    db_classes.giaovienc = json.dumps(classes_data.giaovienc)
    db.add(db_classes)
    db.commit()
    db.refresh(db_classes)
    return db_classes


# delete classes
def delete_classes(db: Session, id: int):
    db_classes = db.query(Classes).filter(Classes.id == id).first()
    if db_classes is None:
        raise HTTPException(status_code=404, detail='Mã lớp không tồn tại')
    db.delete(db_classes)
    db.commit()


'''end class'''
#########################################################################################
'''teacher'''


# create teacher
def create_teacher(db: Session, teacher_data: schemas.TeacherCreate):
    teacher = Teacher(giaovien_id=teacher_data.giaovien_id, giaovien_name=teacher_data.giaovien_name,
                      lophoc_id=teacher_data.lophoc_id)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher


# read teacher with all
def get_teacher_all(db: Session):
    return db.query(Teacher).all()


# read teacher with id
def get_teacher_id(db: Session, giaovien_id: int):
    return db.query(Teacher).filter(Teacher.giaovien_id == giaovien_id).first()


# update teacher with id
def update_teacher_id(db: Session, teacher_data: schemas.TeacherUpdate, giaovien_id: int):
    db_teacher = db.query(Teacher).filter(Teacher.giaovien_id == giaovien_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail='Mã giáo viên không tồn tại')
    db_teacher.giaovien_name = teacher_data.giaovien_name
    db_teacher.lophoc_id = teacher_data.lophoc_id
    db.commit()
    db.refresh(db_teacher)
    return db_teacher


# delete teacher with id
def delete_teacher_id(db: Session, giaovien_id: int):
    db_teacher = db.query(Teacher).filter(Teacher.giaovien_id == giaovien_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=404, detail='Mã giáo viên không tồn tại')
    db.delete(db_teacher)
    db.commit()


'''end teacher'''
