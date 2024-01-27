from sqlalchemy import create_engine
from employees.models import Base

def db_tables_setup():
    engine = create_engine("mysql+mysqlconnector://mko:Knf_2505@localhost/Mko_db")
    Base.metadata.create_all(engine)