from faker import Faker
from sqlalchemy import create_engine,func
from sqlalchemy.orm import sessionmaker
from datetime import time
from models.Doctor import Doctor
from models.Appointment import Appointment
from models.Patient import Patient
from models.Base import Base
# Configure Faker
fake = Faker()

# Connect to the database
engine = create_engine('sqlite:///Hospital.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
session.query(Doctor).delete()
session.query(Patient).delete()
session.query(Appointment).delete()

def generate_fake_data():
    # Generate fake doctors
    for _ in range(5):  # Adjust the number of doctors as needed
        doctor = Doctor(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            department=fake.random_element(elements=('Cardiology', 'Orthopedics', 'Dermatology')),
            phone=fake.random_int(min=1000000000, max=9999999999)
        )
        session.add(doctor)

    # Generate fake patients
    for _ in range(10):  # Adjust the number of patients as needed
        patient = Patient(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            sex=fake.random_element(elements=('male', 'female')),
            birth_date=fake.date_of_birth(),
            phone_number=fake.random_int(min=1000000000, max=9999999999),
            email=fake.email(),
            addmission_date=fake.date_this_decade(),
            medication=fake.word()
        )
        session.add(patient)

    # Generate fake appointments
    for _ in range(15):  # Adjust the number of appointments as needed
        appointment = Appointment(
            doctor=session.query(Doctor).order_by(func.random()).first(),
            patient=session.query(Patient).order_by(func.random()).first(),
            Appointment_date=fake.date_this_year(),
            start_time=time(fake.random_int(min=0, max=23), fake.random_int(min=0, max=10)),
            end_time=time(fake.random_int(min=0, max=23), fake.random_int(min=0, max=10)),
            notes=fake.text()
        )
        session.add(appointment)

    session.commit()

if __name__ == '__main__':
    generate_fake_data()
