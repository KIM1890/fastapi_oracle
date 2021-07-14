from sqlalchemy.orm import Session

from . import models, schemas

########################################################################################
'''class'''


# create classes


def create_class(db: Session, class_data: schemas.ClassCreate):
    classes = models.Classes(id=class_data.id)
    db.add(classes)
    db.commit()
    db.refresh(classes)
    return classes


# read multiple class
def get_class_multi(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Classes).offset(skip).limit(limit).all()


# read all class
def get_class_all(db: Session):
    db_class = db.query(models.Classes).all()
    return db_class


# read class with id
def get_class_id(db: Session, lophoc_id: int):
    return db.query(models.Classes).filter(models.Classes.id == lophoc_id).first()


# update classes
def update_classes(db: Session, classes_data: schemas.ClassUpdate, lophoc_id: int):
    classes = db.query(models.Classes).filter(models.Classes.id == lophoc_id).first()
    # employee.email = employee_data.email
    # employee.name = employee.name
    db.commit()
    db.refresh(classes)
    return classes


# delete classes
def delete_classes(db: Session, lophoc_id: int):
    db_classes = db.query(models.Classes).filter(models.Classes.id == lophoc_id).first()
    db.delete(db_classes)
    db.commit()


'''end class'''
#########################################################################################
'''teacher'''


# create teacher
def create_teacher(db: Session, teacher_data: schemas.TeacherCreate):
    teacher = models.Teacher(giaovien_id=teacher_data.giaovien_id, giaovien_name=teacher_data.giaovien_name,
                             lophoc_id=teacher_data.lophoc_id)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher


# read teacher with all
def get_teacher_all(db: Session):
    return db.query(models.Teacher).all()


# read teacher with id
def get_teacher_id(db: Session, giaovien_id: int):
    return db.query(models.Teacher).filter(models.Teacher.giaovien_id == giaovien_id).first()


# update teacher with id
def update_teacher_id(db: Session, teacher_data: schemas.TeacherUpdate, giaovien_id: int):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.giaovien_id == giaovien_id).first()
    db_teacher.giaovien_name = teacher_data.giaovien_name
    db_teacher.lophoc_id = teacher_data.lophoc_id
    db.commit()
    db.refresh(db_teacher)
    return db_teacher


# delete teacher with id
def delete_teacher_id(db: Session, giaovien_id: int):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.giaovien_id == giaovien_id).first()
    db.delete(db_teacher)
    db.commit()


'''end teacher'''
