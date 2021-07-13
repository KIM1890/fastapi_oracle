from sqlalchemy.orm import Session
from . import models, schemas

########################################################################################
'''Employee'''


# create acount employee
def create_account_employee(db: Session, employee_data: schemas.EmployeeCreate):
    employee = models.Employees(name=employee_data.name, email=employee_data.email)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


# create employee with department(insert in sql)
def create_employee(db: Session, employee_data: schemas.EmployeeCreate, department_id: int):
    employee = models.Employees(name=employee_data.name, email=employee_data.email,
                                department_id=department_id)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


# Read all employees
def get_all_employees(db: Session):
    return db.query(models.Employees).all()


# Read multiple employees
def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employees).offset(skip).limit(limit).all()


# Read a single user by ID.
def get_employee(db: Session, employee_id: int):
    return db.query(models.Employees).filter(models.Employees.id == employee_id).first()


# Read employee by email
def get_employee_email(db: Session, employee_email: str):
    return db.query(models.Employees).filter(models.Employees.email == employee_email).first()


# update employee
def update_employee(db: Session, employee_data: schemas.EmployeeUpdate, employee_id: int):
    employee = db.query(models.Employees).filter(models.Employees.id == employee_id).first()
    employee.email = employee_data.email
    employee.name = employee.name
    db.commit()
    db.refresh(employee)
    return employee


# delete employee
def delete_employee(db: Session, employee_id: int, department_id: int):
    employee = db.query(models.Employees).filter(
        models.Employees.id == employee_id, models.Employees.department_id == department_id).first()
    db.delete(employee)
    db.commit()


'''End Employee'''
######################################################################################################
'''Begin Department'''


# delete department
def delete_department(db: Session, department_id: int):
    department = db.query(models.Departments).filter(models.Departments.id == id).first()
    db.delete(department)
    db.commit()


'''End Department'''
