import secrets
from typing import List

from fastapi import Depends, FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
# json
from fastapi.encoders import jsonable_encoder
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
        # "externalDocs": {
        #     "description": "Items external docs",
        #     "url": "https://fastapi.tiangolo.com/",
        # },
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


@app.get('/', tags=['Template'], response_class=HTMLResponse)
def home(request: Request):
    data = {
        'page': 'Home Page'
    }
    return templates.TemplateResponse('page.html', {'request': request, 'data': data})


##########################################################################################################
'''Class'''


# create class
@app.post('/api/classes/', tags=['Classes'], summary='Thêm lớp học',
          response_model=schemas.Classes)
def create_class(class_data: schemas.ClassCreate, db: Session = Depends(get_db),
                 auth: bool = Depends(is_authenticated)):
    db_class = crud.create_class(db, class_data)
    return db_class


# read class all
@app.get('/api/classes/all/', tags=['Classes'], summary='Lấy ra danh sách lớp học',
         response_model=List[schemas.Classes])
def get_classes_all(db: Session = Depends(get_db), auth: bool = Depends(is_authenticated)):
    db_classes = crud.get_class_all(db)
    if len(db_classes) == 0:
        raise HTTPException(detail='Hiện không có lớp học đang mở')
    return jsonable_encoder(db_classes)


# read class multiple
@app.get('/api/classes/', tags=['Classes'], summary='Lấy ra danh sách lớp học trong một khoảng nào đó',
         response_model=List[schemas.Classes])
def get_classes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),
                auth: bool = Depends(is_authenticated)):
    db_classes = crud.get_class_multi(db, skip, limit)
    return db_classes


# read class with id
@app.get('/api/classes/{id}/', tags=['Classes'], summary='Lấy ra lớp học theo mã lớp',
         response_model=schemas.Classes,
         response_description='classes id')
def get_classes_id(id: int, db: Session = Depends(get_db),
                   auth: bool = Depends(is_authenticated)):
    db_classes = crud.get_class_id(db, id)

    if db_classes is None:
        raise HTTPException(status_code=404, detail='Mã lớp học không tồn tại')
    return db_classes


# update class
@app.put('/api/classes/{id}/', tags=['Classes'], summary='Cập nhật lớp học theo mã lớp',
         response_model=schemas.Classes, response_description='Cập nhật lớp học')
def update_class_id(id: int, class_data: schemas.ClassUpdate, db: Session = Depends(get_db),
                    auth: bool = Depends(is_authenticated)):
    db_classes = crud.update_classes(id, class_data, db)

    return db_classes


# delete class
@app.delete('/api/classes/{id}/', tags=['Classes'], summary='Xóa lớp học theo mã lớp',
            response_model=schemas.Classes, response_description='Xoá lớp học')
def delete_class_id(id: int, db: Session = Depends(get_db),
                    auth: bool = Depends(is_authenticated)):
    crud.delete_classes(db, id)
    db_classes = crud.get_class_all(db)
    return db_classes


'''End Class'''
########################################################################################################
'''Teacher'''


# create teacher
@app.post('/api/teacher/', tags=['Teacher'], summary='Thêm giáo viên',
          response_model=schemas.Teacher, response_description='Thêm giáo viên')
def create_teacher(teacher_data: schemas.TeacherCreate, db: Session = Depends(get_db),
                   auth: bool = Depends(is_authenticated)):
    db_teacher = crud.create_teacher(db, teacher_data)
    return db_teacher


# get teacher all
@app.get('/api/teacher/all/', tags=['Teacher'], summary='Lấy ra tất cả các giáo viên',
         response_model=List[schemas.Teacher], response_description='Tất cả giáo viên')
def get_teacher_all(db: Session = Depends(get_db), auth: bool = Depends(is_authenticated)):
    db_teacher = crud.get_teacher_all(db)
    if len(db_teacher) == 0:
        raise HTTPException(detail='Hiện không có giáo viên')
    return db_teacher


# get teacher with id
@app.get('/api/teacher/{giaovien_id}/', tags=['Teacher'], summary='Lấy ra giáo viên theo mã giáo viên',
         response_model=schemas.Teacher, response_description='Lấy ra giáo viên theo mã giáo viên')
def get_teacher_id(giaovien_id: int, db: Session = Depends(get_db),
                   auth: bool = Depends(is_authenticated)):
    db_teacher = crud.get_teacher_id(db, giaovien_id)

    if db_teacher is None:
        raise HTTPException(status_code=404, detail='Mã giáo viên không tồn tại')
    return db_teacher


# update teacher with id
@app.put('/api/teacher/{giaovien_id}/', tags=['Teacher'], summary='Cập nhật thông tin giáo viên',
         response_model=schemas.Teacher, response_description='Cập nhật thông tin')
def update_teacher_id(giaovien_id: int, teacher_data: schemas.TeacherUpdate,
                      db: Session = Depends(get_db),
                      auth: bool = Depends(is_authenticated)):
    db_teacher = crud.update_teacher_id(db, teacher_data, giaovien_id)
    return db_teacher


# delete teacher with id
@app.delete('/api/teacher/{giaovien_id}/', tags=['Teacher'], summary='Xoá thông tin giáo viên',
            response_model=schemas.Teacher, response_description='Xóa giáo viên')
def delete_teacher_id(giaovien_id: int, db: Session = Depends(get_db)):
    crud.delete_teacher_id(db, giaovien_id)
    return "Delete success"


'''End Teacher'''
