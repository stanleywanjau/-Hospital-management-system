from sqlalchemy import Column, Integer, String,Date,Enum,or_,func
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import object_session
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy import create_engine
from datetime import datetime



from .Base import Base
engine = create_engine('sqlite:///Hospital.db')
Session = sessionmaker(bind=engine)
session = Session()
class Patient(Base):
  __tablename__ = 'patients'
  
  id= Column(Integer, primary_key=True)
  first_name= Column(String)
  last_name= Column(String)
  sex= Column(Enum('male', 'female'))
  birth_date= Column(Date)
  phone_number = Column(String)
  email=Column( VARCHAR(255))
  addmission_date= Column(Date)
  medication= Column( VARCHAR(255))
  
  appointments = relationship("Appointment",back_populates='patient')
  doctor=relationship("Doctor",secondary='appointments',back_populates='patient',viewonly=True)
  
  
  def __repr__(self):
    return f"<Patient(id={self.id},first_name={self.first_name},last_name={self.last_name},sex={self.sex},birth_date={self.birth_date},phone_number={self.phone_number},email={self.email},addmission_date={self.addmission_date},medication={self.medication})>"
  def add_patient_data(self,first_name,last_name,sex,birth_date,phone_number,email,addmission_date,medication):
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date() 
    addmission_date = datetime.strptime(addmission_date, "%Y-%m-%d").date() 
    
    patient=Patient(first_name=first_name,last_name=last_name,sex=sex,birth_date=birth_date,phone_number=phone_number,email=email,addmission_date=addmission_date,medication=medication)
    session.add(patient)
    session.commit()
  def full_name(self):
    return f"{self.first_name} {self.last_name}"
    
  def delete_patient(self,name):
    patient_to_delete =self.get_patient_by_name(name)
    if patient_to_delete:
        session.delete(patient_to_delete)
        session.commit()
        print(f"Patient with name {patient_to_delete.full_name()} deleted successfully.")
    else:
        print(f"Patient with name {name} not found.")
  
  def get_patient_by_name(self, name):
    name = name.lower()
    return session.query(Patient).filter(or_(Patient.first_name.ilike(f'%{name}%'), Patient.last_name.ilike(f'%{name}%'))).first()
  
  
  def update_patient_by_name(self, name,new_data:dict):
    patient = session.query(Patient).filter(func.lower(Patient.first_name) == name.lower()).first()
    if patient:
        for key, value in new_data.items():
            setattr(patient, key, value)
        session.commit()
        print(f"Patient with name {patient.full_name()} updated successfully.")
    else:
        print(f"Patient with name {name} not found.")

