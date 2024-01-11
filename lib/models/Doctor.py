from sqlalchemy import Column, Integer, String,func
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import object_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# Base = declarative_base()
from .Base import Base
engine = create_engine('sqlite:///Hospital.db')
Session = sessionmaker(bind=engine)
session = Session()

class Doctor(Base):
  __tablename__ = 'doctors'
  
  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  department=Column(String)
  phone = Column(Integer)
  
  appointments = relationship("Appointment",back_populates='doctor')
  patient= relationship("Patient",secondary='appointments' ,back_populates='doctor',viewonly=True)
  
  def __repr__(self):
    return f"<doctor(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, department={self.department}, phone={self.phone})>"

  def patients(self):
        return self.patient

  def appointment(self):
    return self.appointments
  def full_name(self):
    return f"{self.first_name} {self.last_name}"
  def add_doctor(self,first_name,last_name,department,phone):
    doctor=Doctor(first_name=first_name,last_name=last_name,department=department,phone=phone)
    session.add(doctor)
    session.commit()
  def get_doctors(self):
    return session.query(Doctor).all()

  def get_doctor_by_name(self, name):
    return (
            session.query(Doctor)
            .filter(func.lower(Doctor.first_name).ilike(func.lower(f"%{name}%")) | func.lower(Doctor.last_name).ilike(func.lower(f"%{name}%")))
            .first()
        )


  def get_doctor_appointments(self, name):
    doctor = self.get_doctor_by_name(name)

    if doctor:
        return doctor.appointments
    else:
        return None
        
  
  def delete_doctor(self, name):
    delete_doc= self.get_doctor_by_name(name)
    if delete_doc :
      session.delete(delete_doc)
      session.commit()
      print(f"Doctor with Name {name} deleted successfully.")
    else:
      print(f"Doctor with Name {name} not found.")