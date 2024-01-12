from models.Doctor import Doctor, Base, engine
from models.Appointment import Appointment
from models.Patient import Patient
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



Base.metadata.create_all(engine)
engine = create_engine('sqlite:///Hospital.db')
Session = sessionmaker(bind=engine)
session = Session()

# Instantiate a doctor object for testing
doctor =Doctor()
# all=doctor.patients()
# for r in all:
#     print(r)
test_doctor = Doctor(first_name="John", last_name="Doe", department="Cardiology", phone=1234567890)

# Add the doctor to the database
doctor.add_doctor(test_doctor.first_name, test_doctor.last_name,test_doctor.department, test_doctor.phone)

# Retrieve all doctors from the database
all_doctors = doctor.get_doctors()
print("All Doctors:")
for doctor in all_doctors:
    print(doctor)



specific_doctor_id = 2  # Replace with a valid doctor ID


# Get appointments for a specific doctor
appointments = doctor.get_doctor_appointments(specific_doctor_id)
print(f"\nAppointments for Doctor with ID {specific_doctor_id}:")
for appointment in appointments:
    print(appointment)


# Retrieve a doctor by name
retrieved_doctor = doctor.get_doctor_by_name("John", "Doe")
print("\nDoctor retrieved by name:")
print(retrieved_doctor)

print("\ndeleted by id:")
doctor_to_delete_id = 6  # Replace with the actual ID of the doctor you want to delete
doctor.delete_doctor(doctor_to_delete_id)

#appointment methods
appointment =Appointment()
print("\nprint all appointment:")
all_appointments = appointment.get_appointment()
for appointment in all_appointments:
    print (appointment)

print("\nadding appointment")
#print the number of appointment before
before_appointments = appointment.get_appointment()
print(f"\nNumber of appointments before adding: {len(before_appointments)}")

# Add a new appointment

appointment.add_appointment(doctor_id=1, patient_id=1, appointment_date="2024-01-09", start_time="09:00:00", end_time="10:00:00", notes="Checkup")

# Print the number of appointments after adding
after_appointments = appointment.get_appointment()
print(f"\nNumber of appointments after adding: {len(after_appointments)}")


#deleting the appointment
appointment_to_delete = 1
print(f"\nDeleting appointment:")
appointment.delete_appointment(appointment_to_delete)


#patient methods
patient=Patient()
patient.add_patient_data(
    first_name="John",
    last_name="Doe",
    sex="male",
    birth_date="1990-01-01",
    phone_number="1234567890",
    email="john.doe@example.com",
    addmission_date="2022-01-01",
    medication="Aspirin"
)

# Test deleting a patient
delete_first_name = "John"
delete_last_name = "Doe"
patient.delete_patient(delete_first_name, delete_last_name)


# Test the get_patient_by_id method
test_first_name = "John"
test_last_name = "Doe"
found_patient = patient.get_patient_by_name(test_first_name, test_last_name)

# Display the result
if found_patient:
    print(f"\nPatient found with first name {test_first_name} and last name {test_last_name}:")
    print(found_patient)
else:
    print(f"\nPatient not found with first name {test_first_name} and last name {test_last_name}.")



# Print patient details before update
test_first_name = "John"
test_last_name = "Doe"
before_update_patient = patient.get_patient_by_name(test_first_name, test_last_name)
print("\nPatient Details Before Update:")
print(before_update_patient)

# Test the update_patient_by_name method
update_data = {'medication': 'Ibuprofen'}
patient.update_patient_by_name(test_first_name, test_last_name, update_data)

# Print patient details after update
after_update_patient = patient.get_patient_by_name(test_first_name, test_last_name)
print("\nPatient Details After Update:")
print(after_update_patient)

print("\nDebug script execution completed.")
