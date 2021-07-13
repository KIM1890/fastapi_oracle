from sqlalchemy.orm import Session

from . import models

########################################################################################
'''class'''


# read class with id
def get_class_id(db: Session, class_id: int):
    return db.query(models.Classes).filter(models.Classes.id == class_id).first()


'''end class'''
#########################################################################################
'''teacher'''


# read teacher with all
def get_teacher_all(db: Session):
    return db.query(models.Teacher).all()


'''end teacher'''
