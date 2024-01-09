from models.Doctor import Doctor, Base, engine
from models.Appointment import Appointment
from models.Patient import Patient



Base.metadata.create_all(engine)

# Instantiate a doctor object for testing
doctor = Doctor()
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


print("\nDebug script execution completed.")
