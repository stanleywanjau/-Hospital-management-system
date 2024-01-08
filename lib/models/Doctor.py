from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import object_session

# Base = declarative_base()
from .Base import Base


class Doctor(Base):
  __tablename__ = 'doctors'
  
  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  department=Column(String)
  phone = Column(Integer)
  
  appointments = relationship("Appointment",back_populates='doctor')
  
  def __repr__(self):
    return f"<doctor(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, department={self.department}, phone={self.phone})>"
  
  