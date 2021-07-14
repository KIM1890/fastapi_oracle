from sqlalchemy.orm import Session

from . import models, schemas

########################################################################################
'''class'''


# create classes


def create_class(db: Session, class_data: schemas.ClassCreate, class_id: int):
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
    return db.query(models.Classes).all()


# read class with id
def get_class_id(db: Session, class_id: int):
    return db.query(models.Classes).filter(models.Classes.id == class_id).first()


# update classes
def update_classes(db: Session, classes_data: schemas.ClassUpdate, class_id: int):
    classes = db.query(models.Classes).filter(models.Classes.id == class_id).first()
    # employee.email = employee_data.email
    # employee.name = employee.name
    db.commit()
    db.refresh(classes)
    return classes


# delete classes
def delete_classes(db: Session, class_id: int):
    db_classes = db.query(models.Classes).filter(models.Classes.id == class_id).first()
    db.delete(db_classes)
    db.commit()


'''end class'''
#########################################################################################
'''teacher'''


# read teacher with all
def get_teacher_all(db: Session):
    return db.query(models.Teacher).all()


'''end teacher'''
