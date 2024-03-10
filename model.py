from sqlalchemy import Integer, String, ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from db import db_engine

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(15))
    last_name: Mapped[str] = mapped_column(String(15))
    numbers: Mapped[list[int]] = mapped_column(ARRAY(Integer))
    addres: Mapped[str] = mapped_column(String(20), nullable=True)
    
Base.metadata.create_all(db_engine)

SessionLocal = sessionmaker(bind=db_engine)  #Creando la sesión

def get_session():
    return SessionLocal()