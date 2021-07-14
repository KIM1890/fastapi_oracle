import secrets
from typing import List

from fastapi import Depends, FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

'''security'''
security = HTTPBasic()


def is_authenticated(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, 'liendtk')
    correct_password = secrets.compare_digest(credentials.password, '123456')
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
        "name": "Classes",
        "description": "Lớp Học",
    },
    {
        "name": "Teacher",
        "description": "Giáo Viên",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]
# define app fastApi
app = FastAPI(
    description='FastAPI',
    version='2.5.0',
    openapi_tags=tags_metadata
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


'''GUI Template'''

#
# @app.get('/', tags=['Template'], response_class=HTMLResponse)
# def home(request: Request):
#     data = {
#         'page': 'Home Page'
#     }
#     return templates.TemplateResponse('page.html', {'request': request, 'data': data})
#

##########################################################################################################
'''Class'''
# create class
'''code in here'''


# read class all
@app.get('/api/classes/all/', tags=['Classes'], summary='Lấy ra tất cả lớp học',
         response_model=List[schemas.Classes])
def get_classes_all(db: Session = Depends(get_db), auth: bool = Depends(is_authenticated)):
    db_classes = crud.get_class_all(db)
    return db_classes


# read class multiple
@app.get('/api/classes/', tags=['Classes'], summary='Lấy ra danh sách lớp học',
         response_model=List[schemas.Classes])
def get_classes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),
                auth: bool = Depends(is_authenticated)):
    db_classes = crud.get_class_multi(db, skip, limit)
    return db_classes


# read class with id
@app.get('/api/classes/{class_id}/', tags=['Classes'], summary='Lấy ra lớp học theo mã lớp',
         response_model=schemas.Classes,
         response_description='classes id')
def get_classes_id(class_id: int, db: Session = Depends(get_db),
                   auth: bool = Depends(is_authenticated)):
    db_classes = crud.get_class_id(db, class_id)
    return db_classes


# update class
'''code in here'''


# delete class
@app.delete('/api/classes/{class_id}/', tags=['Classes'], summary='Xóa lớp học theo mã lớp',
            response_model=schemas.Classes, response_description='Xoá lớp học')
def delete_class_id(class_id: int, db: Session = Depends(get_db),
                    auth: bool = Depends(is_authenticated)):
    crud.delete_classes(db, class_id)
    return 'Delete success'


'''End Class'''
########################################################################################################
'''Teacher'''


@app.get('/api/teacher/all/', tags=['Teacher'], summary='Lấy ra tất cả các giáo viên',
         response_model=List[schemas.Teacher], response_description='Teacher all')
def get_teacher_all(db: Session = Depends(get_db), auth: bool = Depends(is_authenticated)):
    db_teacher = crud.get_teacher_all(db)
    return db_teacher


'''End Teacher'''
