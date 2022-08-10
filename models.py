from sqlalchemy import Column, Integer, String

from sqlalchemy.types import Date

from database import Base

class Record(Base):
    __tablename__ = "pysparktab"
    __table_args__ = {'extend_existing': True} 
    key = Column(Integer, primary_key=True)
    value = Column(String(255), primary_key=True)