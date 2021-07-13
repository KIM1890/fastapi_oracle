from typing import List
import secrets
from fastapi import Depends, FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

from fastapi.security import HTTPBasic, HTTPBasicCredentials

'''security'''
security = HTTPBasic()


def is_authenticated(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, 'user')
    correct_password = secrets.compare_digest(credentials.password, 'pass')
    if not (correct_password and correct_username):
        raise HTTPException(status_code=401, detail='Incorrect login credentials',
                            headers={"www-Authenticate": "Basic"})
    return True


'''end security'''

# metadata for database
models.Base.metadata.create_all(bind=engine)
# tags metadata
tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]
# define app fastApi
app = FastAPI(
    description='FastAPI',
    version='2.5.0'
)
# template to gui
templates = Jinja2Templates(directory='templates')
# static to gui
app.mount('/static', StaticFiles(directory='static'), name='static')


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# '''GUI Template'''


@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    data = {
        'page': 'Home Page'
    }
    return templates.TemplateResponse('page.html', {'request': request, 'data': data})


##########################################################################################################
'''employees'''


# create employee
@app.post('/api/employee/', response_model=schemas.Employee)
def create_employee(employee_data: schemas.EmployeeCreate, department_id: int, db: Session = Depends(get_db)):
    employee_email = crud.get_employee_email(db, employee_data.email)
    if employee_email:
        raise HTTPException(status_code=400, detail='Email already registered')
    employee = crud.create_employee(db, employee_data, department_id=department_id)
    return employee


# read all employees
@app.get('/api/employees/all', tags=['All Employees'], summary='Gets all employees',
         response_model=List[schemas.Employee],
         response_description='A list containing all employee')
def read_all_employees(db: Session = Depends(get_db), auth: bool = Depends(is_authenticated)):
    list_employee = crud.get_all_employees(db)
    return list_employee


# read list employees(range limit->skip)
@app.get('/api/employees/', response_model=List[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_employee = crud.get_employees(db, skip=skip, limit=limit)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee not found')
    return db_employee


# read employee with id
@app.get('/api/employee/{employee_id}/', response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee not found')
    return db_employee


# update employee
@app.put('/employee/{employee_id}/', response_model=schemas.Employee)
def update_employee(employee_id: int, employee_data: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    """update and return"""
    # list_id_employee = list(employee_data.id)
    # if employee_id not in list_id_employee:
    #     raise HTTPException(status_code=404, detail='Employee Id Not Exist')
    '''check id have exist in db'''
    """Update and return employee"""
    employee = crud.get_employee(db, employee_id)
    db_employee = crud.update_employee(db, employee_data, employee_id)
    return db_employee


# delete employee
@app.delete('/api/employee/{employee_id}/', response_model=schemas.Employee)
def delete_employee(employee_id: int, department_id: int, db: Session = Depends(get_db)):
    crud.delete_employee(db, employee_id, department_id)
    return {'Detail': 'Employee Delete Success'}


###########################################################################################
'''Begin Department'''


# delete department
@app.delete('/api/department/{department_id}/', response_model=schemas.Department)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    crud.delete_department(db, department_id=department_id)
    return {'Detail': 'Department Delete Success'}


'''End Department'''
