from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy_utils import database_exists
# connect to oracle
import cx_Oracle

# oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'
#
# engine = create_engine(
#     oracle_connection_string.format(
#         username='USER_TRAINING',
#         password='123456',
#         hostname='192.168.74.53',
#         port='1521',
#         database='UATPTUD',
#     )
# )
oracle_connection_string = (
        'oracle+cx_oracle://{username}:{password}@' +
        cx_Oracle.makedsn('{hostname}', '{port}', service_name='{service_name}')
)

engine = create_engine(
    oracle_connection_string.format(
        username='USER_TRAINING',
        password='123456',
        hostname='192.168.74.53',
        port='1521',
        service_name='UATPTUD',
    )
)

# call to sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# create Base for model
Base = declarative_base()
