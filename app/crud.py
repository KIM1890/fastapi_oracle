from sqlalchemy.orm import Session

from . import models, schemas

########################################################################################
'''class'''


# read multiple class
def get_class_multi(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Classes).offset(skip).limit(limit).all()


# read class with id
def get_class_id(db: Session, class_id: int):
    return db.query(models.Classes).filter(models.Classes.id == class_id).first()


# update classes
def update_classes(db: Session, employee_data: schemas.EmployeeUpdate, employee_id: int):
    employee = db.query(models.Employees).filter(models.Employees.id == employee_id).first()
    employee.email = employee_data.email
    employee.name = employee.name
    db.commit()
    db.refresh(employee)
    return employee


'''end class'''
#########################################################################################
'''teacher'''


# read teacher with all
def get_teacher_all(db: Session):
    return db.query(models.Teacher).all()


'''end teacher'''
